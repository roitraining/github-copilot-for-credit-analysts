---
name: lab-generator
description: >
  Designs and writes ROI Training hands-on lab manuals as Markdown for the HTML
  Lab Viewer—one folder per lab with lab.md, images, Overview, Lab Instructions,
  and Congratulations. Use when creating labs, lab guides, lab manuals, challenge
  steps, or pairing labs with course slide stubs.
---

# Lab Generator Skill

Write **clear, procedural lab manuals** for intermediate professionals. Output
compiles in the [HTML Lab Viewer](https://labv.roitraining.com/) as a single
Markdown document (not slide decks).

**Always read** [examples/lab-template.md](examples/lab-template.md) and the
sample at `labs/lab-01-sample-lab-viewer-format/lab.md`. Copy that structure
rather than inventing a new outline.

Labs are **simpler than slide courses**: one story, numbered tasks, copyable
commands, screenshots where useful. Prefer doing over lecturing.

---

## 1. Audience and tone

- Default: intermediate practitioners (same audience as the paired slide course unless the user says otherwise).
- Voice: **second person** (*you*), **simple present**, conversational but professional.
- Steps: begin with an **imperative** (Click, Run, Create, Configure…).
- Do **not** use the ampersand character (`&`) in titles or body text—write “and”.

---

## 2. Design workflow

1. Confirm what the learner should **accomplish** (outcomes) and **time** (often about **30 minutes**; match the course lab stub).
2. Outline **Tasks** (usually 3–6) that build sequentially. Prefer a **Bonus Task** unless it truly does not fit.
3. Write **one lab folder** with `lab.md` + `images/` (see §3).
4. **Test and illustrate** when you can (see §3a): run the lab steps if tools/access allow; capture or generate screenshots and diagrams; otherwise leave placeholders + TODO comments for humans.
5. If a slide course exists, ensure the chapter **lab stub** has the lab title and time only (Course Generator does not add the link—humans add that later).
6. Run the **Validation checklist** (§9).

---

## 3. Folder and file layout (required)

In the authoring template, labs live under `labs/`:

```text
labs/
  lab-01-getting-started/
    lab.md             # preferred filename (Lab Viewer opens the lab folder)
    images/
      task1-console.png
      architecture.png
  lab-02-remote-state/
    lab.md
    images/
```

### Naming

- Folder: `lab-NN-short-kebab-slug` aligned with course chapter/lab numbers when possible.
- Markdown: prefer **`lab.md`**. Preview by opening the **lab folder** URL in the Lab Viewer (not a deep link to a specific file unless debugging).
- Images: descriptive names under `images/`; never `image1.png`.

### Image references

Use relative paths from `lab.md`:

```markdown
![Create bucket dialog](images/create-bucket.png)
```

The Lab Viewer resolves relative images against the Markdown file’s directory.

### Preview

Open [https://labv.roitraining.com/](https://labv.roitraining.com/) and paste a GitHub URL to the **lab folder** (for example `…/labs/lab-01-getting-started`).

### 3a. Testing, screenshots, and generated images

Treat verification and visuals as part of authoring—not optional polish.

**Test the lab when you are able.** If you have access to the CLIs, consoles, APIs, browsers, or other tools the lab uses, execute the steps (or a faithful dry-run) and fix broken commands, wrong labels, missing flags, and bad ordering before you deliver. If you cannot fully test (no credentials, no product access, offline), say so briefly and still write the most accurate procedure you can.

**Create images and screenshots when you are able.**

- Capture real UI screenshots for non-obvious console or wizard steps
- Generate diagrams, architecture sketches, or annotated visuals when that teaches better than a raw screenshot
- Save files under `images/` with descriptive names; wire them with meaningful alt text

**If you cannot produce an accurate visual yet**, do not silently omit it and do not invent a fake product screenshot when accuracy matters. Instead:

1. Add the Markdown image reference (so the layout is ready)
2. Add a `<!-- TODO IMAGE: … -->` comment that tells a human exactly what to capture or create
3. Add a **placeholder image file** under `images/` (a simple labeled stub is fine) so the link is not broken

```markdown
<!-- TODO IMAGE: Console screenshot of the Create bucket dialog with Name and Location filled in -->
![Create bucket dialog](images/create-bucket.png)
```

Prefer a placeholder + TODO over a missing image or a fabricated UI that could mislead learners.

---

## 4. Required lab structure (in order)

Use **Title Case** for `#` and `##` headings. Use `### Task N: …` / `### Bonus Task N: …` with a **colon**, and **sentence case** after the colon (capitalize the first word and proper nouns only—not Title Case on every word).

| Section | Heading | Required? | Notes |
| :--- | :--- | :--- | :--- |
| Title | `# …` | Yes | Outcome-oriented; Title Case; include key product/tech names |
| Time Required | `## Time Required` | Yes | Prefer **`30 minutes`** (or the agreed duration). Write the full phrase, not a bare number |
| Overview | `## Overview` | Yes | Short narrative: *In this lab, you will…* / *In this lab, you…* what students do |
| You learn how to | `### You learn how to:` | Yes | Nested under Overview. Imperative bullets; one bullet per main task theme; begin each with a verb |
| Scenario | `## Scenario` | Optional | Business problem / use case framing |
| Lab Instructions | `## Lab Instructions` | Yes | Contains all tasks |
| Tasks | `### Task N: …` | Yes | Numbered tasks; setup belongs in **Task 1** (no separate Setup section) |
| Bonus | `### Bonus Task N: …` | Preferred | Fewer step-by-step hints; stretch goal similar to what they just practiced |
| Closing | `## Congratulations!` | Yes | *In this lab, you have:* + past tense of the “You learn how to” bullets |

### Overview and learning objectives

```markdown
## Overview

In this lab, you will configure a remote backend and migrate Terraform state for team use.

### You learn how to:
- Create a remote state bucket with versioning enabled.
- Configure a Terraform backend and migrate state.
- Verify that state locking prevents concurrent applies.
```

- Bullets under **You learn how to** are imperative, complete sentences with ending punctuation.
- Prefer one learning bullet per primary task (Bonus may share themes rather than adding a new bullet).

### Scenario (optional, but preferred)

Short description of the business problem or use case. Omit when the Overview already provides enough context.

### Lab Instructions and tasks

Under `## Lab Instructions`:

1. **`### Task 1: …`** — Include environment setup here (sign in, select project, open console/Cloud Shell, clone repo). Then the first real work.
2. **`### Task 2: …`** through **`### Task N: …`** — Continue the story.
3. **`### Bonus Task N: …`** — Preferred. Same domain, fewer hand-holding steps.

#### Task body pattern

1. One or two sentences: what this task achieves (not the full step list).
2. **Numbered steps** — restart at **1.** at the beginning of each task. Put a **blank line between each numbered step**. One primary user action per step when practical.
3. Fenced code with a **language tag**; introduce commands with purpose (“To list regions, run:”).
4. Screenshots for non-obvious UI; **meaningful alt text**; do not screenshot text that belongs in a code block.
5. **Callouts when appropriate** — see §4a. Prefer `[!NOTE]`, `[!IMPORTANT]`, and `[!WARNING]` in labs (TIP/CAUTION also supported).

Optional under a task: a short **Success criteria** bullet list when verification matters.

### 4a. Callouts / alerts (use when appropriate)

Add GitHub-style callouts in tasks when they help the learner. Do **not** sprinkle them on every step—use them for real guidance, constraints, or pitfalls.

| Alert | Use when |
| :--- | :--- |
| `> [!NOTE]` | Helpful context, expected results, or “you should see…” guidance |
| `> [!IMPORTANT]` | Must-follow constraints (ignore fine details for now, required settings, do not skip) |
| `> [!WARNING]` | Mistakes, destructive actions, or easy-to-miss failures |
| `> [!TIP]` | Optional shortcut (use sparingly) |
| `> [!CAUTION]` | Stronger than WARNING when the risk is high |

**Syntax** (blockquote + tag on the first line; blank line before the callout is fine):

```markdown
> [!NOTE]
> Your generated page should resemble the screenshot below, but it will not be fully functional yet.

> [!IMPORTANT]
> Ignore fine visual details for now. Focus on structure and layout.

> [!WARNING]
> Do not commit real project IDs or secrets to a shared repository.
```

Place callouts after the step (or cluster of steps) they apply to. Emulate the sample lab and patterns like the GCP Canvas labs.

### Congratulations!

```markdown
## Congratulations!

In this lab, you have:
- Created a remote state bucket with versioning enabled.
- Configured a Terraform backend and migrated state.
- Verified that state locking prevents concurrent applies.
```

Mirror the **You learn how to** list in past tense. No new procedures.

---

## 5. Lab Viewer Markdown correctness

The Lab Viewer is a single scrolling HTML page (TOC from headings) at
[https://labv.roitraining.com/](https://labv.roitraining.com/). It supports:

- Standard Markdown (headings, lists, tables, links, images)
- Fenced code blocks with language tags (copy button in the viewer)
- GitHub-style alerts: `[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`, `[!CAUTION]`

**Do not use** Qwiklabs-only tags or fragments (`ql-code-block`, `ql-infobox`,
`![[/fragments/…]]`, templated `ql-variable` syntax). Those belong in other
publishing systems, not this viewer.

External links are fine; the viewer opens them in a new tab.

---

## 6. Teaching quality bar

- One clear **story**: problem → approach → tasks → accomplishment.
- Prefer **transferable skills** over click-only tourism.
- Keep conceptual asides short; link out for deep docs.
- Tables for three or more related UI field/value pairs on the same screen.
- UI labels in **sentence case** in steps, even if the product UI is all caps.
- When a step ends with text the learner types, omit ending punctuation on that step.

---

## 7. Relationship to slide courses

- Course Generator writes a **lab stub** on slides: **title and time only**.
- Humans add the lab URL/link later.
- This skill writes the **full lab manual** under `labs/lab-NN-slug/lab.md`.

---

## 8. Explicit non-goals

- Do **not** write slide decks here (use Course Generator).
- Do **not** author Qwiklabs YAML, assessments, or `ql-*` markup unless the user explicitly asks for that platform.
- Do **not** invent credentials, project IDs, or secret values—use placeholders like `YOUR_PROJECT_ID`.
- Do **not** leave screenshot references without alt text, without a file on disk, or without a `<!-- TODO IMAGE: … -->` when the real asset is still missing.
- Do **not** invent fake product screenshots when accuracy matters—use a placeholder image + TODO for the human.
- Do **not** skip testing when you have the tools/access to run the lab steps.
- Do **not** add a separate top-level Setup or Prerequisites section—put setup steps in Task 1.
- Do **not** put a lab URL on the course stub (title and time only).

---

## 9. Validation checklist

Before delivering:

- [ ] Folder `labs/lab-NN-slug/` with **`lab.md`** and `images/` as needed
- [ ] Structure: Title → Time Required → Overview (with You learn how to) → (Scenario) → Lab Instructions (Task 1…N, Bonus preferred) → Congratulations!
- [ ] `#` / `##` headings use Title Case; tasks use `### Task N: …` with sentence case after the colon
- [ ] Time Required uses a full phrase such as `30 minutes`
- [ ] You learn how to bullets are imperative complete sentences with ending punctuation
- [ ] Setup appears in Task 1 (no standalone Setup section)
- [ ] Each task restarts numbering at 1; code fences have language tags
- [ ] Bonus Task included unless it clearly does not fit
- [ ] Congratulations past-tense mirrors You learn how to
- [ ] Lab tested when tools/access allow; known untested areas noted
- [ ] Screenshots/diagrams generated or captured when possible; otherwise placeholder image file + `<!-- TODO IMAGE: … -->` + meaningful alt text
- [ ] Images use `images/…` relative paths (no broken links)
- [ ] Callouts use correct `[!NOTE]|[!IMPORTANT]|[!WARNING]|[!TIP]|[!CAUTION]` syntax when used; NOTE/IMPORTANT/WARNING added where appropriate (not on every step)
- [ ] No `&` in titles/body; no `ql-*` / fragment syntax
- [ ] Second person, simple present
- [ ] Course stub (if any) has title and time only—no lab link authored here

---

## 10. Templates

Copy-paste skeleton: [examples/lab-template.md](examples/lab-template.md).  
Emulate the sample: `labs/lab-01-sample-lab-viewer-format/lab.md`.
