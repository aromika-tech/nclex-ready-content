# Social plan from 4 Nov 2026 (Dhruval, 31 Oct)

Replaces the 30 Oct reels-only plan (kept in content/plan-2026-10-30.md). Dhruval asked for:
- more promotion of the product: features and the student journey, not only education;
- three posts a day per channel;
- a different call to action on each post, matched to what the post is about;
- varied animation, with the same music level and pace;
- no "taught to Australian practice" selling line for now.

## Daily mix (per channel; YouTube takes Reels only)
1. One education quiz Reel: the next teaching post (N = posted + 1), written as a spec in
   content/product/qNN-reel.json with out_dir "post-NN" and its own on-screen lines.
   No "In Australia" lines; regulator names (NMBA, Ahpra) are fine where the topic needs them.
2. One feature Reel from the student-journey series, in order, then repeat with new hooks:
   1 readiness test, 2 weekly plan, 3 every wrong answer explained, 4 short lessons with a worked
   example, 5 spaced-repetition flashcards, 6 the 15-question weekly check that adapts the plan,
   7 adaptive mock exams (85 to 150 questions, about 2.5 hours, readiness report by area),
   8 case studies (100+, Next Gen formats), 9 the Today screen and journey bar to exam date,
   10 start free (7 days, no card; 8, 12, 16 or 20 weeks or a Self-study pass).
3. One more feature item: a carousel post (IG and FB) on alternate days, otherwise a second
   feature Reel. Carousels: "Your first week, step by step" (built), "What a study week looks
   like", "Your readiness report, explained", "Mock exam day: what you get", "From first test
   to exam day".
Only claim what the app does; check src/pages/Home.tsx and Pricing.tsx in aromika-tech/nclex-ready
if unsure, and recount any number in Supabase (rounded figures only).

## Calls to action (change every post; never the same one twice in a row on a channel)
Every Reel spec sets "cta": {show, say, url, note, banner}. Pick by the post's nature:
- quiz Reel: "Try free practice questions" (/sample-questions, no sign-up) or "Find your weak
  areas free" (/diagnostic);
- readiness, mock or report: "Take the free readiness test" / "Check where you stand" (/diagnostic);
- weekly plan, plan lengths: "See plans and prices" (/pricing);
- lessons, flashcards, practice tests, case studies, start free: "Start 7 days free" (/signup);
Captions end with a comment question that fits the post, then a direct link with UTM
(utm_source=<instagram|facebook|youtube>&utm_medium=<reel|post>&utm_campaign=<slug>) on
Facebook and YouTube, and a matching "link in bio" line on Instagram. Vary the wording.

## Look and sound
- Motion: set "motion" in each spec and rotate push, pull, drift, slide, wipe; never the same
  motion on two Reels in a row. Looks: editorial, notecard, chart, rotated.
- Music and pace unchanged: uplifting CC0 beds at the same level, GAP 0.6, tempo 0.93.
- Voice: Chatterbox default. Azure Natasha when AZURE_SPEECH_KEY exists. No other licensed
  voice is available yet; do not clone anyone's voice.
- Cover under 40 characters, a question or a common mistake. First spoken line under 8 words.
  15 to 25 seconds.

## Times (IST), 3 per channel per day, at least 2 hours apart, never on the hour or half hour
- Facebook: slot time in the morning, about 13:00, about 18:45.
- Instagram: about 09:20, about 13:15, plus the IG slot (or about 19:10 at weekends).
- YouTube: two Shorts at the day's YouTube slots.

## Buffer free cap
10 scheduled posts per channel. At three a day, about three days fit. Queue in date order;
the rest goes to content/pending.json for the next run.

## Results check, 4 Nov (24 Oct to 4 Nov, Buffer)
- Facebook: 43 posts, about 1,600 impressions, 2 reactions, 0 clicks.
- Instagram: 42 posts, about 500 views, reach about 470, 1 save, 0 followers. Average Reel watch time about 1.3 seconds.
- YouTube: 13 Shorts, about 230 views, 1 like.
- Reels carry nearly all reach; Stories and single cards are near zero. Quiz Reels and the case-studies Reel did best.
- Watch time is the problem to fix: viewers leave in the first second. Next builds: put the question on screen and say it in the first second (first spoken line under 6 words), keep Reels nearer 15 seconds than 25, and start with a direct question to the viewer.
