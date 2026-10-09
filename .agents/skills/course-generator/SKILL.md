---
name: course-generator
description: >
  Authors high-quality ROI Training slide courses for instructor-led classrooms
  (intermediate/advanced professionals), delivered as Markdown for the HTML
  Slides Viewer (multi-file by default; short courses may be one file). Use when
  creating or improving courses, presentations, chapter outlines, teaching
  content, converting docs to slides, or choosing layout directives.
---

# Course Generator Skill

## Mission (primary)

Your job is to write **great training courses**: decks an instructor can teach from
and professionals can learn from. Optimize for clear objectives, accurate substance,
concrete examples, and classroom pacing.

Structure, house style, and viewer syntax **serve that mission**. They are not the
mission. When house style and teaching quality conflict, **teaching quality wins**,
without breaking viewer hard constraints.

**Non-negotiable constraint:** Output must compile correctly in the **HTML Slides
Viewer**. Invalid layout comments, missing `---`, or broken fences produce a broken
class, not a stylistic preference.

Prefer scannable instructor-led slides - not beginner textbooks pasted into Markdown.

**Always read** [examples/layout-templates.md](examples/layout-templates.md) and copy
those templates for viewer syntax rather than inventing directives.

---

## 1. Audience and product context

- **Default audience**: intermediate professionals (e.g. programmers teaching programmers, managers with experience).
- **Advanced** courses when the topic warrants it; **beginner** only when the user explicitly asks.
- Duration ranges from about **1–2 hours** to **multi-day** (3–4 days). Size the outline to the allotted time.

---

## 2. Teaching craft (house style, not the mission)

Write for an instructor at the front of the room: one clear point per slide, enough
detail to teach, no filler.

### What “good” looks like

- Tangible objectives students can actually achieve
- Right altitude for the stated audience (default: intermediate/advanced)
- Concrete examples, contrasts, failure modes, and decision rules - not only definitions
- Slides an instructor can talk from without reading paragraphs aloud
- Professional tone: direct, concrete, minimal hype

### Usual pattern (House style)

- About **3–4 main bullets**; **first bullet is the thesis** of the slide
- Supporting bullets develop that thesis (exemplify, warn, or operationalize) - not a new topic
- Optional sub-bullets (**0–3**) for how / e.g. / watch-for
- **Two bullet levels maximum**; deeper structure → table, **2-column** / **3-column**, or a new slide
- Prefer **one-line, scannable** bullets

### Use judgment

- Prefer this pattern because it keeps decks consistent and teachable
- Depart when another shape teaches better (worked example, comparison table, code snippet, diagram-led slide, quiz, title/nav/lab templates)
- Do **not** sacrifice clarity, accuracy, or usefulness to “satisfy the bullet count”
- Never invent deep outline trees (**3+ levels**) or walls of prose
- Mix layouts; deepen selectively with examples and contrasts - not with more generic bullets
- Include code samples in programming courses 

---

## 3. Design workflow

1. List **tangible teaching objectives** (what students will know or be able to do).
2. Organize into **chapters → sections** that build sequentially for the time budget.
3. Present/confirm the outline with the user when practical.
4. **Write strong teaching content** for each section (examples, contrasts, decisions): see §2.
5. Emit course Markdown: **multi-file by default**; a **short course may be one file**. See §4.
6. Generate or placeholder **images** under `images/`. See §8.
7. Run the **Validation checklist** (§10) before delivering: quality and viewer conformance.

---

## 4. Course file layout (multi-file default)

**Default for multi-chapter / full-length courses:** emit separate files.

| File | Contents |
| :--- | :--- |
| Introduction (Chapter 0) | Intro spine only |
| Chapter 1…N | One file per content chapter |

### Naming convention

```text
00-introduction.md
01-getting-started.md
02-basic-language-syntax.md
…
images/          # shared visuals for all chapters
```

Use zero-padded indexes and short kebab-case slugs.

### Per-file rules

- Put the **same** `<!-- course-title: NNN: Short Name -->` at the top of **every** file (viewer footer).
- Put the **same** `<!-- course-theme: roi-theme -->` at the top of **every** file (viewer default theme).
- Each file is its own slide deck fragment: slides separated by a lone `---` line.
- Do **not** collapse a **multi-chapter** course into a single Markdown file out of convenience.

### Short-course exception

A **short** course (roughly a single sitting / one thin chapter’s worth of teaching: often ~1–2 hours or less, or when the user asks for one deck) may live in **one Markdown file**.

- Still use valid viewer syntax (`course-title`, `---`, layouts).
- Still include the intro spine and teaching structure appropriate to the length.
- Prefer a clear name such as `course.md` or `00-short-title.md`.
- If the outline grows into multiple substantial chapters, split into the default multi-file layout.

---

## 5. Timing heuristics (guidelines)

- ~**2–3 minutes** of lecture per content slide on average.
- Section: ~**6–10** teaching slides.
- Chapter: ~**3–4** sections → ~**30–40** slides → ~**90–120** minutes lecture (~**1.5–2.5 hours**).
- Activity/lab stub: estimate about **30 minutes** (title and time only on slides. Do not author lab steps or the lab URL).
- Full training day: aim for **4–5** labs (often 2 chapters morning, 2–3 afternoon). Adjust when lengths differ.

---

## 6. Required course structures

### Introduction chapter (`00-introduction.md`), in order

1. **Title**: `<!-- layout: title -->` (logo + course title/subtitle)
2. **Welcome!**: `<!-- layout: panel-right -->`. ROI positioning; Meet your instructor (Name / Background / Contact info placeholders. **Do not invent** a fake instructor); Let’s get started! Bullets stay in the light area. Wire **`images/welcome.png`** so it sits in the colored third.
3. **Course Objectives**: bullets: **1 overall course objective**, then **one objective per content chapter** (5 chapters → 6 bullets)
4. **Agenda**: `<!-- layout: panel-left -->`. List of **chapters** (course-level orientation; not section Navigation). Bullets in the light area. Wire **`images/agenda.png`** in the colored third.
5. **Who Should Attend**: `<!-- layout: panel-right -->`. Bullets in the light area. Wire **`images/who-should-attend.png`** in the colored third.
6. **Prerequisites**: `<!-- layout: panel-left -->`. Bullets in the light area. Wire **`images/prerequisites.png`** in the colored third.

### Each content chapter file, in order

1. **Chapter title page**: `<!-- layout: title -->`
2. **Chapter Objectives**
3. **For each section:**
   - **Navigation**: `<!-- layout: navigation -->`: full section list; bold **exactly one** current section (where we’ve been / where we are / where we’re going; ~2 seconds of instructor time)
   - **Section teaching slides** (~6–10 typical)
4. **Activity / Hands-On Lab**: lab title and time estimate **only** (no lab URL; humans add the link later). Labs are authored separately with the Lab Generator skill.
5. **What You Learned**: past tense of the Chapter Objectives (same ideas)
6. **Chapter quizzes**: default; see below (omit only when appropriate)
7. **Questions and Answers**: title `Questions and Answers`; body `Questions?` **or** `<!-- layout: stacked -->` with stock **`images/qa.png`** (pick one pattern per course and stay consistent)

### Chapter quizzes (default for content chapters)

**Where:** After **What You Learned**, immediately before **Questions and Answers**.

**Who gets them:** Each **content** chapter by default. Do **not** add this block to the Introduction (`00-…`) or to a course-summary / office-hours / pure closing chapter.

**When to omit:** The chapter is very short, or the user says they do not want quizzes. Otherwise include them.

**Format (follow exactly):** 3 questions, each with an answer/discussion-points slide:

1. **Quiz 1 of 3**: multiple choice (A–D)
2. **Quiz 1: Answer**: restate the question; `**Correct: X.** …`; short rationale bullets
3. **Quiz 2 of 3**: multiple choice (A–D)
4. **Quiz 2: Answer**: same answer pattern as Quiz 1
5. **Quiz 3 of 3: Discussion**: `<!-- layout: 2-column -->` with `### Prompt` and `### Discuss`
6. **Quiz 3: Discussion Points**: `<!-- layout: 2-column -->` with `### Strong Answers Mention` and `### Watch For`

**Quality bar:** Write good questions from **this chapter’s content**: application, decisions, and misconceptions, not trivia or gotchas. Distractors should be plausible. Discussion prompts should be usable in class for 2–4 minutes.

Copy-paste patterns: [examples/layout-templates.md](examples/layout-templates.md) (quiz templates).

---

## 7. Viewer Markdown correctness (hard constraints)

Slides only display correctly if they follow HTML Slides Viewer syntax. These rules
are **gates**, not the creative goal.

### Structure

- `<!-- course-title: … -->` at the top of **each** chapter file
- Lone `---` between slides
- Clean layout comments on their own line. Never nest HTML comments
- Valid directives only: `title` | `navigation` | `2-column` / `two-column` | `3-column` / `three-column` | `card-layout` / `cards` / `card` | `panel-left` / `left-panel` | `panel-right` / `right-panel` | `title-image` | `image-only` / `image` | `full-bleed` / `bleed` | `stacked` / `stack`

### Layout selection matrix

| Layout | Directive | Use when |
| :--- | :--- | :--- |
| **Title** | `<!-- layout: title -->` | Course cover and chapter dividers |
| **Navigation** | `<!-- layout: navigation -->` | Section orientation; bold exactly one active item |
| **Content** | *(omit)* | Default vertical bullets, short code, tables, alerts |
| **Auto-split** | *(omit)* | Same slide has **both** a bullet list and an image → list left, image right |
| **Two-column** | `<!-- layout: 2-column -->` | Compare two items; pros/cons; before/after. Columns start at `###`. Optional `<!-- below-columns -->` keeps a following alert full width under the columns |
| **Three-column** | `<!-- layout: 3-column -->` | Three parallel options. Columns start at `###`. Same `<!-- below-columns -->` marker for a full-width callout under the row |
| **Card layout** | `<!-- layout: card-layout -->` | Each `###` is a card title; dash list items become sentences in the card body (no bullets). Three cards in a row; four cards in a 2-by-2 grid |
| **Title-image** | `<!-- layout: title-image -->` | One large diagram/screenshot that should dominate |
| **Image-only** | `<!-- layout: image-only -->` | Full-stage image with **no visible title**; keep an `#` heading in Markdown so the slide tray has a label |
| **Panel left** | `<!-- layout: panel-left -->` | Theme color fills the left third. Title and bullets stay in the light area. An image is centered in the colored third. Standard for Agenda and Prerequisites |
| **Panel right** | `<!-- layout: panel-right -->` | Same as panel left, with the colored third on the right. Standard for Welcome and Who Should Attend |
| **Full-bleed** | `<!-- layout: full-bleed -->` | Image covers the entire 16:9 slide, including top bar and footer. Keep an `#` heading for the tray label |
| **Stacked** | `<!-- layout: stacked -->` | Bullets/content on top, image below (full width); disables auto-split |

**Variety:** do not use default content layout more than **3 times in a row**.

### Callouts / alerts

Use when appropriate for teaching emphasis. Do not put a callout on every slide. Prefer NOTE, IMPORTANT, and WARNING in procedural teaching; TIP and CAUTION when they fit.

| Alert | Use for |
| :--- | :--- |
| `> [!NOTE]` | Context / background / expected results |
| `> [!TIP]` | Shortcuts / pro tips |
| `> [!WARNING]` | Pitfalls |
| `> [!IMPORTANT]` | Must-not-miss rules |
| `> [!CAUTION]` | Strong caution (supported by the viewer) |

```markdown
> [!NOTE]
> Remote state is shared. Coordinate before force-unlocking.

> [!IMPORTANT]
> Always enable locking before the team shares a backend.

> [!WARNING]
> Applying with the wrong workspace can destroy the wrong environment.
```

### Other syntax rules

- Code fences **must** include a language tag (` ```python `, ` ```bash `, ` ```hcl `, etc.)
- Avoid the **ampersand** (`&`) in visible slide text and titles (viewer/encoding issues). Write `and` instead. For example, **Questions and Answers**, not `Q&A`.
- Do **not** use em-dashes (U+2014, the long dash) in slide text or titles. Use a colon when you are introducing or explaining (`Quiz 1: Answer`, `Local state lives on one machine: no shared source of truth`). Use a normal hyphen (`-`) for a break or contrast (`slides - not a textbook`, `one prompt at a time - you drive every step`).
- Use **smart quotes** in visible slide text: curly apostrophes (`’`) and curly double quotes (`“` `”`). Examples: `Let’s`, `don’t`, `the “apply” step`. Leave straight quotes (`'` and `"`) inside code fences and inline code.

---

## 8. Images policy (required)

Visuals are part of course quality - not optional decoration.

### Standard stock images (this template)

This authoring template ships canonical intro/outro graphics under `course/images/`. **Reuse them. Do not regenerate:**

| File | Slide | Layout |
| :--- | :--- | :--- |
| `images/roi-logo-with-name.png` | Title / chapter dividers | `title` |
| `images/welcome.png` | Welcome! | `panel-right` |
| `images/agenda.png` | Agenda | `panel-left` |
| `images/who-should-attend.png` | Who Should Attend | `panel-right` |
| `images/prerequisites.png` | Prerequisites | `panel-left` |
| `images/qa.png` | Questions and Answers (optional alternative to `Questions?` body) | `stacked` |

Copy from `course/images/` in this repo (or from the HTML Slides Viewer `images/` folder) when starting a new course.

### When to use images

- Diagrams, analogies, infographics, charts, architecture drawings, AI-generated photos when they improve understanding or appeal
- Screenshots when teaching UI/tooling
- Prefer `title-image`, `image-only`, `full-bleed`, `stacked`, or auto-split when a visual should dominate, sit alone, fill the whole slide, sit below content, or sit beside bullets

### Where files live

- Store all course images under a shared **`images/`** folder beside the chapter Markdown files
- Reference with relative paths: `![Architecture overview](images/ch02-remote-state-diagram.png)`
- Use descriptive filenames (chapter/topic); never `image1.png`

### Generate vs placeholder

- **If you can create the image** (diagram/infographic/analogy/photo via available tools): save under `images/` and wire `![alt](images/...)`
- **If you cannot create an accurate asset** (real product screenshots, proprietary UI, exact branded captures): still add the Markdown image reference **and** a human TODO, e.g.

```markdown
<!-- TODO IMAGE: Screenshot of AWS S3 console showing bucket versioning enabled -->
![S3 versioning console](images/ch03-s3-versioning-screenshot.png)
```

- Never silently omit a needed visual; prefer a placeholder over a weak text-only slide
- Do **not** invent fake product screenshots when accuracy matters: use a placeholder
- Do **not** invent replacements for the template’s standard stock images: copy the canonical files

---

## 9. Explicit non-goals

- **Do not write lab exercise bodies**: only the lab stub slide (title and time; no URL)
- **Do not invent instructor bio**: use Welcome placeholders
- **Do not** collapse a multi-chapter / full-length course into one file for convenience (short single-deck courses are fine; see §4)
- **Do not** leave a broken image link without a TODO when the file was not generated
- **Do not** skip or replace the template’s standard stock images when authoring from this repo

---

## 10. Validation checklist

Before delivering, verify **teaching quality** and **viewer conformance**.

### Teaching quality

- [ ] Objectives are tangible and match the stated audience altitude
- [ ] Content slides generally have a clear thesis (often the first bullet)
- [ ] Chapters include concrete examples, contrasts, or decision rules - not definitions only
- [ ] Detail level fits the topic: short when that’s enough; deeper when it teaches
- [ ] Content-chapter quizzes (when present) test application of that chapter - not trivia
- [ ] Timing/size roughly matches requested duration

### Course spine and viewer conformance

- [ ] File layout fits length: multi-file (`00-…`, `01-…`) for multi-chapter courses; one file OK for short single-deck courses
- [ ] Same `<!-- course-title: … -->` in every file (or once at top if single-file)
- [ ] Intro slide order: Title → Welcome → Course Objectives → Agenda → Who Should Attend → Prerequisites
- [ ] Welcome and Who Should Attend use `<!-- layout: panel-right -->`; Agenda and Prerequisites use `<!-- layout: panel-left -->`
- [ ] Intro uses stock images when authoring from this template: `welcome.png`, `agenda.png`, `who-should-attend.png`, `prerequisites.png` (plus ROI logo on title)
- [ ] Course Objectives = 1 overall + 1 per content chapter
- [ ] Each content chapter: Title → Objectives → (Nav → section slides)… → Lab stub → What You Learned → Quizzes (default) → Questions and Answers last
- [ ] Every section Navigation lists **all** sections with **exactly one** `**bold**` item
- [ ] Lab stub has title and time estimate only (no lab steps; no lab URL authored here)
- [ ] What You Learned is past tense of Chapter Objectives; Questions and Answers is minimal (`Questions?` or stacked + `qa.png`)
- [ ] Content-chapter quizzes (unless omitted): 2 MCQs + 1 discussion, each with answer/points slides, grounded in chapter content; not on intro/summary closers
- [ ] Layout directives are valid; comments are clean (not nested)
- [ ] Alerts use correct `[!NOTE]|[!TIP]|[!WARNING]|[!IMPORTANT]|[!CAUTION]` syntax
- [ ] Code fences have language tags
- [ ] Visible slide text uses smart quotes (`’` `“` `”`); straight quotes stay inside code fences and inline code
- [ ] No em-dashes in slide text or titles. Use a colon or a normal hyphen (`-`) instead. No ampersands.
- [ ] Images live under `images/` with relative links; template stock set copied when using this repo; TODOs present where assets were not generated
- [ ] No more than 3 consecutive default content slides; no 3+ levels of bullet nesting

---

## 11. Templates

Copy-paste patterns: [examples/layout-templates.md](examples/layout-templates.md).
