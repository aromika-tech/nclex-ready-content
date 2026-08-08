"""Five art directions for NCLEX Ready social cards.

Same brand, five genuinely different looks. Each theme keeps the fixed brand system:
two fonts (Fraunces headings, Inter body), the brand palette, left alignment, a single
accent per card, and the platform safe zones, and varies only the things that should
vary: background treatment, layout structure, and the decorative layer.

Design rules applied to every theme (from current carousel design guidance):
  * two fonts maximum, three hierarchy levels maximum per card
  * body text at or above 20px on a 1080 canvas; line-height 130-150%
  * one accent colour per card, held consistent across a set
  * 4.5:1 minimum contrast; never pure black on pure white
  * text kept ~100px from the top and ~150px from the bottom (safe zones)
  * 30-40% of the canvas left as negative space
  * one focal point per card, left-aligned, top-to-bottom reading order
"""

NAVY, TEAL, TEAL_DEEP = "#0F2D5E", "#0D9488", "#0B7064"
PEACH, SAGE, GOLD = "#F2A88A", "#A8C9A0", "#C9A97A"
CREAM, INK, MUTED = "#FDF8F3", "#334155", "#64748B"
NAVY_DEEP = "#0A1F42"
MINT = "#5EEAD4"

THEMES = {

# ── 1. EDITORIAL, light, calm, serif-led. The default voice. ────────────────
"editorial": dict(
    label="Editorial",
    blurb="Light and calm. Serif headline on warm cream, soft colour haze.",
    page=CREAM, head=NAVY, body=INK, muted=MUTED, rule="rgba(15,45,94,.10)",
    card="#ffffff", card_bd="rgba(15,45,94,.10)", card_sh="0 10px 34px rgba(15,45,94,.06)",
    brandname=NAVY, handle=MUTED, site=TEAL_DEEP, lead=NAVY,
    eyebrow_fg="ACCENT", eyebrow_bg="TINT",
    deco="""<div class="bg">
      <div class="blob" style="background:$ACCENT;opacity:.10;width:620px;height:620px;top:-230px;right:-190px"></div>
      <div class="blob" style="background:#A8C9A0;opacity:.13;width:460px;height:460px;bottom:-160px;left:-170px"></div>
    </div>""",
    extra_css="""
    .blob{position:absolute;border-radius:50%;filter:blur(90px)}
    """),

# ── 2. MIDNIGHT, dark ground, high impact. Stops the scroll. ────────────────
"midnight": dict(
    label="Midnight",
    blurb="Dark navy ground, luminous accent. High contrast, stops the scroll.",
    page=NAVY_DEEP, head=CREAM, body="rgba(253,248,243,.82)", muted="rgba(253,248,243,.52)",
    rule="rgba(253,248,243,.16)",
    card="rgba(255,255,255,.06)", card_bd="rgba(255,255,255,.14)", card_sh="none",
    brandname=CREAM, handle="rgba(253,248,243,.55)", site=MINT, lead=MINT,
    eyebrow_fg="#0A1F42", eyebrow_bg="ACCENT_SOLID",
    deco="""<div class="bg">
      <div class="glow" style="background:$ACCENT;top:-260px;right:-200px"></div>
      <div class="glow" style="background:#0D9488;opacity:.30;width:520px;height:520px;bottom:-200px;left:-190px"></div>
      <div class="hair"></div>
    </div>""",
    extra_css="""
    .glow{position:absolute;border-radius:50%;filter:blur(110px);opacity:.42;width:660px;height:660px}
    .hair{position:absolute;inset:0;background-image:
      linear-gradient(rgba(255,255,255,.028) 1px,transparent 1px);background-size:100% 46px}
    .dot{box-shadow:0 0 14px $ACCENT}
    """),

# ── 3. BLOCK, a solid colour field carries the headline. Bold, graphic. ─────
"block": dict(
    label="Colour Block",
    blurb="Solid colour field carries the headline. Bold, graphic, unmistakable.",
    page=CREAM, head=CREAM, body=INK, muted=MUTED, rule="rgba(15,45,94,.10)",
    card="#ffffff", card_bd="rgba(15,45,94,.09)", card_sh="0 10px 30px rgba(15,45,94,.07)",
    brandname=CREAM, handle="rgba(253,248,243,.72)", site=TEAL_DEEP, lead=NAVY,
    eyebrow_fg="ACCENT", eyebrow_bg="#ffffff",
    deco="""<div class="bg"><div class="field" style="background:$ACCENT"></div></div>""",
    extra_css="""
    .field{position:absolute;top:0;left:0;right:0;height:$FIELDH;
      border-radius:0 0 64px 0}
    .wrap{padding-top:$PADTOP!important}
    h1{max-width:88%}
    .body{padding-top:14px}
    """),

# ── 4. CHART, the Australian observation chart as a design language. ────────
"chart": dict(
    label="Clinical Chart",
    blurb="Built from the observation chart, colour rail, grid, tabular numerals.",
    page="#FBFAF7", head=NAVY, body=INK, muted=MUTED, rule="rgba(15,45,94,.14)",
    card="#ffffff", card_bd="rgba(15,45,94,.16)", card_sh="none",
    brandname=NAVY, handle=MUTED, site=TEAL_DEEP, lead=NAVY,
    eyebrow_fg="#ffffff", eyebrow_bg="ACCENT_SOLID",
    deco="""<div class="bg">
      <div class="grid"></div>
      <div class="rail">
        <div style="background:#A8C9A0"></div><div style="background:#C9A97A"></div>
        <div style="background:#F2A88A"></div><div style="background:$ACCENT"></div>
        <div style="background:#0F2D5E"></div>
      </div>
      <div class="ticks"></div>
    </div>""",
    extra_css="""
    .grid{position:absolute;inset:0;background-image:
      linear-gradient(rgba(15,45,94,.11) 1px,transparent 1px),
      linear-gradient(90deg,rgba(15,45,94,.09) 1px,transparent 1px);
      background-size:46px 46px}
    .rail{position:absolute;left:0;top:0;bottom:0;width:38px;display:flex;flex-direction:column;
      box-shadow:2px 0 0 rgba(15,45,94,.18)}
    .rail div{flex:1}
    .ticks{position:absolute;left:38px;right:0;top:0;height:16px;
      background-image:linear-gradient(90deg,rgba(15,45,94,.30) 2px,transparent 2px);
      background-size:46px 100%;opacity:.55}
    body{font-feature-settings:"tnum" 1}
    .lead{letter-spacing:-.005em}
    .wrap{padding-left:$PADRAIL!important}
    .eyebrow{border-radius:4px!important;letter-spacing:.12em!important}
    .card{border-radius:6px!important;border-width:1.5px!important}
    .pt div{font-variant-numeric:tabular-nums}
    .aub{border-radius:0 6px 6px 0!important}
    h1{border-bottom:3px solid $ACCENT;padding-bottom:20px;display:inline-block}
    """),

# ── 5. NOTECARD, the study card. Paper, rule lines, a numbered tab. ─────────
"notecard": dict(
    label="Study Card",
    blurb="A study card on a tinted desk, ruled paper, corner tab, hand-made feel.",
    page="#EDF3EE", head=NAVY, body=INK, muted=MUTED, rule="rgba(15,45,94,.10)",
    card="#FCFBF8", card_bd="rgba(15,45,94,.10)", card_sh="0 6px 20px rgba(15,45,94,.05)",
    brandname=NAVY, handle=MUTED, site=TEAL_DEEP, lead=NAVY,
    eyebrow_fg="ACCENT", eyebrow_bg="TINT",
    deco="""<div class="bg">
      <div class="sheet"></div>
      <div class="tab" style="background:$ACCENT"></div>
    </div>""",
    extra_css="""
    .sheet{position:absolute;left:36px;right:36px;top:58px;bottom:34px;background:#FFFDF9;
      border-radius:8px 8px 22px 22px;box-shadow:0 20px 54px rgba(15,45,94,.13);
      border:1px solid rgba(15,45,94,.10);
      background-image:linear-gradient(rgba(15,45,94,.085) 1px,transparent 1px);
      background-size:100% 50px;background-position:0 150px}
    .sheet:after{content:"";position:absolute;left:96px;top:0;bottom:0;width:2px;
      background:rgba(242,168,138,.55)}
    .tab{position:absolute;left:36px;right:36px;top:58px;height:18px;
      border-radius:8px 8px 0 0;opacity:.95}
    .wrap{padding:$PADCARD!important}
    .card{background:rgba(13,148,136,.05)!important;box-shadow:none!important}
    """),
}

ORDER = ["editorial", "midnight", "block", "chart", "notecard"]
