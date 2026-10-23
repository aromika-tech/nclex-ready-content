# NCLEX Ready content system

The teaching curriculum and card generator behind the NCLEX Ready social accounts.

Seventy nursing topics mapped to the 2026 NCLEX-RN Test Plan, effective April 2026, with topic counts allocated by the blueprint's percentage midpoints so the teaching schedule mirrors what the exam weights. Every topic states Australian clinical practice directly and carries a verified free Australian source.

This repository is public so that automated sessions can read it without credentials. It is not an invitation to reuse the content. See the notice at the foot.

## Layout

```
content/topics.py            the single source of truth, 70 topics
content/build_calendar.py    regenerates the calendar and the plan from topics.py
content/today.py             works out which post is due, prints the morning brief
content/content-calendar.csv one row per post, 23 columns
content/10-week-plan.md      the readable syllabus
content/resource-library.md  every source used, by topic
design/build_social.py       the card generator
design/themes.py             five art directions
design/fonts/                brand woff2 files, vendored so this runs anywhere
design/build_publish.py      JPEG cards and silent reels for automated posting
publish/post-NN/             those files, one folder per post, served from jsDelivr
publish/manifest.json        public URL and caption for every post
```

## Running it

```bash
./setup.sh                   # once, on a fresh machine

cd content
python3 today.py             # the morning brief for the next due post
python3 today.py --peek 5    # what is coming up
python3 today.py --status    # how far through the cycle

cd ../design
python3 build_social.py --id 27              # every size, in the assigned look
python3 build_social.py --captions --id 27   # the caption
python3 build_social.py --week 4             # a whole week
```

## Automated posting

Instagram and Facebook fetch media from a public URL and take JPEG only, so every post is pre-rendered into `publish/` and served through jsDelivr (`https://cdn.jsdelivr.net/gh/aromika-tech/nclex-ready-content@main/publish/...`). The daily task posts from `publish/manifest.json`. After editing a topic, rebuild that post and commit:

```bash
cd design && python3 build_publish.py --id 27   # or --all
```

Art direction is assigned per template in `THEME_FOR_TEMPLATE`, so no theme flag is needed in normal use. Every slide of a carousel uses the same look, which the generator enforces.

After editing a topic, run `python3 content/build_calendar.py` to rebuild the calendar and the plan. Never hand-edit either output.

## Cycle state

This repository is read only in the automated flow, so the cycle position is not stored here. It lives in a small state file outside the repository, and is replayed onto a fresh checkout each morning:

```bash
python3 today.py --progress 12   # the first 12 are already posted
python3 today.py                 # so this prints number 13
```

The `Status` column in the committed calendar stays empty on purpose.

## Editorial rules that apply to anything generated from this

Australian English throughout. Australian practice is stated directly, never framed as a comparison or a translation of anything else.

No em-dashes and no semicolons, anywhere. Feed captions carry no call to action.

Every claim on a card traces to a named Australian body: ACSQHC, NMBA, AHPRA, TGA, Australian Prescriber, or a state health department. If it cannot be traced, it does not go on a card.

## Notice

Copyright Aromika Pty Ltd. All rights reserved. Published here for operational access, not licensed for reuse, redistribution or derivative works.

NCLEX Ready is an independent educational platform operated by Aromika Pty Ltd. It is not affiliated with, endorsed by, or connected to AHPRA, NMBA, NCLEX, Pearson VUE, or NCSBN. NCLEX is a registered trademark of NCSBN, used here for descriptive purposes only.

Nothing in this repository is clinical advice. It is exam preparation material and every clinical decision belongs to a registered practitioner working within their own scope and their own employer's policy.
