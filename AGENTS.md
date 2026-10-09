# Agent instructions — ROI course authoring

## Skills

- **Slide courses:** Always read and follow `.agents/skills/course-generator/SKILL.md` and `.agents/skills/course-generator/examples/layout-templates.md` when creating, outlining, editing, or validating slides.
- **Course graphics:** After a course is drafted (or when polishing visuals), read and follow `.agents/skills/course-graphics-designer/SKILL.md` and `.agents/skills/course-graphics-designer/examples/visual-patterns.md`. Improve layouts and graphics without breaking viewer rules.
- **Course editing:** For spelling, grammar, and house-style typography (smart quotes, no em-dashes, no ampersands), read and follow `.agents/skills/course-editor/SKILL.md` and `.agents/skills/course-editor/examples/editing-patterns.md`. Do not break code, directives, or product names.
- **Labs:** Always read and follow `.agents/skills/lab-generator/SKILL.md` and `.agents/skills/lab-generator/examples/lab-template.md` when creating or editing files under `labs/`.

## Repository layout

- `course/` — slide Markdown and `images/`
- `labs/lab-NN-slug/` — each lab’s `lab.md` plus `images/`
- Stock intro/outro slide images live in `course/images/`; copy/reuse those filenames; do not regenerate.

## Output expectations

- Prefer multi-file courses (`00-introduction.md`, `01-….md`, …) under `course/`; short single-deck courses may use one file.
- Same `<!-- course-title: … -->` in every chapter file.
- Same `<!-- course-theme: … -->` in every chapter file.
- No ampersand (`&`) in slide or lab titles/body text (use “and”).
- Content chapters: Lab stub → What You Learned → Quizzes (default) → Questions and Answers.
- Lab stub on slides: **title and time only** (no lab URL—humans add the link later).
- Questions and Answers: `Questions?` body **or** stacked + `images/qa.png`—pick one pattern per course.
- Labs: Title → Time Required → Overview (You learn how to) → optional Scenario → Lab Instructions (Task / Bonus Task) → Congratulations!; preferred file `lab.md`; no Qwiklabs `ql-*` tags.
- Preview labs at https://labv.roitraining.com/ (paste the lab folder URL).
