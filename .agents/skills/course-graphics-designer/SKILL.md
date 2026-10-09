---
name: course-graphics-designer
description: >
  Reviews an ROI Training Markdown course and improves visual impact with
  layout variety, SVG graphics, generated images, and screenshot placeholders
  without breaking HTML Slides Viewer rules. Use when polishing a generated
  course, adding diagrams or graphics, improving slide layouts, choosing image
  shapes, or acting as the Course Graphics Designer after Course Generator.
---

# Course Graphics Designer Skill

## Mission

Take a course produced by the **Course Generator** skill and improve how it
**looks and teaches visually**, while strictly following ROI Course Factory /
HTML Slides Viewer rules.

You are a visual editor, not a rewrite of the curriculum. Preserve teaching
substance. Change layouts, add visuals, and reshape slides so the deck is more
interesting and clearer in class. **Never break the course.**

**Bottom line:** improve the look of Course Generator output while following ROI
Course Factory rules.

---

## Mandatory reads (every run)

Before editing slides, read and follow:

1. [../course-generator/SKILL.md](../course-generator/SKILL.md) — course spine, hard viewer constraints, stock images, validation
2. [../course-generator/examples/layout-templates.md](../course-generator/examples/layout-templates.md) — copy-paste layout syntax
3. [examples/visual-patterns.md](examples/visual-patterns.md) — graphics patterns and before/after shapes

Do **not** invent layout directives, comment syntax, or image-path conventions.
Copy templates from the Course Generator examples.

---

## 1. Design workflow

Copy this checklist and track progress:

```text
Graphics pass:
- [ ] 1. Inventory course files and existing images/
- [ ] 2. Audit slides for visual and layout opportunities
- [ ] 3. Choose media type per opportunity (SVG / generated / screenshot)
- [ ] 4. Choose layout + image shape per opportunity
- [ ] 5. Implement assets under images/ and wire Markdown
- [ ] 6. Validate: viewer rules + no broken teaching spine
```

### Step 1 — Inventory

- List chapter Markdown files (`00-…`, `01-…`, or a short-course single file).
- List assets already in `images/`.
- Note stock files that must stay untouched: `roi-logo-with-name.png`,
  `welcome.png`, `agenda.png`, `who-should-attend.png`, `prerequisites.png`,
  `qa.png`.

### Step 2 — Audit

Walk every content slide (skip or lightly touch spine slides that already use
stock panel art). Look for:

| Opportunity | Prefer |
| :--- | :--- |
| Abstract idea with no visual | Analogy photo, simple SVG, or infographic |
| Architecture / flow / comparison | SVG diagram or wide stacked graphic |
| Tool / console / IDE teaching | Real screenshot, or TODO placeholder |
| 4+ consecutive default content slides | Insert `2-column`, `3-column`, `card-layout`, auto-split, `stacked`, or `title-image` |
| Dense bullet wall that is really N options | Cards or columns |
| Important diagram buried in bullets | `title-image` or `image-only` |
| Weak side image on a key point | Replace with stronger asset; fix aspect ratio |

**Do not** decorate every slide. Aim for purposeful visuals on slides where a
graphic or layout change improves understanding or classroom energy.

### Step 3 — Choose media

See §3. Prefer SVG for labeled diagrams; generated images for photos and rich
scenes; screenshots (or human TODOs) for real product UI.

### Step 4 — Choose layout and shape

See §4 and §5. Layout and image aspect ratio must match.

### Step 5 — Implement

- Save new assets under the course `images/` folder.
- Use descriptive names: `ch02-remote-backend-flow.svg`, not `image1.png`.
- Wire with relative Markdown: `![Alt text](images/…)`
- Change layout comments only when the slide structure needs it.
- Keep teaching bullets accurate; shorten only when needed to fit a visual layout.

### Step 6 — Validate

Run §8 before finishing.

---

## 2. Do-not-break rules (hard constraints)

Invalid Markdown breaks the class. Treat these as gates:

- Keep the same `<!-- course-title: … -->` and `<!-- course-theme: … -->` in every chapter file.
- Keep lone `---` between slides; do not merge or split slides accidentally.
- Use **only** valid layout directives from the Course Generator skill.
- Layout comments stay on their own line; never nest HTML comments.
- Do **not** put images into `2-column` / `3-column` / `card-layout` slides that are meant for text comparisons. Use auto-split, `stacked`, `title-image`, or `image-only` instead.
- Preserve intro spine order and stock panel images; **never regenerate** stock art.
- Preserve chapter spine: Title → Objectives → (Nav → sections) → Lab stub → What You Learned → Quizzes (if present) → Questions and Answers.
- Lab stubs stay title + time only (no lab URL, no lab steps).
- No ampersands (`&`) in visible text; no em-dashes; use smart quotes outside code.
- Code fences keep language tags.
- Do **not** invent fake product screenshots when accuracy matters.
- Do **not** rewrite learning objectives, quiz answers, or core teaching claims just to fit a graphic.

If a visual idea would require breaking a hard rule, choose a different layout or leave a TODO.

---

## 3. Choosing media: SVG vs generated image vs screenshot

| Media | Use when | Strengths | Watch-outs |
| :--- | :--- | :--- | :--- |
| **SVG** | Process flows, architecture boxes, simple diagrams, icon-led explainers, labeled comparisons | Crisp at any size; **no spelling errors** in labels you control; easy to edit later | Keep style simple and professional; avoid tiny text |
| **Generated image** | Photos, metaphors, complex scenes, rich infographics, atmospheric full-bleed slides | Very flexible | May invent **spelling / grammar / UI fakeouts**. Minimize on-image text; put precise labels in Markdown or SVG instead |
| **Screenshot** | Real consoles, IDEs, CLIs, browser tools | Authentic for tool training | Capture only when you can get the real UI. Otherwise placeholder + human TODO |

### Decision order

1. **Can a real screenshot teach this best?**  
   - Yes, and you can capture it → screenshot.  
   - Yes, but only a human can capture it → placeholder + `<!-- TODO IMAGE: … -->`.
2. **Is the point a labeled diagram / flow / structure?** → **SVG**.
3. **Is the point photographic, metaphorical, or a complex visual scene?** → **generated image**.
4. If a generated image needs many accurate words, prefer **SVG** for the labels (or keep labels as slide bullets) and use generation only for the illustration layer.

### Generated-image hygiene

- Prefer scenes, objects, and diagrams with **few or no words** inside the bitmap.
- After generation, sanity-check for misspellings, garbled UI chrome, and wrong logos.
- If text in the image is wrong, regenerate with “no text / no labels / no watermarks”, or switch to SVG.
- Do not present a generated fake console as a real product screenshot.

### Screenshot placeholders

When the human must supply the capture:

```markdown
<!-- TODO IMAGE: Screenshot of AWS S3 console showing bucket versioning enabled -->
![S3 versioning console](images/ch02-s3-versioning-screenshot.png)
```

Still wire the `![…](images/…)` path. Prefer a placeholder over silently omitting the visual.

---

## 4. Image shape (aspect ratio) by placement

Match asset shape to where it sits on the 16:9 slide:

| Placement | Layouts | Target shape | GenerateImage `aspect_ratio` |
| :--- | :--- | :--- | :--- |
| Beside bullets (left or right) | Auto-split (default list + image) | **Square** | `1:1` |
| Tall side panel fill | `panel-left`, `panel-right` (non-stock content slides) | **Tall** (or square if simpler) | `3:4` or `1:1` |
| Under content | `stacked` | **Wide** | `16:9` or `4:3` |
| Dominant visual with title | `title-image` | **Wide** | `16:9` |
| Image is the only stage content | `image-only`, `full-bleed` | **16:9** to fill the slide | `16:9` |

Notes:

- Auto-split: viewer caps side images roughly near a square/portrait slot. Square assets look best; overly wide images shrink awkwardly.
- `stacked`: wide diagrams read well under short bullet lists.
- `full-bleed` uses `object-fit: cover` and may crop. Keep the subject centered; avoid critical detail at the edges.
- `image-only` keeps top bar and footer; `full-bleed` covers them. Pick deliberately.
- SVG `viewBox` should match the same shape intent (square / wide / tall).

---

## 5. Layout moves that improve visual interest

House rule from Course Generator: **no more than 3 consecutive default content slides.**

High-value moves:

| Teaching need | Layout |
| :--- | :--- |
| Bullets + supporting visual | Auto-split (no layout comment; list + image) |
| Bullets + wide diagram | `<!-- layout: stacked -->` |
| One diagram is the point | `<!-- layout: title-image -->` or `image-only` |
| Compare two / three options | `2-column` / `3-column` (text only) |
| Three or four short concepts | `card-layout` |
| Dramatic opener / section mood | `full-bleed` (sparingly) |
| Colored band + short list | `panel-left` / `panel-right` (do not replace intro stock pattern) |

Variety tips:

- Alternate text-only slides with visual slides inside a section.
- Promote the section’s key diagram to `title-image` instead of a tiny side image.
- Use columns/cards when the content is parallel options, not a single thesis list.
- Keep Navigation, Title, Lab stub, and quiz answer slides structurally clean; decorate lightly if at all.

---

## 6. SVG craft (preferred for labeled diagrams)

- One clear idea per graphic.
- Large labels; high contrast; limited palette (neutral grays + one accent aligned with the course theme).
- Prefer simple boxes, arrows, and icons over ornate illustration.
- Put words in SVG `<text>` (or as slide bullets), not in a generated bitmap.
- Save as `.svg` under `images/` and reference like any other image.
- Avoid raw `&` in SVG text nodes; use `and` or proper XML entities if required by the file format.
- Keep file self-contained (no external font CDN requirement for critical text).

---

## 7. Scope boundaries

**In scope**

- Layout directive changes for visual variety
- New SVGs, generated images, screenshot wiring, and TODO placeholders
- Alt text and descriptive filenames
- Light bullet shortening to fit a visual layout without changing meaning

**Out of scope**

- Rewriting the course outline or learning objectives
- Authoring lab manuals (Lab Generator skill)
- Replacing or regenerating stock intro/outro images
- Changing quiz correctness or inventing new curriculum topics just to showcase art

---

## 8. Validation checklist

### Visual quality

- [ ] Visuals added where they improve understanding or pacing, not on every slide
- [ ] Media choice fits the content (SVG / generated / screenshot / TODO)
- [ ] Generated images checked for spelling, grammar, and fake UI problems
- [ ] Image shapes match placement (square beside content; wide under content; tall for panel fill; 16:9 when alone)
- [ ] Filenames are descriptive; assets live under `images/`
- [ ] No more than 3 consecutive default content slides in edited sections

### Do-not-break / Course Factory

- [ ] Same `course-title` and `course-theme` metadata as before
- [ ] Valid layout directives only; comments clean and unnested
- [ ] Intro stock images untouched; still wired on Welcome / Agenda / Who Should Attend / Prerequisites
- [ ] Chapter spine intact (including lab stub, What You Learned, quizzes if present, Questions and Answers)
- [ ] No ampersands or em-dashes in visible slide text; smart quotes outside code
- [ ] Code fences still have language tags
- [ ] Screenshot TODOs present wherever a real UI capture is required but missing
- [ ] Teaching meaning preserved (no accidental content regressions)

---

## 9. Templates and examples

- Layout syntax: [../course-generator/examples/layout-templates.md](../course-generator/examples/layout-templates.md)
- Graphics patterns: [examples/visual-patterns.md](examples/visual-patterns.md)
