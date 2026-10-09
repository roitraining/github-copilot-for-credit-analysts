# Course Graphics Designer — Visual Patterns

Copy these patterns when polishing decks for the HTML Slides Viewer.
Viewer syntax must match [../../course-generator/examples/layout-templates.md](../../course-generator/examples/layout-templates.md).

---

## 1. Media choice cheat sheet

| Need | Choose | Example filename |
| :--- | :--- | :--- |
| Labeled flow with accurate words | SVG | `images/ch02-apply-flow.svg` |
| Architecture boxes and arrows | SVG | `images/ch03-module-graph.svg` |
| Team collaboration metaphor | Generated photo (`1:1` or `16:9`) | `images/ch01-pair-programming.jpg` |
| Complex infographic scene | Generated (`16:9`), minimal text | `images/ch04-pipeline-overview.png` |
| Cloud console step | Screenshot or TODO | `images/ch02-s3-versioning-screenshot.png` |

---

## 2. Auto-split (square side image)

**When:** thesis bullets plus a supporting diagram or photo on the right.  
**Shape:** square (`1:1`).

```markdown
# Remote Backend Shape

- **Bucket / container** stores state objects
- **Lock table** prevents concurrent writes
- **IAM / identity** scopes least privilege
- **Encryption** at rest is mandatory

![Remote backend shape](images/ch02-remote-backend-shape.svg)
```

No `<!-- layout: … -->` comment. List + image triggers auto-split.

---

## 3. Stacked (wide image under bullets)

**When:** short bullets need a wide flow or timeline underneath.  
**Shape:** wide (`16:9` or `4:3`).

```markdown
<!-- layout: stacked -->
# Plan, Apply, Repeat

- Plan shows the blast radius before you change anything
- Apply makes the real change once the plan looks right
- The loop is how teams stay safe at speed

![Plan apply loop](images/ch01-plan-apply-loop.svg)
```

---

## 4. Title-image / image-only (16:9 hero diagram)

**When:** the diagram is the teaching point.

```markdown
<!-- layout: title-image -->
# Reference Architecture

![Reference architecture](images/ch02-reference-architecture.svg)
```

```markdown
<!-- layout: image-only -->
# Reference Architecture

![Reference architecture](images/ch02-reference-architecture.svg)
```

`image-only` hides the on-stage title but keeps the `#` heading for the slide tray. Use **16:9** assets.

---

## 5. Full-bleed mood slide (16:9, use sparingly)

```markdown
<!-- layout: full-bleed -->
# Why State Discipline Matters

![Operations center](images/ch02-state-discipline-bleed.jpg)
```

Keep the subject centered; edges may crop. Prefer generated photos with **no embedded text**.

---

## 6. Panel side art (tall or square)

Intro slides already use stock panel images. For a rare content-chapter panel:

```markdown
<!-- layout: panel-right -->
# When Local State Is Enough

- Solo prototypes on one laptop
- Throwaway sandboxes you will never share
- Learning labs before the team backend exists

![Local state](images/ch02-local-state-panel.svg)
```

**Shape:** tall (`3:4`) or square (`1:1`). Do **not** replace `welcome.png` / `agenda.png` / `who-should-attend.png` / `prerequisites.png`.

---

## 7. Columns and cards (usually no images)

Use for parallel text options. Do not force a diagram into these layouts.

```markdown
<!-- layout: 2-column -->
# Local vs Remote State

### Local
- Fast for solo prototypes
- No team sharing
- Easy to lose or overwrite

### Remote
- Shared source of truth
- State locking
- Audit-friendly workflows
```

```markdown
<!-- layout: card-layout -->
# Choose a Backend Shape

### Locking
- Concurrent writes must be blocked before they corrupt state.

### Durability
- State belongs in a service with versioning and encryption at rest.

### Access
- Grant the pipeline identity only what it needs to read and write state.
```

If students also need a picture, add a **follow-on** auto-split, stacked, or title-image slide.

---

## 8. Screenshot placeholder

```markdown
# Enable Bucket Versioning

- Turn on versioning before migrating state
- Confirm the setting in the cloud console

<!-- TODO IMAGE: Screenshot of AWS S3 console showing bucket versioning enabled -->
![S3 versioning console](images/ch02-s3-versioning-screenshot.png)
```

Acceptable outcome: wired path + clear TODO for the human. Do not fake the console with image generation when accuracy matters.

---

## 9. SVG starter (square flow)

Save as `images/ch01-plan-apply-loop.svg` (adjust `viewBox` for wide/tall needs).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" role="img" aria-label="Plan apply loop">
  <rect width="800" height="800" fill="#f5f7fa"/>
  <rect x="80" y="160" width="200" height="120" rx="16" fill="#1f4b99"/>
  <rect x="300" y="160" width="200" height="120" rx="16" fill="#1f4b99"/>
  <rect x="520" y="160" width="200" height="120" rx="16" fill="#1f4b99"/>
  <text x="180" y="230" text-anchor="middle" fill="#ffffff" font-family="Arial, Helvetica, sans-serif" font-size="36">Plan</text>
  <text x="400" y="230" text-anchor="middle" fill="#ffffff" font-family="Arial, Helvetica, sans-serif" font-size="36">Apply</text>
  <text x="620" y="230" text-anchor="middle" fill="#ffffff" font-family="Arial, Helvetica, sans-serif" font-size="36">Review</text>
  <path d="M280 220 H300" stroke="#334155" stroke-width="8" fill="none"/>
  <path d="M500 220 H520" stroke="#334155" stroke-width="8" fill="none"/>
  <path d="M620 280 V360 H180 V280" stroke="#334155" stroke-width="8" fill="none"/>
  <text x="400" y="420" text-anchor="middle" fill="#334155" font-family="Arial, Helvetica, sans-serif" font-size="32">Safe team loop</text>
</svg>
```

Prefer this over a generated diagram when labels must be spelled correctly.

---

## 10. Before / after thinking

**Before (weak):** four default bullet slides in a row, no visuals.

**After (stronger):**

1. Default thesis slide (text)
2. Auto-split with square SVG
3. `2-column` comparison (text)
4. `stacked` wide flow diagram
5. `title-image` architecture closer

Same teaching points; better pacing and retention.
