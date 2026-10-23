#!/usr/bin/env python3
"""Voiced 9:16 Reels and Shorts from the 70-topic curriculum.

Each video reveals a topic one line at a time: the title as the question, the hook,
three teaching points, the Australian practice note, then the brand end card. The line
being spoken is highlighted and the rest are dimmed, so the on-screen text doubles as
captions for people watching with the sound off. Narration is Kokoro-82M (Apache-2.0,
runs on CPU). A CC0 bed from music/ plays underneath and ducks under the voice.

The look is the topic's assigned theme from themes.py, so a video matches its card.

USAGE
  python3 build_video.py --id 1                 publish/post-01/short.mp4
  python3 build_video.py --id 1 --voice bm_george
  python3 build_video.py --all

Needs: pip install kokoro-onnx soundfile, plus the two model files in $KOKORO_DIR
(kokoro-v1.0.onnx and voices-v1.0.bin from the kokoro-onnx model-files-v1.0 release).
"""
import argparse, html, json, os, pathlib, random, subprocess, sys, tempfile
from string import Template

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import build_social as B
from build_assets import FONT_CSS
from themes import THEMES, NAVY, TEAL, CREAM

W, H = 1080, 1920
FPS = 30
GAP = 0.35          # silence after each spoken line, seconds
END_HOLD = 2.6      # end card, seconds
DEFAULT_VOICE = "bf_emma"

# Mood per template, matched against the mood field in music/licences.json.
MOOD_FOR = {"fact": "calm", "auvs": "calm", "ref": "calm", "compare": "ambient",
            "mnemonic": "lo-fi", "drug": "ambient", "qotd": "reflective", "carousel": "lo-fi"}

FRAME = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${W}px;height:${H}px;overflow:hidden}
body{background:$PAGE;font-family:'Inter',sans-serif;color:$BODYC;position:relative}
.bg{position:absolute;inset:0;overflow:hidden;z-index:1}
$EXTRA
.wrap{position:relative;z-index:2;height:${H}px;padding:150px 84px 230px;display:flex;flex-direction:column}
.top{display:flex;align-items:center;gap:16px;margin-bottom:46px}
.mark{width:56px;height:56px;border-radius:15px;flex:0 0 56px;background:linear-gradient(135deg,$TEAL,$NAVY);
  display:flex;align-items:center;justify-content:center}
.mark span{width:21px;height:21px;border-radius:5px;background:$CREAM;transform:rotate(45deg);display:block}
.bname{font-family:'Fraunces',serif;font-weight:500;font-size:32px;color:$BRANDNAME}
.bhandle{margin-left:auto;font-size:21px;color:$HANDLEC;font-weight:600}
.eyebrow{align-self:flex-start;font-size:22px;font-weight:700;letter-spacing:.1em;padding:12px 26px;
  border-radius:99px;margin-bottom:30px;color:$EYEFG;background:$EYEBG}
h1{font-family:'Fraunces',serif;font-weight:600;color:$HEAD;letter-spacing:-.025em;line-height:1.08;
  font-size:${H1}px;margin-bottom:40px;transition:none}
.lines{display:flex;flex-direction:column;gap:30px}
.ln{font-size:${LN}px;line-height:1.38;opacity:.28;display:flex;gap:18px}
.ln .d{flex:0 0 14px;height:14px;border-radius:50%;background:$ACCENT;margin-top:${DOT}px}
.ln.hook{font-weight:600;color:$LEADC}
.ln.au{background:$CARD;border-left:8px solid $ACCENT;border-radius:0 18px 18px 0;padding:20px 24px}
.ln.on{opacity:1}
.ln.on.pt{color:$HEAD;font-weight:600}
h1.dim{opacity:.4}
.foot{position:absolute;left:84px;right:84px;bottom:150px;z-index:3;display:flex;align-items:center;gap:16px;
  font-size:20px;color:$MUTED}
.bar{flex:1;height:6px;border-radius:3px;background:$RULE;overflow:hidden}
.bar i{display:block;height:100%;width:$PCT%;background:$ACCENT}
.site{font-weight:700;color:$SITEC}
.end{position:absolute;inset:0;z-index:4;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:34px;background:$PAGE;text-align:center}
.end .w{font-family:'Fraunces',serif;font-weight:600;color:$HEAD;font-size:92px;line-height:1}
.end .s{font-size:34px;color:$BODYC;max-width:760px;line-height:1.4}
.end .u{font-size:30px;font-weight:700;color:$SITEC}
</style></head><body>$DECO
<div class="wrap">
  <div class="top"><div class="mark"><span></span></div><div class="bname">NCLEX Ready</div><div class="bhandle">$HANDLE</div></div>
  <div class="eyebrow">$EYEBROW</div>
  <h1 class="$H1CLS">$TITLE</h1>
  <div class="lines">$LINES</div>
</div>
<div class="foot"><div class="bar"><i></i></div><div>AI voice</div><div class="site">$SITE</div></div>
$END
</body></html>""")


def esc(s):
    return html.escape(str(s), quote=False)


def lines_for(t):
    """The spoken sequence. Kinds: title, hook, pt, au."""
    seq = [("title", t["title"]), ("hook", t["hook"])]
    seq += [("pt", f) for f in t["facts"][:3]]
    seq.append(("au", f"In Australia: {t['au']}"))
    return seq


def speakable(text):
    """Small fixes so the voice reads clinical shorthand naturally."""
    rep = {"ABC": "A B C", "ATS 1-5": "A T S, one to five", "1-5": "one to five", "e.g.": "for example",
           "i.e.": "that is", "&": "and", "/": " or ", "NCLEX-RN": "N-CLEX R N", "NCLEX": "N-CLEX",
           "ISBAR": "I-S-BAR", "EN ": "E N ", "RN ": "R N ", "AIN": "A I N", "NMBA": "N M B A",
           "ACSQHC": "the Commission on Safety and Quality in Health Care", "TGA": "T G A"}
    for a, b in rep.items():
        text = text.replace(a, b)
    return text.replace("'", "").replace("’", "")


def frame_html(t, theme, seq, step, end=False):
    th = THEMES[theme]
    base_accent, tint, eyebrow = B.STYLE[t["template"]]
    accent = B.MIDNIGHT_ACCENT[t["template"]] if theme == "midnight" else base_accent
    efg = {"ACCENT": accent, "ACCENT_SOLID": accent}.get(th["eyebrow_fg"], th["eyebrow_fg"])
    ebg = {"TINT": tint, "ACCENT_SOLID": accent}.get(th["eyebrow_bg"], th["eyebrow_bg"])
    if theme == "block":       # the colour field is sized for cards, so keep videos calm on cream
        efg, ebg = "#ffffff", accent
    body = []
    for i, (kind, text) in enumerate(seq[1:], start=1):
        if i > step:
            break
        cls = f"ln {kind}" + (" on" if i == step else "")
        dot = '<span class="d"></span>' if kind == "pt" else ""
        body.append(f'<div class="{cls}">{dot}<div>{esc(text)}</div></div>')
    end_html = ""
    if end:
        end_html = (f'<div class="end"><div class="w">NCLEX Ready</div>'
                    f'<div class="s">NCLEX-RN prep, taught to Australian practice</div>'
                    f'<div class="u">{B.SITE}</div></div>')
    extra = Template(th["extra_css"]).safe_substitute(ACCENT=accent, FIELDH="0", PADTOP="150px",
                                                      PADRAIL="106px", PADCARD="150px 106px 230px 142px")
    if theme == "block":
        extra = ""
    deco = "" if theme == "block" else Template(th["deco"]).safe_substitute(ACCENT=accent)
    pct = 100 if end else round(100 * step / (len(seq) - 1))
    return FRAME.substitute(
        FONT_CSS=FONT_CSS, W=W, H=H, PAGE=th["page"], BODYC=th["body"], HEAD=th["head"], MUTED=th["muted"],
        RULE=th["rule"], CARD=th["card"], BRANDNAME=th["brandname"], HANDLEC=th["handle"], SITEC=th["site"],
        LEADC=th["lead"], EYEFG=efg, EYEBG=ebg, ACCENT=accent, TEAL=TEAL, NAVY=NAVY, CREAM=CREAM,
        EXTRA=extra, DECO=deco, HANDLE=B.HANDLE, SITE=B.SITE, EYEBROW=esc(eyebrow), TITLE=esc(t["title"]),
        H1CLS="" if step == 0 else "dim", H1=74 if len(t["title"]) < 48 else 64, LN=40, DOT=17,
        LINES="".join(body), PCT=pct, END=end_html)


def pick_bed(template, seed):
    ledger = json.loads((ROOT / "music" / "licences.json").read_text())
    want = MOOD_FOR.get(template, "calm")
    pool = [l for l in ledger if want in l["mood"] and l["seconds"] >= 60] or \
           [l for l in ledger if l["seconds"] >= 60]
    return random.Random(seed).choice(pool)


def tts(kokoro, text, voice, path):
    import soundfile as sf
    samples, sr = kokoro.create(speakable(text), voice=voice, speed=1.0, lang="en-gb")
    sf.write(path, samples, sr)
    return len(samples) / sr


def build(t, voice, br, kokoro, out_dir):
    theme = B.theme_for(t)
    seq = lines_for(t)
    tmp = pathlib.Path(tempfile.mkdtemp())
    durs, wavs = [], []
    for i, (_, text) in enumerate(seq):
        wav = tmp / f"v{i}.wav"
        durs.append(tts(kokoro, text, voice, wav) + GAP)
        wavs.append(wav)
    # frames: one per spoken step, plus the end card
    pngs = []
    for step in range(len(seq)):
        p = tmp / f"f{step}.png"
        pg = br.new_page(viewport={"width": W, "height": H})
        pg.set_content(frame_html(t, theme, seq, step)); pg.wait_for_timeout(200)
        pg.screenshot(path=str(p)); pg.close(); pngs.append(p)
    p = tmp / "fend.png"
    pg = br.new_page(viewport={"width": W, "height": H})
    pg.set_content(frame_html(t, theme, seq, len(seq) - 1, end=True)); pg.wait_for_timeout(200)
    pg.screenshot(path=str(p)); pg.close(); pngs.append(p); durs.append(END_HOLD)

    # narration track: each line followed by its gap, then silence under the end card
    concat = tmp / "voice.txt"
    with concat.open("w") as f:
        for w_, d in zip(wavs, durs):
            f.write(f"file '{w_}'\n")
    voice_wav = tmp / "voice.wav"
    parts = []
    for i, (w_, d) in enumerate(zip(wavs, durs)):
        parts.append(f"[{i}:a]apad=whole_dur={d:.3f},aresample=44100,aformat=channel_layouts=mono[a{i}]")
    filt = ";".join(parts) + ";" + "".join(f"[a{i}]" for i in range(len(wavs))) + \
        f"concat=n={len(wavs)}:v=0:a=1,apad=pad_dur={END_HOLD}[v]"
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for w_ in wavs:
        cmd += ["-i", str(w_)]
    cmd += ["-filter_complex", filt, "-map", "[v]", str(voice_wav)]
    subprocess.run(cmd, check=True)
    total = sum(durs)

    # picture: still frames with short crossfades
    XF = 0.25
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for p_, d in zip(pngs, durs):
        cmd += ["-loop", "1", "-t", f"{d + XF:.3f}", "-framerate", str(FPS), "-i", str(p_)]
    vf, last, off = [], "[0:v]", 0.0
    for i in range(1, len(pngs)):
        off += durs[i - 1]
        vf.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off - XF / 2:.3f}[x{i}]")
        last = f"[x{i}]"
    vf.append(f"{last}format=yuv420p,trim=duration={total:.3f}[pic]")
    pic = tmp / "pic.mp4"
    cmd += ["-filter_complex", ";".join(vf), "-map", "[pic]", "-r", str(FPS), "-c:v", "libx264",
            "-preset", "medium", "-crf", "23", str(pic)]
    subprocess.run(cmd, check=True)

    # mix: bed from a random point, faded, ducked under the voice
    bed = pick_bed(t["template"], t["id"])
    bed_path = ROOT / "music" / bed["file"]
    start = random.Random(t["id"]).uniform(0, max(0, bed["seconds"] - total - 1))
    out = out_dir / "short.mp4"
    mix = (f"[1:a]atrim=start={start:.2f}:duration={total:.3f},asetpts=PTS-STARTPTS,volume=0.32,"
           f"afade=t=in:d=0.8,afade=t=out:st={total - 1.6:.3f}:d=1.6[bed];"
           f"[2:a]aresample=44100,aformat=channel_layouts=stereo,asplit=2[vo][sc];"
           f"[bed][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
           f"[duck][vo]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(pic), "-i", str(bed_path), "-i", str(voice_wav),
                    "-filter_complex", mix, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "160k", "-movflags", "+faststart", "-shortest", str(out)], check=True)
    return out, total, bed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", type=int); ap.add_argument("--all", action="store_true")
    ap.add_argument("--voice", default=DEFAULT_VOICE)
    a = ap.parse_args()
    if not (a.id or a.all): ap.error("choose --id N or --all")
    from kokoro_onnx import Kokoro
    from playwright.sync_api import sync_playwright
    kd = pathlib.Path(os.environ.get("KOKORO_DIR", "."))
    kokoro = Kokoro(str(kd / "kokoro-v1.0.onnx"), str(kd / "voices-v1.0.bin"))
    ids = {t["id"] for t in B.CURRICULUM.TOPICS} if a.all else {a.id}
    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
        br = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        for t in [t for t in B.CURRICULUM.TOPICS if t["id"] in ids]:
            d = ROOT / "publish" / f"post-{t['id']:02d}"
            d.mkdir(parents=True, exist_ok=True)
            out, total, bed = build(t, a.voice, br, kokoro, d)
            print(f"post {t['id']:02d}: short.mp4 {total:.1f}s, bed {bed['file']}")
        br.close()


if __name__ == "__main__":
    main()
