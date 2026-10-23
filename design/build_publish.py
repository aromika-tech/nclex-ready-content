#!/usr/bin/env python3
"""Publish-ready files for the Instagram and Facebook APIs.

Meta fetches media from a public URL and only takes JPEG for photos, so this renders
each post as JPEG plus a short silent reel, into publish/post-NN/, and lists the public
jsDelivr URLs in publish/manifest.json. The daily task posts from those URLs.

USAGE
  python3 build_publish.py --all          every post (run once, then commit publish/)
  python3 build_publish.py --id 24        one post

Per post:
  feed.jpg                1080x1350, the single feed card (non-carousel)
  slide1.jpg .. slide5.jpg 1080x1350, carousel posts only
  story.jpg               1080x1920
  reel.mp4                1080x1920, silent, H.264. Carousel: story then each slide,
                          3 s each. Other posts: the story card with a slow 8 s zoom.

Needs ffmpeg. The files are fixed per post id: if an override changes the wording,
these no longer match and that day posts by hand instead.
"""
import argparse, json, os, pathlib, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_social as B
from PIL import Image

PUB = HERE.parent / "publish"
CDN = "https://cdn.jsdelivr.net/gh/aromika-tech/nclex-ready-content@main/publish"


def to_jpeg(png, jpg):
    Image.open(png).convert("RGB").save(jpg, "JPEG", quality=90, optimize=True, progressive=True)


def reel(dir_, slides, story):
    out = dir_ / "reel.mp4"
    enc = ["-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "27",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
    if not slides:
        # Slow push-in on the story card, 8 s.
        vf = ("scale=2160:3840,zoompan=z='min(zoom+0.0006,1.08)':d=240:"
              "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(story),
               "-vf", vf, "-t", "8", *enc]
    else:
        # Story card, then each slide centred on the slide's own background colour.
        frames = [story] + slides
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for f in frames:
            cmd += ["-loop", "1", "-t", "3", "-i", str(f)]
        parts = []
        for i, f in enumerate(frames):
            # Extend the slide's top edge colour upward and its bottom edge colour downward.
            im = Image.open(f).convert("RGB")
            top = "0x%02x%02x%02x" % im.getpixel((4, 4))
            bot = "0x%02x%02x%02x" % im.getpixel((4, im.height - 4))
            parts.append(f"[{i}]scale=1080:-2,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color={bot},"
                         f"drawbox=x=0:y=0:w=1080:h=(1920-1080*{im.height}/{im.width})/2:"
                         f"color={top}:t=fill,setsar=1[v{i}]")
        parts.append("".join(f"[v{i}]" for i in range(len(frames)))
                     + f"concat=n={len(frames)}:v=1:a=0[out]")
        cmd += ["-filter_complex", ";".join(parts), "-map", "[out]", *enc]
    subprocess.run(cmd, check=True)


def build(ids):
    from playwright.sync_api import sync_playwright
    manifest_path = PUB / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        exe = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
        br = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        tmp = pathlib.Path(tmp)
        for t in [t for t in B.CURRICULUM.TOPICS if t["id"] in ids]:
            th = B.theme_for(t)
            d = PUB / f"post-{t['id']:02d}"
            d.mkdir(parents=True, exist_ok=True)
            pages, slides = [], []
            if t["template"] == "carousel":
                for sl in range(1, 6):
                    png = tmp / f"s{sl}.png"
                    pages.append((png, B.render_html(t, "portrait", th, sl), B.FORMATS["portrait"]))
                    slides.append(png)
            else:
                pages.append((tmp / "feed.png", B.render_html(t, "portrait", th), B.FORMATS["portrait"]))
            pages.append((tmp / "story.png", B.render_html(t, "story", th), B.FORMATS["story"]))
            B.shoot(pages, br)

            files = {}
            for png, _, _ in pages:
                jpg = d / (f"slide{png.stem[1:]}.jpg" if png.stem.startswith("s") and png.stem != "story"
                           else f"{png.stem}.jpg")
                to_jpeg(png, jpg)
                files[jpg.stem] = f"{CDN}/{d.name}/{jpg.name}"
            reel(d, slides, tmp / "story.png")
            files["reel"] = f"{CDN}/{d.name}/reel.mp4"
            manifest[str(t["id"])] = {"title": t["title"], "template": t["template"],
                                      "caption": B.caption(t), "files": files}
            print(f"post {t['id']:02d}: {', '.join(files)}")
        br.close()
    manifest_path.write_text(json.dumps(dict(sorted(manifest.items(), key=lambda kv: int(kv[0]))),
                                        indent=1, ensure_ascii=False) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true"); ap.add_argument("--id", type=int)
    a = ap.parse_args()
    if not (a.all or a.id): ap.error("choose --all or --id N")
    PUB.mkdir(exist_ok=True)
    build({t["id"] for t in B.CURRICULUM.TOPICS} if a.all else {a.id})


if __name__ == "__main__":
    main()
