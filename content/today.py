#!/usr/bin/env python3
"""Work out which post is due, and print the morning brief for it.

The cycle position comes from the Status column in content-calendar.csv, not from
the date. So a missed day rolls forward instead of being skipped, which is what you
want: the syllabus stays intact and the cycle just runs one day longer.

  python3 today.py                 the next unposted topic, as a morning brief
  python3 today.py --id 27         a specific topic
  python3 today.py --peek 5        the next five, one line each
  python3 today.py --done 27       mark 27 posted and stamp the date
  python3 today.py --skip 27       push 27 to the back of the queue
  python3 today.py --status        how far through the cycle you are
  python3 today.py --progress 12   mark the first 12 in the queue as already posted

--progress exists because the repo the calendar ships in is read only. The cycle
position lives in a small state file outside the repo (Google Drive), and each
morning it is replayed onto a fresh checkout with one number.

--done takes the date from the caller, because a fresh session should pass the real
date in rather than trust the container clock:

  python3 today.py --done 27 --date 2026-08-11
"""
import argparse, csv, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from topics import TOPICS, WEEK_TITLES, THEME_FOR_TEMPLATE

CSV = HERE / "content-calendar.csv"

THEME_NAME = {"editorial": "Editorial", "midnight": "Midnight", "block": "Colour Block",
              "chart": "Clinical Chart", "notecard": "Study Card"}

TEMPLATE_NAME = {
    "fact": "Single-fact card", "qotd": "Question of the day",
    "mnemonic": "Mnemonic card", "ref": "Reference card",
    "compare": "Comparison card", "drug": "Drug card",
    "auvs": "Australian practice card", "carousel": "Carousel, 5 slides in one post",
}

CAROUSEL_SLIDES = [
    "Slide 1, the hook on its own",
    "Slide 2, what you will know by the end, first three points listed",
    "Slide 3, teaching points 1 and 2 unpacked",
    "Slide 4, teaching points 3 and 4 unpacked",
    "Slide 5, the Australian practice note and the common trap",
]


def load():
    with CSV.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def topic(tid):
    return next(t for t in TOPICS if t["id"] == int(tid))


def next_due(rows):
    for r in rows:
        if not r["Status"].strip():
            return r
    return None


def brief(row):
    t = topic(row["Post #"])
    th = THEME_FOR_TEMPLATE.get(t["template"], "editorial")
    L = []
    L.append(f"POST #{t['id']} of 70   Week {t['week']} of 10, day {t['day']}")
    L.append(f"Week theme: {WEEK_TITLES[t['week']]}")
    L.append(f"Funnel stage: {row['Funnel stage']}   "
             f"Primary goal: {row['Primary goal']}   Feed CTA: none")
    L.append("")
    L.append(f"FORMAT   {TEMPLATE_NAME[t['template']]}")
    L.append(f"LOOK     {THEME_NAME[th]}")
    L.append("")
    L.append(f"TITLE    {t['title']}")
    L.append(f"HOOK     {t['hook']}")
    L.append("")
    L.append("TEACHING POINTS")
    for i, f in enumerate(t["facts"], 1):
        L.append(f"  {i}. {f}")
    L.append("")
    L.append(f"AUSTRALIAN PRACTICE   {t['au']}")
    L.append(f"COMMON TRAP           {t['trap']}")
    L.append(f"SOURCE                {t['res']}")
    L.append(f"                      {t['url']}")
    L.append("")
    L.append(f"NCLEX category: {t['cat']}   Practise in: {t['nr_cat']}")

    if t["template"] == "carousel":
        L.append("")
        L.append("CAROUSEL STRUCTURE, all five slides in the Colour Block look")
        for s in CAROUSEL_SLIDES:
            L.append(f"  {s}")

    if t["day"] == 7 and row["Sunday story (this week)"]:
        L.append("")
        L.append("SUNDAY STORY, write this one by hand")
        L.append(f"  {row['Sunday story (this week)']}")

    L.append("")
    L.append("BUILD IT WITH")
    L.append(f"  cd design && python3 build_social.py --id {t['id']}")
    L.append(f"  cd design && python3 build_social.py --captions --id {t['id']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", type=int)
    ap.add_argument("--peek", type=int)
    ap.add_argument("--done", type=int)
    ap.add_argument("--skip", type=int)
    ap.add_argument("--date", default="")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--progress", type=int,
                    help="mark the first N in the queue as already posted")
    a = ap.parse_args()
    rows = load()

    if a.progress is not None:
        n = 0
        for r in rows:
            if n < a.progress:
                if not r["Status"].strip():
                    r["Status"] = "posted"
                n += 1
        save(rows)
        nxt = next_due(rows)
        print(f"replayed {a.progress} posted; next up "
              f"#{nxt['Post #'] if nxt else 'none, cycle complete'}")
        return

    if a.done:
        for r in rows:
            if int(r["Post #"]) == a.done:
                r["Status"] = f"posted {a.date}".strip()
                save(rows)
                print(f"marked #{a.done} as {r['Status']}")
                return
        sys.exit(f"no post #{a.done}")

    if a.skip:
        hit = [r for r in rows if int(r["Post #"]) == a.skip]
        if not hit:
            sys.exit(f"no post #{a.skip}")
        rows = [r for r in rows if int(r["Post #"]) != a.skip] + hit
        save(rows)
        print(f"pushed #{a.skip} to the back of the queue")
        return

    if a.status:
        done = [r for r in rows if r["Status"].strip()]
        nxt = next_due(rows)
        print(f"{len(done)} of {len(rows)} posted")
        if nxt:
            print(f"next up: #{nxt['Post #']}, {nxt['Topic']}")
        else:
            print("cycle complete, clear the Status column to start the next one")
        return

    if a.peek:
        pending = [r for r in rows if not r["Status"].strip()][:a.peek]
        for r in pending:
            print(f"#{r['Post #']:>3}  {r['Template name']:<28} {r['Art direction']:<15} "
                  f"{r['Topic']}")
        return

    row = ([r for r in rows if int(r["Post #"]) == a.id][0] if a.id else next_due(rows))
    if not row:
        print("Cycle complete. Clear the Status column in content-calendar.csv "
              "to start the next one.")
        return
    print(brief(row))


if __name__ == "__main__":
    main()
