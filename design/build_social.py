#!/usr/bin/env python3
"""NCLEX Ready social post generator.

Eight templates x five art directions x four formats, rendered from the 70-topic
curriculum in content/topics.py.

The brand system is fixed across every theme: two fonts (Fraunces headings, Inter
body), the brand palette, left alignment, one accent per card, and the platform safe
zones. Only the background treatment, layout structure and decorative layer change.

Art direction is assigned, not improvised. Each template has a fixed theme in
content/topics.py (THEME_FOR_TEMPLATE), so a week's posts vary in look while every
carousel stays internally consistent and every reference card looks like the last
reference card. Pass --theme to override for a one-off.

USAGE
  python3 build_social.py --week 3                     a full week, themes assigned
  python3 build_social.py --id 24 --fmt story          a single card
  python3 build_social.py --week 3 --theme chart       force one theme across a week
  python3 build_social.py --themes                     one card in all five themes
  python3 build_social.py --samples --theme midnight   one card per template
  python3 build_social.py --captions --week 3          captions for a week
"""
import argparse, pathlib, sys, html
from string import Template

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "content"))
import topics as CURRICULUM
from build_assets import FONT_CSS
from themes import THEMES, ORDER, NAVY, TEAL, TEAL_DEEP, PEACH, SAGE, GOLD, CREAM, MINT

OUT = HERE / "social"
OUT.mkdir(exist_ok=True)

HANDLE, SITE = "@nclexready", "nclexready.com.au"

FORMATS = {"portrait": (1080, 1350), "square": (1080, 1080), "story": (1080, 1920)}

# accent, light tint, eyebrow label. One accent per card, held across a set
STYLE = {
    "fact":     (TEAL_DEEP, "rgba(13,148,136,.09)",  "CLINICAL FACT"),
    "qotd":     (NAVY,      "rgba(15,45,94,.08)",    "QUESTION OF THE DAY"),
    "mnemonic": ("#8A6A2F", "rgba(201,169,122,.16)", "MEMORY AID"),
    "ref":      ("#166534", "rgba(168,201,160,.20)", "SAVE THIS REFERENCE"),
    "compare":  (TEAL_DEEP, "rgba(13,148,136,.09)",  "SIDE BY SIDE"),
    "drug":     ("#9A3412", "rgba(242,168,138,.18)", "DRUG CARD"),
    "auvs":     ("#8A6A2F", "rgba(201,169,122,.16)", "AUSTRALIAN PRACTICE"),
    "carousel": (TEAL_DEEP, "rgba(13,148,136,.09)",  "SWIPE"),
}
# On dark grounds the muted accents lose contrast, so each maps to a luminous partner.
MIDNIGHT_ACCENT = {"fact": MINT, "qotd": MINT, "mnemonic": GOLD, "ref": SAGE,
                   "compare": MINT, "drug": PEACH, "auvs": GOLD, "carousel": MINT}

BASE = Template("""
$FONT_CSS
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${W}px;height:${H}px;overflow:hidden}
body{background:$PAGE;font-family:'Inter',sans-serif;color:$BODYC;position:relative;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.bg{position:absolute;inset:0;overflow:hidden;z-index:1}
.wrap{position:relative;z-index:2;height:${H}px;padding:${PAD}px ${PADX}px;
  display:flex;flex-direction:column}
.headwrap{$HEADWRAP}
.top{display:flex;align-items:center;gap:16px;margin-bottom:${TOPGAP}px}
.mark{width:52px;height:52px;border-radius:14px;flex:0 0 52px;
  background:linear-gradient(135deg,$TEAL 0%,$NAVY 100%);
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 0 0 2px rgba(255,255,255,.16)}
.mark span{width:20px;height:20px;border-radius:5px;background:$CREAM;opacity:.95;
  transform:rotate(45deg);display:block}
.bname{font-family:'Fraunces',serif;font-weight:500;font-size:30px;color:$BRANDNAME;letter-spacing:-.02em}
.bhandle{font-size:19px;color:$HANDLEC;margin-left:auto;font-weight:500}
.eyebrow{display:inline-block;align-self:flex-start;font-size:20px;font-weight:700;
  letter-spacing:.09em;padding:11px 24px;border-radius:99px;margin-bottom:${EYEGAP}px;
  color:$EYEFG;background:$EYEBG}
h1{font-family:'Fraunces',serif;font-weight:600;color:$HEAD;letter-spacing:-.025em;
  line-height:1.1;font-size:${H1}px;margin-bottom:26px}
.body{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:22px}
.foot{display:flex;align-items:center;gap:14px;font-size:18px;color:$MUTED;
  border-top:2px solid $RULE;padding-top:20px;margin-top:22px}
.foot .src{flex:1;line-height:1.4}
.foot .site{font-weight:700;color:$SITEC;white-space:nowrap}

.lead{font-size:${LEAD}px;line-height:1.45;color:$LEADC;font-weight:600}
.pts{display:flex;flex-direction:column;gap:${PTGAP}px}
.pt{display:flex;gap:16px;align-items:flex-start}
.dot{flex:0 0 13px;height:13px;border-radius:50%;background:$ACCENT;margin-top:${DOTTOP}px}
.pt div{font-size:${PT}px;line-height:1.45}
.card{background:$CARD;border:2px solid $CARDBD;border-radius:24px;padding:30px 32px;
  box-shadow:$CARDSH}
.aub{background:$CARD;border-left:8px solid $GOLD;border-radius:0 16px 16px 0;
  padding:22px 26px;font-size:${AU}px;line-height:1.45;border-top:1px solid $CARDBD;
  border-right:1px solid $CARDBD;border-bottom:1px solid $CARDBD}
.aub b{color:$LEAD}
.answer{font-size:${PT}px;color:$MUTED;font-style:italic}
.slide{position:absolute;bottom:${PAD}px;right:${PADX}px;font-size:19px;color:$MUTED;font-weight:700;z-index:3}
$EXTRA
""")

SHELL = Template("""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8">
<style>$CSS</style></head><body>
$DECO
<div class="wrap">
  <div class="headwrap">
    <div class="top"><div class="mark"><span></span></div><div class="bname">NCLEX Ready</div>
      <div class="bhandle">$HANDLE</div></div>
    <div class="eyebrow">$EYEBROW</div>
    <h1>$TITLE</h1>
  </div>
  <div class="body">$BODY</div>
  <div class="foot"><div class="src">$SRC</div><div class="site">$SITE</div></div>
</div>$SLIDE</body></html>""")


def esc(s):
    return html.escape(str(s), quote=False)


def metrics(fmt):
    if fmt == "story":
        return dict(PAD=150, PADX=76, TOPGAP=52, EYEGAP=32, H1=70, LEAD=40,
                    PT=34, AU=31, PTGAP=26, DOTTOP=12)
    if fmt == "square":
        return dict(PAD=62, PADX=68, TOPGAP=34, EYEGAP=22, H1=56, LEAD=33,
                    PT=28, AU=26, PTGAP=17, DOTTOP=9)
    return dict(PAD=76, PADX=72, TOPGAP=42, EYEGAP=26, H1=62, LEAD=36,
                PT=31, AU=28, PTGAP=21, DOTTOP=10)


def points(facts, n=None):
    sel = facts[:n] if n else facts
    return ('<div class="pts">' + "".join(
        f'<div class="pt"><div class="dot"></div><div>{esc(f)}</div></div>' for f in sel)
        + '</div>')


def build_body(t, fmt, slide=None):
    tpl, n = t["template"], (3 if fmt == "square" else 4)
    if slide is not None:
        if slide == 1:
            return f'<div class="lead">{esc(t["hook"])}</div>'
        if slide == 2:
            return f'<div class="lead">By the end of this you will know:</div>{points(t["facts"],3)}'
        if slide in (3, 4):
            i = (slide - 3) * 2
            return points(t["facts"][i:i + 2])
        return (f'<div class="aub"><b>In Australia:</b> {esc(t["au"])}</div>'
                f'<div class="lead" style="font-size:28px;font-weight:500">'
                f'Common trap: {esc(t["trap"])}</div>')
    if tpl == "qotd":
        return (f'<div class="lead">{esc(t["hook"])}</div>'
                f'<div class="card">{points(t["facts"], n)}</div>'
                f'<div class="answer">What would you do first? Answer in the comments.</div>')
    if tpl == "auvs":
        return (f'<div class="lead">{esc(t["hook"])}</div>'
                f'<div class="aub"><b>Here:</b> {esc(t["au"])}</div>{points(t["facts"], n-1)}')
    if tpl in ("ref", "compare", "drug"):
        return f'<div class="lead">{esc(t["hook"])}</div><div class="card">{points(t["facts"], n)}</div>'
    if tpl == "mnemonic":
        return f'<div class="lead">{esc(t["hook"])}</div><div class="card">{points(t["facts"], n+1)}</div>'
    return (f'<div class="lead">{esc(t["hook"])}</div>{points(t["facts"], n)}'
            f'<div class="aub"><b>In Australia:</b> {esc(t["au"])}</div>')


def render_html(t, fmt, theme="editorial", slide=None):
    th = THEMES[theme]
    base_accent, tint, eyebrow = STYLE[t["template"]]
    accent = MIDNIGHT_ACCENT[t["template"]] if theme == "midnight" else base_accent

    real_fmt = "portrait" if slide is not None else fmt
    w, h = FORMATS[real_fmt]
    m = metrics(real_fmt)

    # eyebrow colours resolve per theme
    efg = {"ACCENT": accent, "ACCENT_SOLID": accent}.get(th["eyebrow_fg"], th["eyebrow_fg"])
    ebg = {"TINT": tint, "ACCENT_SOLID": accent}.get(th["eyebrow_bg"], th["eyebrow_bg"])

    # the colour-block theme wraps the header in a solid field that bleeds to the edges
    headwrap = ""
    if theme == "block":
        headwrap = (f"background:{accent};margin:-{m['PAD']}px -{m['PADX']}px 34px;"
                    f"padding:{m['PAD']}px {m['PADX']}px 44px;border-radius:0 0 64px 0;")

    extra = Template(th["extra_css"]).safe_substitute(
        ACCENT=accent, FIELDH="0", PADTOP=f"{m['PAD']}px",
        PADRAIL=f"{m['PADX']+22}px",
        PADCARD=f"{m['PAD']+46}px {m['PADX']+22}px {m['PAD']+16}px {m['PADX']+58}px")

    css = BASE.substitute(
        FONT_CSS=FONT_CSS, W=w, H=h, PAGE=th["page"], BODYC=th["body"], HEAD=th["head"],
        MUTED=th["muted"], RULE=th["rule"], CARD=th["card"], CARDBD=th["card_bd"],
        CARDSH=th["card_sh"], BRANDNAME=th["brandname"], HANDLEC=th["handle"],
        SITEC=th["site"], LEADC=th["lead"], EYEFG=efg, EYEBG=ebg, ACCENT=accent,
        HEADWRAP=headwrap, TEAL=TEAL, NAVY=NAVY, CREAM=CREAM, GOLD=GOLD,
        EXTRA=extra, **m)

    deco = Template(th["deco"]).safe_substitute(ACCENT=accent)
    return SHELL.substitute(
        CSS=css, DECO=deco, HANDLE=HANDLE, SITE=SITE,
        EYEBROW=eyebrow if slide is None else f"SWIPE · {slide} OF 5",
        TITLE=esc(t["title"]), BODY=build_body(t, fmt, slide),
        SRC=esc(f'Source: {t["res"]}'),
        SLIDE="" if slide is None else f'<div class="slide">{slide}/5</div>')


def theme_for(t):
    """The art direction this topic's template is assigned in content/topics.py."""
    return CURRICULUM.THEME_FOR_TEMPLATE.get(t["template"], "editorial")


def caption(t):
    facts = "\n".join(f"• {f}" for f in t["facts"])
    return (f"{t['hook']}\n\n{t['title']}\n\n{facts}\n\n"
            f"In Australia: {t['au']}\n\nWatch out for: {t['trap']}\n\n"
            f"Source: {t['res']}\n{t['url']}\n\n"
            f"Save this for your revision. What would you add?\n\n"
            f"#NCLEXRN #IQNAustralia #AHPRAPathway #NursingAustralia #NCLEXPrep")


def shoot(pages, browser):
    for path, src, (w, h) in pages:
        pg = browser.new_page(viewport={"width": w, "height": h})
        pg.set_content(src); pg.wait_for_timeout(300)
        pg.screenshot(path=str(path)); pg.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", type=int); ap.add_argument("--id", type=int)
    ap.add_argument("--fmt", default="portrait", choices=list(FORMATS))
    ap.add_argument("--theme", default=None, choices=list(THEMES),
                help="override the assigned theme for this run")
    ap.add_argument("--samples", action="store_true")
    ap.add_argument("--themes", action="store_true")
    ap.add_argument("--captions", action="store_true")
    a = ap.parse_args()
    T = CURRICULUM.TOPICS

    if a.captions:
        sel = [t for t in T if t["week"] == a.week] if a.week else [t for t in T if t["id"] == a.id]
        for t in sel:
            print("=" * 70); print(f"W{t['week']} D{t['day']} · {t['template']} · {t['title']}")
            print("=" * 70); print(caption(t), "\n")
        return

    pages = []
    if a.themes:                      # same card, every art direction
        base = [t for t in T if t["id"] == (a.id or 35)][0]
        for th in ORDER:
            pages.append((OUT / f"theme_{th}.png", render_html(base, "portrait", th),
                          FORMATS["portrait"]))
    elif a.samples:                   # one card per template, one theme
        seen, sel = set(), []
        for t in T:
            if t["template"] not in seen:
                seen.add(t["template"]); sel.append(t)
        for t in sel:
            th = a.theme or theme_for(t)
            pages.append((OUT / f"{th}_{t['template']}_{t['id']:02d}.png",
                          render_html(t, "portrait", th), FORMATS["portrait"]))
    else:
        sel = ([t for t in T if t["week"] == a.week] if a.week
               else [t for t in T if t["id"] == a.id])
        if not sel: ap.error("choose --themes, --samples, --week N or --id N")
        fmts = list(FORMATS) if a.week else [a.fmt]
        for t in sel:
            th = a.theme or theme_for(t)
            stem = f"w{t['week']:02d}d{t['day']}_{t['template']}_{t['id']:02d}_{th}"
            if t["template"] == "carousel":
                for sl in range(1, 6):
                    pages.append((OUT / f"{stem}_slide{sl}.png",
                                  render_html(t, "portrait", th, sl), FORMATS["portrait"]))
            for f in fmts:
                pages.append((OUT / f"{stem}_{f}.png",
                              render_html(t, f, th), FORMATS[f]))

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); shoot(pages, b); b.close()
    print(f"rendered {len(pages)} images -> {OUT}")


if __name__ == "__main__":
    main()
