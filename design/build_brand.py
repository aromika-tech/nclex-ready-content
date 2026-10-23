#!/usr/bin/env python3
"""Brand cards for account launch: the welcome post, the first marketing post and
the profile avatar.

Same fixed brand system as build_social.py: Fraunces headings, Inter body, the brand
palette, left alignment, one accent per card and the platform safe zones. The two
feed cards reuse the "midnight" and "editorial" art directions from themes.py.

The logo is the live product mark (src/components/LogoMark.tsx in the app): a
diamond with a diamond cut-out. On dark grounds it takes a mint to teal gradient so
it stays visible, as the app does with its solid override on inverse surfaces.

USAGE
  python3 build_brand.py           writes publish/brand/{welcome,marketing,avatar}.jpg
"""
import os, pathlib, tempfile
from string import Template
from PIL import Image

from build_assets import FONT_CSS
from themes import THEMES, NAVY, NAVY_DEEP, TEAL, TEAL_DEEP, CREAM, MINT

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "publish" / "brand"
HANDLE, SITE = "@nclexready", "nclexready.com.au"
MARK_PATH = "M256 56 L456 256 L256 456 L56 256 Z M256 191 L321 256 L256 321 L191 256 Z"


def mark(size, c1, c2, gid):
    return (f'<svg viewBox="0 0 512 512" width="{size}" height="{size}" aria-hidden="true">'
            f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0%" stop-color="{c1}"/><stop offset="100%" stop-color="{c2}"/>'
            f'</linearGradient></defs>'
            f'<path fill="url(#{gid})" fill-rule="evenodd" d="{MARK_PATH}"/></svg>')


FEED = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:$PAGE;font-family:'Inter',sans-serif;color:$BODYC;position:relative}
.bg{position:absolute;inset:0;overflow:hidden;z-index:1}
.wrap{position:relative;z-index:2;height:1350px;padding:120px 88px 110px;
  display:flex;flex-direction:column}
.eyebrow{align-self:flex-start;font-size:21px;font-weight:700;letter-spacing:.14em;
  padding:12px 26px;border-radius:99px;color:$EYEFG;background:$EYEBG;margin-bottom:46px}
h1{font-family:'Fraunces',serif;font-weight:600;color:$HEAD;letter-spacing:-.03em;
  line-height:1.04;font-size:${H1}px;margin-bottom:44px;max-width:92%}
h1 em{font-style:italic;font-weight:500}
.rule{width:96px;height:4px;border-radius:2px;background:$ACCENT;margin-bottom:44px}
.lead{font-size:38px;line-height:1.36;color:$LEADC;font-weight:600;margin-bottom:34px;
  max-width:94%}
.body{font-size:29px;line-height:1.5;max-width:94%}
.spacer{flex:1}
.foot{display:flex;align-items:center;gap:18px;border-top:2px solid $RULE;padding-top:30px}
.bname{font-family:'Fraunces',serif;font-weight:500;font-size:32px;color:$BRANDNAME;
  letter-spacing:-.02em}
.meta{margin-left:auto;font-size:21px;font-weight:600;color:$HANDLEC}
.meta b{color:$SITEC;font-weight:700}
$EXTRA
</style></head><body>$DECO
<div class="wrap">
  <div class="eyebrow">$EYEBROW</div>
  <h1>$TITLE</h1>
  <div class="rule"></div>
  $LEAD
  <div class="body">$BODY</div>
  <div class="spacer"></div>
  <div class="foot">$MARK<div class="bname">NCLEX Ready</div>
    <div class="meta">$HANDLE&nbsp;&nbsp;·&nbsp;&nbsp;<b>$SITE</b></div></div>
</div></body></html>""")


def feed(theme, eyebrow, title, lead, body, accent, eyefg, eyebg, h1, mark_svg):
    th = THEMES[theme]
    return FEED.substitute(
        FONT_CSS=FONT_CSS, PAGE=th["page"], BODYC=th["body"], HEAD=th["head"],
        RULE=th["rule"], BRANDNAME=th["brandname"], HANDLEC=th["handle"], SITEC=th["site"],
        LEADC=th["lead"], EYEFG=eyefg, EYEBG=eyebg, ACCENT=accent, H1=h1,
        EXTRA=Template(th["extra_css"]).safe_substitute(ACCENT=accent),
        DECO=Template(th["deco"]).safe_substitute(ACCENT=accent),
        EYEBROW=eyebrow, TITLE=title, LEAD=f'<div class="lead">{lead}</div>' if lead else "",
        BODY=body, MARK=mark_svg, HANDLE=HANDLE, SITE=SITE)


WELCOME = feed(
    "midnight", "WELCOME", "Welcome to <em>NCLEX&nbsp;Ready</em>",
    "Your study page for the NCLEX-RN on the pathway to AHPRA registration.",
    "Free tools for internationally qualified nurses, taught to Australian clinical "
    "practice and drawn from primary sources. Short, practical teaching on "
    "prioritisation, delegation, pharmacology and the clinical judgement the exam now tests.",
    accent=MINT, eyefg=NAVY_DEEP, eyebg=MINT, h1=104,
    mark_svg=mark(54, MINT, TEAL, "mw"))

MARKETING = feed(
    "editorial", "WHY NCLEX READY", "Built for Australian practice, <em>not generic prep</em>",
    "",
    "The exam tests one standard. Your AHPRA registration follows another. We teach "
    "both, with every card grounded in Australian primary sources, the NMBA, ACSQHC and "
    "ANZCOR. So what you revise is what you will actually be registered to do.",
    accent=TEAL_DEEP, eyefg=TEAL_DEEP, eyebg="rgba(11,112,100,.10)", h1=96,
    mark_svg=mark(54, TEAL_DEEP, NAVY, "mm"))
# The editorial body sits a size up, since this card carries no lead line.
MARKETING = MARKETING.replace(".body{font-size:29px", ".body{font-size:34px")

AVATAR = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden}
body{background:radial-gradient(circle at 50% 42%,#163a72 0%,$NAVY 46%,$NAVY_DEEP 100%);
  display:flex;align-items:center;justify-content:center}
.stack{display:flex;flex-direction:column;align-items:center;text-align:center}
.word{font-family:'Fraunces',serif;font-weight:600;color:$CREAM;font-size:118px;
  line-height:.94;letter-spacing:.02em}
.rule{width:150px;height:5px;border-radius:3px;background:$MINT;margin:34px 0 26px}
.au{font-family:'Inter',sans-serif;font-weight:700;color:$MINT;font-size:30px;
  letter-spacing:.42em;margin-right:-.42em}
svg{margin-bottom:34px}
</style></head><body><div class="stack">$MARK
  <div class="word">NCLEX</div><div class="word">READY</div>
  <div class="rule"></div><div class="au">AUSTRALIA</div>
</div></body></html>""").substitute(FONT_CSS=FONT_CSS, NAVY=NAVY, NAVY_DEEP=NAVY_DEEP,
                                     CREAM=CREAM, MINT=MINT, MARK=mark(170, MINT, TEAL, "ma"))


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [("welcome", WELCOME, (1080, 1350)), ("marketing", MARKETING, (1080, 1350)),
            ("avatar", AVATAR, (1080, 1080))]
    with sync_playwright() as p, tempfile.TemporaryDirectory() as tmp:
        exe = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
        br = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None)
        for name, src, (w, h) in jobs:
            png = pathlib.Path(tmp) / f"{name}.png"
            pg = br.new_page(viewport={"width": w, "height": h})
            pg.set_content(src); pg.wait_for_timeout(300)
            pg.screenshot(path=str(png)); pg.close()
            Image.open(png).convert("RGB").save(OUT / f"{name}.jpg", "JPEG", quality=90,
                                                optimize=True, progressive=True)
            print(f"publish/brand/{name}.jpg")
        br.close()


if __name__ == "__main__":
    main()
