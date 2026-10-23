#!/usr/bin/env python3
"""Product, welcome and marketing posts from a JSON spec.

The same brand card as the launch posts (build_brand.FEED), in the editorial or
midnight look, rendered as 4:5 feed slides and a 9:16 story card. A spec lists slides;
one slide is a single-image post, two or more make a carousel.

  python3 build_product.py content/product/welcome.json

Spec:
  {"out_dir": "product/welcome", "story": 0,
   "slides": [{"theme": "midnight", "eyebrow": "WELCOME", "title": "Welcome to <em>NCLEX Ready</em>",
               "lead": "...", "body": "...", "points": ["...", "..."]}]}

"story" is the index of the slide that is also rendered as the 9:16 story card, or give
"story_slide" with its own content when the feed wording does not suit a Story.
Product numbers in a spec must come from a fresh database count on the day.
"""
import json, os, pathlib, sys, tempfile
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import build_brand as BB
from themes import NAVY, NAVY_DEEP, TEAL, TEAL_DEEP, MINT

LOOK = {
    "midnight": dict(accent=MINT, eyefg=NAVY_DEEP, eyebg=MINT, mark=(MINT, TEAL)),
    "editorial": dict(accent=TEAL_DEEP, eyefg=TEAL_DEEP, eyebg="rgba(11,112,100,.10)", mark=(TEAL_DEEP, NAVY)),
    "notecard": dict(accent=TEAL_DEEP, eyefg=TEAL_DEEP, eyebg="rgba(11,112,100,.10)", mark=(TEAL_DEEP, NAVY)),
    "chart": dict(accent=TEAL_DEEP, eyefg="#ffffff", eyebg=TEAL_DEEP, mark=(TEAL_DEEP, NAVY)),
}
POINTS_CSS = """
.pts{display:flex;flex-direction:column;gap:22px;margin-top:10px}
.pt{display:flex;gap:18px;font-size:31px;line-height:1.4}
.pt i{flex:0 0 14px;height:14px;border-radius:50%;background:ACC;margin-top:14px}
"""


def page(slide, height):
    look = LOOK[slide.get("theme", "editorial")]
    body = slide.get("body", "")
    if slide.get("points"):
        body += '<div class="pts">' + "".join(f'<div class="pt"><i></i><div>{p}</div></div>'
                                              for p in slide["points"]) + "</div>"
    src = BB.feed(slide.get("theme", "editorial"), slide["eyebrow"], slide["title"], slide.get("lead", ""),
                  body, look["accent"], look["eyefg"], look["eyebg"], slide.get("h1", 92),
                  BB.mark(54, *look["mark"], "m"))
    src = src.replace("$EXTRA", "").replace("</style>", POINTS_CSS.replace("ACC", look["accent"]) + "</style>")
    if height != 1350:
        src = src.replace("height:1350px", f"height:{height}px").replace(
            "padding:120px 88px 110px", "padding:230px 88px 260px")
    return src


def main():
    spec_path = pathlib.Path(sys.argv[1])
    spec = json.loads(spec_path.read_text())
    out = ROOT / "publish" / spec["out_dir"]
    out.mkdir(parents=True, exist_ok=True)
    jobs = [(f"slide{i + 1}", page(s, 1350), 1350) for i, s in enumerate(spec["slides"])]
    if "story_slide" in spec:
        jobs.append(("story", page(spec["story_slide"], 1920), 1920))
    elif "story" in spec:
        jobs.append(("story", page(spec["slides"][spec["story"]], 1920), 1920))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        exe = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
        br = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        for name, src, h in jobs:
            png = pathlib.Path(tmp) / f"{name}.png"
            pg = br.new_page(viewport={"width": 1080, "height": h})
            pg.set_content(src); pg.wait_for_timeout(300)
            pg.screenshot(path=str(png)); pg.close()
            Image.open(png).convert("RGB").save(out / f"{name}.jpg", "JPEG", quality=90, optimize=True, progressive=True)
            print(f"publish/{spec['out_dir']}/{name}.jpg")
        br.close()


if __name__ == "__main__":
    main()
