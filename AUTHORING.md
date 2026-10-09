# Authoring guide (instructors)

How to create an ROI Training course with this template and an AI coding agent.

## 1. Create your repository

- Prefer **GitHub → Use this template** so you get a clean course repo.
- Or copy this folder and `git init`.

You do **not** need the slides viewer or lab viewer source code in your repo.

## 2. Open in your editor

Use any editor with a coding agent:

- Cursor  
- Visual Studio Code + GitHub Copilot  
- Claude Code  
- Antigravity / Gemini  

Pointer files in this repo (`.cursorrules`, `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`) tell the agent to follow the Course Generator and Lab Generator skills. You should not need global machine setup.

If the agent seems unaware of the rules, say explicitly:

> Read `.agents/skills/course-generator/SKILL.md`, `.agents/skills/course-graphics-designer/SKILL.md`, `.agents/skills/course-editor/SKILL.md`, and `.agents/skills/lab-generator/SKILL.md`, then follow them.

## 3. Course layout (slides)

```text
course/
  00-introduction.md
  01-your-first-chapter.md
  02-…
  images/
    roi-logo-with-name.png   # stock — do not regenerate
    welcome.png
    agenda.png
    who-should-attend.png
    prerequisites.png
    qa.png
    …                        # your diagrams / screenshots
```

- **Multi-chapter courses:** one Markdown file per chapter (required by the skill).
- **Stock images** are already in `course/images/`. Copy them into place for every new course folder if you split courses later; do not reinvent them.
- Replace `course/sample-course.md` with your real chapters when you start (or keep it as a layout reference).

## 4. Labs layout

```text
labs/
  lab-01-getting-started/
    lab.md
    images/
  lab-02-…
```

Follow:

- [.agents/skills/lab-generator/SKILL.md](.agents/skills/lab-generator/SKILL.md)
- [.agents/skills/lab-generator/examples/lab-template.md](.agents/skills/lab-generator/examples/lab-template.md)

See also [labs/README.md](labs/README.md) and the sample at `labs/lab-01-sample-lab-viewer-format/lab.md`.

### Lab stubs on slides

Chapter endings include a **lab stub** with the **lab title and time only**. Do **not** add the lab URL in the stub—humans add the link later. Do not write full lab steps in the slide deck.

## 5. Work with the agent

Suggested sequence:

1. Share audience, duration, and objectives.
2. Ask for an **outline** (chapters → sections → labs) and confirm it.
3. Ask the agent to **write** `course/00-introduction.md` and each chapter file.
4. Ask the agent to run a **graphics pass** with the Course Graphics Designer skill (layouts, SVG, generated images, screenshot TODOs).
5. Ask the agent to run an **editor pass** with the Course Editor skill (spelling, grammar, smart quotes, no em-dashes or ampersands).
6. Ask the agent to **write** each lab under `labs/lab-NN-slug/` using the Lab Generator skill.
7. Ask it to run each skill’s **validation checklist**.
8. You review slides and labs in their viewers; fix content and visuals as needed.

## 6. Preview

### Slides

1. Push your repo to GitHub (public, or ensure the viewer can read it).
2. Open the [HTML Slides Viewer](https://slidesv.roitraining.com/).
3. **Open → GitHub**, paste the URL to your `course/` folder (or a single `.md` file).

Local alternative: run any static server in a checkout of the slides viewer and pass `?course=` at your Markdown URL.

### Labs

Use the [HTML Lab Viewer](https://labv.roitraining.com/) and paste a GitHub URL to the lab folder.

## 7. What not to do

- Do not paste an entire multi-chapter course into one mega-file (unless you intentionally author a short single-file workshop and accept that it diverges from the default skill).
- Do not invent instructor bios on the Welcome slide.
- Do not use `&` in slide titles/body (write “and”; use **Questions and Answers**, not “Q&A”).
- Do not regenerate the stock intro/outro images—reuse the files in `course/images/`.
- Do not put full lab procedures in slide Markdown—use `labs/` and the Lab Generator skill.
- Do not put a lab URL on the course lab stub (title and time only; humans add the link later).
- Do not use Qwiklabs `ql-*` tags or fragments in Lab Viewer manuals.

## 8. Skill reference

- Course: [.agents/skills/course-generator/SKILL.md](.agents/skills/course-generator/SKILL.md)  
- Course templates: [.agents/skills/course-generator/examples/layout-templates.md](.agents/skills/course-generator/examples/layout-templates.md)  
- Course graphics: [.agents/skills/course-graphics-designer/SKILL.md](.agents/skills/course-graphics-designer/SKILL.md)  
- Graphics patterns: [.agents/skills/course-graphics-designer/examples/visual-patterns.md](.agents/skills/course-graphics-designer/examples/visual-patterns.md)  
- Course editor: [.agents/skills/course-editor/SKILL.md](.agents/skills/course-editor/SKILL.md)  
- Editing patterns: [.agents/skills/course-editor/examples/editing-patterns.md](.agents/skills/course-editor/examples/editing-patterns.md)  
- Labs: [.agents/skills/lab-generator/SKILL.md](.agents/skills/lab-generator/SKILL.md)  
- Lab template: [.agents/skills/lab-generator/examples/lab-template.md](.agents/skills/lab-generator/examples/lab-template.md)  
