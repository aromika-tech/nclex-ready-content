#!/usr/bin/env python3
"""Regenerate the posting calendar and the 10-week plan from content/topics.py.

topics.py is the single source of truth. Edit a topic there, run this, and both
the CSV and the markdown plan update together. Nothing here is hand-maintained.

  python3 build_calendar.py

Writes:
  content/content-calendar.csv   one row per post, 23 columns, for the scheduler
  content/10-week-plan.md        the readable syllabus, for the study planner PDF
"""
import csv, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from topics import TOPICS, WEEK_TITLES, THEME_FOR_TEMPLATE

CSV_OUT = HERE / "content-calendar.csv"
MD_OUT = HERE / "10-week-plan.md"

DAYS = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday",
        5: "Friday", 6: "Saturday", 7: "Sunday"}

TEMPLATE_NAME = {
    "fact": "Single-fact card",
    "qotd": "Question of the day",
    "mnemonic": "Mnemonic card",
    "ref": "Reference card",
    "compare": "Comparison card",
    "drug": "Drug card",
    "auvs": "Australian practice card",
    "carousel": "Carousel (1 post, 5 slides)",
}

THEME_NAME = {"editorial": "Editorial", "midnight": "Midnight", "block": "Colour Block",
              "chart": "Clinical Chart", "notecard": "Study Card"}

# What each format is actually for. Saves are the strongest ranking signal, so the
# reference and memory formats carry the growth load and the rest fill in around them.
GOAL = {"ref": "SAVE", "compare": "SAVE", "drug": "SAVE", "mnemonic": "SAVE",
        "carousel": "SAVE + SHARE", "auvs": "SHARE", "qotd": "COMMENT", "fact": "REACH"}

# The four-stage arc. Weeks 1 and 2 ask for nothing at all, by design.
def stage(week):
    if week <= 2: return "TRUST"
    if week <= 4: return "TEACH"
    if week <= 7: return "INVITE"
    return "CONVERT"

# Every feed post carries no call to action. The invitation lives in Sunday Stories.
STORY = {
    1: "Introduce the 10-week syllabus and ask people to comment 'in' if they are "
       "starting with you. No link.",
    2: "Recap the week's four legal and professional posts in one frame. Ask what "
       "topic they want covered next. No link.",
    3: "Poll: which of this week's infection-control facts did you not know? Still no link.",
    4: "Share the medication-safety carousel again as a story. Mention that the "
       "syllabus is halfway to the halfway point. No link.",
    5: "First mention of the readiness test. Frame it as 'find out which of these "
       "areas is actually below your level'. Link sticker.",
    6: "Story the cardiac reference card, then the readiness test link under it.",
    7: "Ask a question about the week's emergencies, then link the readiness test in "
       "the reply frame.",
    8: "Readiness test link, with the line about the report naming specific areas "
       "rather than giving a score.",
    9: "Two frames: the end-of-life post that got the most saves, then the readiness "
       "test link.",
    10: "Close the cycle. The content was the syllabus, the platform is where you "
        "practise it, and the next cycle starts Monday. Link to plans.",
}


def rows():
    for t in TOPICS:
        theme = THEME_FOR_TEMPLATE.get(t["template"], "editorial")
        yield {
            "Week": t["week"],
            "Week theme": WEEK_TITLES[t["week"]],
            "Week marker": f"Week {t['week']} of 10",
            "Funnel stage": stage(t["week"]),
            "Day": DAYS[t["day"]],
            "Post #": t["id"],
            "Template": t["template"],
            "Template name": TEMPLATE_NAME[t["template"]],
            "Art direction": THEME_NAME[theme],
            "Theme key": theme,
            "Primary goal": GOAL[t["template"]],
            "Feed CTA": "None, feed stays pure teaching",
            "Topic": t["title"],
            "Hook": t["hook"],
            "NCLEX category": t["cat"],
            "Practise in": t["nr_cat"],
            "Australian practice": t["au"],
            "Common trap": t["trap"],
            "Resource": t["res"],
            "Resource URL": t["url"],
            "Generate": f"python3 build_social.py --id {t['id']}",
            "Sunday story (this week)": STORY[t["week"]] if t["day"] == 7 else "",
            "Status": "",
        }


def write_csv():
    data = list(rows())
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)
    return len(data)


PREAMBLE = """# NCLEX Ready, 10-Week Study and Content Plan

**70 topics. 7 posts a week. Mapped to the 2026 NCLEX-RN Test Plan, effective April 2026.**

Topic counts follow the blueprint's percentage midpoints, so the teaching schedule mirrors
what the exam weights. Every topic states Australian practice directly and carries a
verified free resource.

This file is generated. Edit `content/topics.py` and run `python3 build_calendar.py`.

## The eight templates, and the look each one wears

Art direction is assigned rather than rotated at random. Consistency builds recognition
faster than variety does, so a reference card always looks like a reference card and a
carousel always reads as one piece. The rule that matters most: never switch art
direction inside a carousel. Every slide in a single post must match.

| Template | Code | Art direction | Primary goal |
|---|---|---|---|
"""

THEME_GUIDE = """
## Why the art directions are assigned this way

There are five art directions in `design/themes.py`. Two sensible ways to use them exist,
and this plan takes the second.

*Pick one and own it.* Consistency builds recognition fastest. Editorial or Study Card are
the most sustainable for daily posting, and if a week ever gets away from you, falling back
to a single theme is the safe move.

*Assign by purpose.* Midnight opens and carries anything you want to travel, because a dark
card in a feed of white ones stops a thumb. Clinical Chart takes reference and lab-value
content, since it is literally built from the observation chart. Colour Block takes the
carousel, where a solid field holds a five-slide set together. Editorial carries everyday
teaching, and Study Card carries the memory aids and drug cards because it looks like the
thing your audience already writes by hand.

That gives a feed rhythm without looking scattered, and it removes a decision from every
posting day. The mapping lives in `THEME_FOR_TEMPLATE` in `content/topics.py`, so the
generator picks it up with no flag needed:

```bash
python3 build_social.py --week 3            # a full week, each post in its assigned look
python3 build_social.py --week 3 --theme chart   # force one look, for a themed week
```

Across a typical week this produces roughly four Editorial cards, one or two Study Cards,
one Chart, and either a Midnight question or a Block carousel. Enough variety to keep a
grid interesting. Not so much that it stops looking like one account.

---
"""


def write_md():
    out = [PREAMBLE]
    for code, name in TEMPLATE_NAME.items():
        th = THEME_FOR_TEMPLATE.get(code, "editorial")
        out.append(f"| {name} | `{code}` | {THEME_NAME[th]} | {GOAL[code]} |\n")
    out.append(THEME_GUIDE)

    for wk in range(1, 11):
        wt = WEEK_TITLES[wk]
        out.append(f"\n## Week {wk}: {wt}\n")
        out.append(f"\n*Funnel stage: {stage(wk)}. "
                   f"Sunday story: {STORY[wk]}*\n")
        for t in [x for x in TOPICS if x["week"] == wk]:
            th = THEME_FOR_TEMPLATE.get(t["template"], "editorial")
            out.append(f"\n### {DAYS[t['day']]} · #{t['id']} · "
                       f"{TEMPLATE_NAME[t['template']]} · {THEME_NAME[th]}\n")
            out.append(f"**{t['title']}**\n")
            out.append(f"\n> {t['hook']}\n\n")
            for fct in t["facts"]:
                out.append(f"- {fct}\n")
            out.append(f"\n**In Australia:** {t['au']}\n")
            out.append(f"\n**Common trap:** {t['trap']}\n")
            out.append(f"\n**Resource:** [{t['res']}]({t['url']})\n")
            out.append(f"\n*NCLEX category: {t['cat']} · practise in: {t['nr_cat']} "
                       f"· generate: `--id {t['id']}`*\n")
    MD_OUT.write_text("".join(out), encoding="utf-8")


if __name__ == "__main__":
    n = write_csv()
    write_md()
    dash = chr(0x2014)  # spelled out so this file stays clean
    bad = [p for p in (CSV_OUT, MD_OUT) if dash in p.read_text(encoding="utf-8")]
    print(f"{n} posts written to {CSV_OUT.name} and {MD_OUT.name}")
    print("em-dash check:", "FAILED in " + ", ".join(p.name for p in bad) if bad else "clean")
