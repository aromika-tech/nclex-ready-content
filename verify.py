#!/usr/bin/env python3
"""Check the kit for AI tells before anything ships. Run from the kit root."""
import pathlib, re, sys

EXT = {".md", ".csv", ".py", ".json", ".txt", ".html"}
SKIP = {"__pycache__", ".git", "social", "pkg"}
TELLS = ["delve", "tapestry", "testament to", "in today's world", "ever-evolving",
         "seamless", "myriad", "plethora", "cutting-edge", "game-changer",
         "it's not just", "it is not just", "let's dive", "moreover,", "furthermore,"]

# These files define the rules, so they legitimately quote the banned patterns.
RULE_FILES = {"verify.py", "brand-voice-core.md", "NEXT-CHAT-PROMPT.md", "SKILL.md",
              "START-HERE.md", "AUTOMATION-BRIEF.md", "DAILY-TASK-PROMPT.md",
              "DAILY-LOOP.md", "PAGE-SETUP.md"}

root = pathlib.Path(".")
bad_dash, bad_word = [], []
for p in root.rglob("*"):
    if not p.is_file() or p.suffix not in EXT: continue
    if any(s in p.parts for s in SKIP): continue
    try: txt = p.read_text(encoding="utf-8")
    except Exception: continue
    for i, line in enumerate(txt.split("\n"), 1):
        if "—" in line and "`—`" not in line:
            bad_dash.append(f"{p}:{i}: {line.strip()[:90]}")
        if p.name in RULE_FILES: continue
        low = line.lower()
        for t in TELLS:
            if t in low:
                bad_word.append(f"{p}:{i}: {t}")

if bad_dash:
    print("EM-DASHES FOUND:"); [print(" ", b) for b in bad_dash]
if bad_word:
    print("TELL WORDS FOUND:"); [print(" ", b) for b in bad_word]
if not bad_dash and not bad_word:
    print("clean: no em-dashes, no tell words")
sys.exit(1 if bad_dash or bad_word else 0)
