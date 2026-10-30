# Social plan from 3 Nov 2026 (Dhruval's decision, 30 Oct)

Dhruval asked for this plan to be made from the numbers. It replaces the 10-day schedule, which ends on Mon 2 Nov. **Do not ask him what to post next.** Follow this plan until he changes it.

## What the first week showed (Buffer, 23 to 30 Oct, 75 posts)
- Static cards, carousels and Stories (48 posts) reached almost no one. Facebook cards got 14 impressions in total. Instagram cards and Stories got 0.
- All the reach came from the 27 reels:
  - Facebook: about 1,170 impressions
  - Instagram: about 240 views
  - YouTube Shorts: about 120 views
- Instagram viewers leave after about 2 seconds on most reels.
- YouTube sent the most social visits to the site: 27 landings in 7 days, against 3 from Instagram.

## The plan
1. **One reel a day**, posted to Instagram, Facebook and as a YouTube Short. No static cards, carousels or Stories: stop building them. If content/pending.json still holds the Sun 1 Nov card and Story posts, queue them only if their time is still in the future, then empty the file.
2. **Mix per week:**
   - Five clinical quiz reels: the next teaching post (N = posted + 1), turned into a quiz.
   - One readiness-test walk-through reel: what the free test looks like and what you get at the end. Rotate the existing product specs with build_video.py --spec.
   - One pathway or news reel, only for a real update checked on the official page that day. Otherwise make a sixth quiz reel.
3. **Hook:**
   - Cover title under 40 characters, written as a question or a common mistake.
   - First spoken line under 8 words, and on screen from the first frame.
   - 15 to 20 seconds in total.
   - Shape: question, "Pause", answer, why in one line.
   - End with "Reply A or B" or a "what would you do" question.
4. **Link on every reel:** the caption and the YouTube description end with the comment prompt, then this link:
   https://www.nclexready.com.au/diagnostic?utm_source=<instagram|facebook|youtube>&utm_medium=reel&utm_campaign=post-NN (or the product slug)
   The readiness-test start screen was redesigned on 30 Oct, so the free test is the call to action on every reel.
5. **Slots (IST), one reel per channel per day, customScheduled:**

   | Channel | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
   |---|---|---|---|---|---|---|---|
   | Facebook | 06:46 | 08:44 | 08:08 | 08:12 | 08:47 | 07:56 | 09:16 |
   | YouTube | 21:56 | 20:41 | 21:09 | 19:28 | 17:31 | 18:11 | 19:16 |
   | Instagram | 20:16 | 19:00 | 18:20 | 10:55 | 07:38 | 19:13 | 19:13 |

6. **Weekly check, on the run that covers a Monday:**
   - From Buffer (includeMetrics): reach or views per reel by channel, and Instagram average watch time.
   - From Supabase (doxehmcltbyhcgbrdazh): site_events `landing` and `readiness_intro` rows by utm_source for the last 7 days. Use explicit columns and a LIMIT.
   - Targets by 16 Nov:
     - Instagram average watch time over 3 seconds.
     - Social visits that reach the readiness-test start screen growing week on week.
   - On 16 Nov, if YouTube is still the best source of visits, add a second Short a day on YouTube only. It is a re-cut of the same day's reel with a different hook. Tell Dhruval when you do this.
7. **When you arm the next run,** write this plan into its message instead of the old cards-and-Stories steps. Keep everything else the same: rules, engine, quality checks, Buffer cap, raw.githubusercontent URLs.

The rules are unchanged: Australian English, no em dashes or exclamation marks, no pass rates, no competitor or source names, no AI wording, rounded figures only.
