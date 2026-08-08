#!/usr/bin/env python3
"""Shared print and screen assets for every NCLEX Ready builder.

The six brand woff2 files are vendored in design/fonts/ and base64-embedded at build
time, so a fresh machine with nothing installed still renders the brand typography.
Every path here is relative to this file, so the kit runs from any directory.

Fonts are base64-embedded so any HTML built from these is fully self-contained and
renders with the brand typography (Fraunces headings, Inter body) rather than
substitutes. Imported by build_posters.py, build_b2b_brief.py and build_social.py.

Exports: FONT_CSS, the palette constants, DISCLAIMER, LOGO, qr_svg_path().

This module used to also carry a v1 A4 poster and product brief. Both were retired
in August 2026 and their copy no longer met the brand rules, so they were removed
rather than kept around.
"""
import base64, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FONT_DIR = HERE / "fonts"
OUT = HERE


def font_b64(rel: str) -> str:
    return base64.b64encode((FONT_DIR / rel).read_bytes()).decode()


FONTS = {
    "fraunces_500": font_b64("fraunces-latin-500-normal.woff2"),
    "fraunces_500i": font_b64("fraunces-latin-500-italic.woff2"),
    "fraunces_600": font_b64("fraunces-latin-600-normal.woff2"),
    "inter_400": font_b64("inter-latin-400-normal.woff2"),
    "inter_600": font_b64("inter-latin-600-normal.woff2"),
    "inter_700": font_b64("inter-latin-700-normal.woff2"),
}

FONT_CSS = """
@font-face {{ font-family:'Fraunces'; src:url(data:font/woff2;base64,{fraunces_500}) format('woff2'); font-weight:500; font-style:normal; }}
@font-face {{ font-family:'Fraunces'; src:url(data:font/woff2;base64,{fraunces_500i}) format('woff2'); font-weight:500; font-style:italic; }}
@font-face {{ font-family:'Fraunces'; src:url(data:font/woff2;base64,{fraunces_600}) format('woff2'); font-weight:600; font-style:normal; }}
@font-face {{ font-family:'Inter'; src:url(data:font/woff2;base64,{inter_400}) format('woff2'); font-weight:400; font-style:normal; }}
@font-face {{ font-family:'Inter'; src:url(data:font/woff2;base64,{inter_600}) format('woff2'); font-weight:600; font-style:normal; }}
@font-face {{ font-family:'Inter'; src:url(data:font/woff2;base64,{inter_700}) format('woff2'); font-weight:700; font-style:normal; }}
""".format(**FONTS)

# Brand palette, taken from the live product tokens.
NAVY, TEAL, TEAL_DEEP = "#0F2D5E", "#0D9488", "#0B7064"
PEACH, SAGE, EUCALYPT = "#F2A88A", "#A8C9A0", "#3E8B5C"
GOLD, CREAM, PAGE = "#C9A97A", "#FDF8F3", "#F8FAFC"
INK = "#334155"
MUTED = "#64748B"

DISCLAIMER = ("NCLEX Ready is an independent educational platform operated by Aromika Pty Ltd. "
              "It is not affiliated with, endorsed by, or connected to AHPRA, NMBA, NCLEX, "
              "Pearson VUE, or NCSBN. NCLEX is a registered trademark of NCSBN, used here for "
              "descriptive purposes only.")


def qr_svg_path(url: str) -> str:
    import qrcode  # only the print builders need this, so it stays out of the card path
    """Return QR as inline SVG rect path data (crisp at any print size)."""
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
    qr.add_data(url)
    qr.make(fit=True)
    m = qr.get_matrix()
    n = len(m)
    rects = "".join(
        f'<rect x="{x}" y="{y}" width="1" height="1"/>'
        for y in range(n) for x in range(n) if m[y][x]
    )
    return f'<svg viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges"><g fill="{NAVY}">{rects}</g></svg>'


LOGO = f"""
<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{TEAL}"/><stop offset="100%" stop-color="{NAVY}"/>
  </linearGradient></defs>
  <rect x="8" y="8" width="24" height="24" rx="5" transform="rotate(45 20 20)" fill="url(#lg)"/>
  <rect x="15" y="15" width="10" height="10" rx="2" transform="rotate(45 20 20)" fill="{CREAM}" opacity="0.92"/>
</svg>"""
