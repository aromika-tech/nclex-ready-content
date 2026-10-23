#!/usr/bin/env python3
"""Brand cards for account launch: the welcome post, the first marketing post and
the profile avatar, plus the Facebook and YouTube banners and Instagram highlight covers.

Same fixed brand system as build_social.py: Fraunces headings, Inter body, the brand
palette, left alignment, one accent per card and the platform safe zones. The two
feed cards reuse the "midnight" and "editorial" art directions from themes.py.

The logo is the live product mark (src/components/LogoMark.tsx in the app): a
diamond with a diamond cut-out. On dark grounds it takes a mint to teal gradient so
it stays visible, as the app does with its solid override on inverse surfaces.

USAGE
  python3 build_brand.py           writes publish/brand/{welcome,marketing,avatar}.jpg,
                                   banner-facebook.jpg, banner-youtube.jpg and highlight-*.jpg,
                                   with -light versions of the avatar and both banners

Banner safe zones: Facebook shows the full 1640x624 on desktop but only about the
centre 1110px width on mobile. YouTube shows the full 2560x1440 on TV, but on mobile
only the centre 1546x423. All text sits inside those boxes, the decoration bleeds.
"""
import os, pathlib, tempfile
from string import Template
from PIL import Image

from build_assets import FONT_CSS
from themes import THEMES, NAVY, NAVY_DEEP, TEAL, TEAL_DEEP, CREAM, MINT, INK, SAGE

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

AVATAR_T = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden}
body{background:$BG;
  display:flex;align-items:center;justify-content:center}
.stack{display:flex;flex-direction:column;align-items:center;text-align:center}
.word{font-family:'Fraunces',serif;font-weight:600;color:$FG;font-size:118px;
  line-height:.94;letter-spacing:.02em}
.rule{width:150px;height:5px;border-radius:3px;background:$ACC;margin:34px 0 26px}
.au{font-family:'Inter',sans-serif;font-weight:700;color:$ACC;font-size:30px;
  letter-spacing:.42em;margin-right:-.42em}
svg{margin-bottom:34px}
</style></head><body><div class="stack">$MARK
  <div class="word">NCLEX</div><div class="word">READY</div>
  <div class="rule"></div><div class="au">AUSTRALIA</div>
</div></body></html>""")


def avatar(look):
    if look == "light":
        return AVATAR_T.substitute(FONT_CSS=FONT_CSS, BG=CREAM, FG=NAVY, ACC=TEAL_DEEP,
                                   MARK=mark(170, TEAL_DEEP, NAVY, "ma"))
    return AVATAR_T.substitute(
        FONT_CSS=FONT_CSS, FG=CREAM, ACC=MINT, MARK=mark(170, MINT, TEAL, "ma"),
        BG=f"radial-gradient(circle at 50% 42%,#163a72 0%,{NAVY} 46%,{NAVY_DEEP} 100%)")


AVATAR, AVATAR_LIGHT = avatar("dark"), avatar("light")


BANNER = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${W}px;height:${H}px;overflow:hidden}
body{background:$BG;font-family:'Inter',sans-serif;position:relative}
.glow{position:absolute;border-radius:50%;filter:blur(${BLUR}px)}
.hair{position:absolute;inset:0;background-image:
  linear-gradient($HAIRC 1px,transparent 1px);background-size:100% ${HAIR}px}
.safe{position:absolute;left:50%;top:50%;width:${SW}px;height:${SH}px;
  transform:translate(-50%,-50%);display:flex;align-items:center;gap:${GAP}px}
.brand{display:flex;flex-direction:column;align-items:flex-start;gap:${BGAP}px;flex:0 0 auto}
.bname{font-family:'Fraunces',serif;font-weight:500;color:$FG;font-size:${BN}px;
  letter-spacing:-.02em;line-height:1}
.div{width:2px;align-self:stretch;background:$DIVC;margin:${DIVM}px 0}
.copy{display:flex;flex-direction:column;gap:${CGAP}px}
h1{font-family:'Fraunces',serif;font-weight:600;color:$FG;font-size:${H1}px;
  line-height:1.06;letter-spacing:-.025em}
h1 em{font-style:italic;font-weight:500;color:$ACC}
.sub{font-size:${SUB}px;color:$SUBC;line-height:1.4}
.site{font-size:${SITEF}px;font-weight:700;color:$ACC;letter-spacing:.02em}
</style></head><body>
<div class="glow" style="background:$G1C;opacity:$G1A;width:${G1}px;height:${G1}px;top:-${G1O}px;right:-${G1O}px"></div>
<div class="glow" style="background:$G2C;opacity:$G2A;width:${G2}px;height:${G2}px;bottom:-${G2O}px;left:-${G2O}px"></div>
<div class="hair"></div>
<div class="safe">
  <div class="brand">$MARK<div class="bname">NCLEX Ready</div></div>
  <div class="div"></div>
  <div class="copy">
    <h1>NCLEX-RN prep, built to <em>Australian practice</em></h1>
    <div class="sub">For internationally qualified nurses on the pathway to AHPRA&nbsp;registration</div>
    <div class="site">$SITE</div>
  </div>
</div></body></html>""")


# Dark is the midnight look, light is the editorial look of the marketing card.
BANNER_LOOK = {
    "dark": dict(BG=NAVY_DEEP, FG=CREAM, ACC=MINT, SUBC="rgba(253,248,243,.78)",
                 DIVC="rgba(253,248,243,.16)", HAIRC="rgba(255,255,255,.028)",
                 G1C=MINT, G1A=".34", G2C=TEAL, G2A=".32", M1=MINT, M2=TEAL),
    "light": dict(BG=CREAM, FG=NAVY, ACC=TEAL_DEEP, SUBC=INK,
                  DIVC="rgba(15,45,94,.12)", HAIRC="rgba(15,45,94,0)",
                  G1C=TEAL_DEEP, G1A=".10", G2C=SAGE, G2A=".22", M1=TEAL_DEEP, M2=NAVY),
}


def banner(W, H, SW, SH, k, look="dark"):
    """k scales type to the safe box, so both banners share one composition."""
    v = dict(GAP=56, BGAP=20, BN=40, DIVM=8, CGAP=16, H1=58, SUB=25, SITEF=23, MARKS=92)
    v = {a: round(b * k) for a, b in v.items()}
    L = dict(BANNER_LOOK[look])
    return BANNER.substitute(
        FONT_CSS=FONT_CSS, W=W, H=H, SW=SW, SH=SH, SITE=SITE, BLUR=round(H * .16), HAIR=round(46 * k),
        G1=round(H * 1.2), G1O=round(H * .45), G2=round(H * .9), G2O=round(H * .35),
        MARK=mark(v.pop("MARKS"), L.pop("M1"), L.pop("M2"), "mb"), **L, **v)


BANNER_FB = banner(1640, 624, 1060, 440, 1.0)
BANNER_YT = banner(2560, 1440, 1500, 400, 1.36)
BANNER_FB_LIGHT = banner(1640, 624, 1060, 440, 1.0, "light")
BANNER_YT_LIGHT = banner(2560, 1440, 1500, 400, 1.36, "light")

HIGHLIGHT = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8"><style>
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden}
body{background:radial-gradient(circle at 50% 50%,#163a72 0%,$NAVY 30%,$NAVY_DEEP 70%);
  display:flex;align-items:center;justify-content:center}
.c{display:flex;flex-direction:column;align-items:center;gap:30px}
.w{font-family:'Fraunces',serif;font-weight:600;color:$CREAM;font-size:$FS;line-height:1;
  letter-spacing:-.02em}
.r{width:110px;height:6px;border-radius:3px;background:$MINT}
</style></head><body><div class="c">$INNER</div></body></html>""")


def highlight(inner_html, fs="150px"):
    return HIGHLIGHT.substitute(FONT_CSS=FONT_CSS, NAVY=NAVY, NAVY_DEEP=NAVY_DEEP,
                                CREAM=CREAM, MINT=MINT, FS=fs, INNER=inner_html)


# Highlight covers show as a ~1080px-wide circle crop, so each holds one centred glyph.
HIGHLIGHTS = {
    "highlight-start": highlight(mark(300, MINT, TEAL, "h1")),
    "highlight-abc": highlight('<div class="w">ABC</div><div class="r"></div>'),
    "highlight-drugs": highlight('<div class="w">mg</div><div class="r"></div>', "190px"),
    "highlight-au": highlight('<div class="w">AU</div><div class="r"></div>', "190px"),
}


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [("welcome", WELCOME, (1080, 1350)), ("marketing", MARKETING, (1080, 1350)),
            ("avatar", AVATAR, (1080, 1080)),
            ("banner-facebook", BANNER_FB, (1640, 624)),
            ("banner-youtube", BANNER_YT, (2560, 1440)),
            ("avatar-light", AVATAR_LIGHT, (1080, 1080)),
            ("banner-facebook-light", BANNER_FB_LIGHT, (1640, 624)),
            ("banner-youtube-light", BANNER_YT_LIGHT, (2560, 1440))]
    jobs += [(n, src, (1080, 1920)) for n, src in HIGHLIGHTS.items()]
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
