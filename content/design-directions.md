# Five Art Directions

The problem with the first set was that all eight templates were the same cream card with a soft blob behind it. Different content, identical artwork.

These five directions fix that. Each is a genuinely different look, and each works across all eight templates and all four formats.

## What stays fixed, and what varies

The mistake would be to "vary" the brand, different fonts, different palettes, an accent per slide. Current design guidance is consistent that this reads as chaos rather than range. So the brand system is locked:

- **Two fonts only**: Fraunces for headings, Inter for body
- **The brand palette**: navy, teal, peach, sage, gold, cream
- **One accent per card**, held consistent across a set
- **Left-aligned, top-to-bottom** reading order
- **Body text at or above 20px** on a 1080 canvas, line-height 130–150%
- **4.5:1 minimum contrast**, never pure black on pure white
- **Safe zones**: text clear of roughly 100px top and 150px bottom
- **One focal point per card**, three hierarchy levels maximum

What varies is the part that should: **background treatment, layout structure, and the decorative layer.**

## The five

**Editorial**: light and calm. Serif headline on warm cream, a soft colour haze behind. This is the default brand voice and the safest for dense clinical content.

**Midnight**: deep navy ground with a luminous accent. Because the muted brand accents lose contrast on dark, each maps to a brighter partner: mint for teal, gold, peach, sage. Highest stopping power in a feed of white cards, and the strongest choice for a hook or a launch post.

**Colour Block**: a solid colour field carries the headline, with the content on cream beneath. The field is content-adaptive, so it grows with a longer title rather than clipping it. Bold, graphic, and the most "designed" of the five.

**Clinical Chart**: built from the Australian observation chart: a colour zone rail down the left edge, a fine grid, tick marks along the top, square corners and tabular numerals. This is the one that could only belong to a nursing brand, and it suits reference and lab-value content especially well.

**Study Card**: a ruled sheet on a tinted desk, with a bound top edge and a margin rule. Borrows the visual language of the thing your audience actually does every day, which makes it feel like a study note rather than an advertisement.

## How to use them

**Do not rotate randomly.** Two sensible approaches:

*Pick one and own it.* Consistency builds recognition faster than variety. Editorial or Study Card are the most sustainable for daily posting.

*Assign by purpose.* Midnight for the week opener and anything you want to travel; Chart for reference and lab-value cards; Colour Block for the carousel; Editorial or Study Card for everyday teaching. This gives a feed rhythm without looking scattered.

What to avoid is switching theme mid-carousel, within a single post, every slide must match.

```bash
python3 build_social.py --themes                    # compare all five on one card
python3 build_social.py --samples --theme midnight  # all 8 templates in one theme
python3 build_social.py --week 3 --theme chart      # a full week
```

Adding a sixth direction means adding one entry to `design/themes.py`, the generator picks it up automatically.
