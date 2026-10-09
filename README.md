# ROI Course Authoring Template

Template repository for ROI Training **slide courses** and (soon) **labs**.  
It does **not** include the slide or lab viewer apps—only what instructors need to author content with an AI coding agent.

## What’s in this repo

| Path | Purpose |
| :--- | :--- |
| `course/` | Slide Markdown + shared `images/` (stock graphics + sample) |
| `labs/` | One folder per lab (`lab.md` + `images/`) |
| `.agents/skills/course-generator/` | Rules and layout templates for slide courses |
| `.agents/skills/course-graphics-designer/` | Visual polish pass: layouts, SVG, generated images, screenshots |
| `.agents/skills/course-editor/` | Proofreading pass: spelling, grammar, house-style typography |
| `.agents/skills/lab-generator/` | Rules and templates for hands-on labs |
| `.cursorrules`, `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` | Point every common coding agent at the skills |

## Quick start

1. **Create your course repo** from this template (GitHub → *Use this template*), or clone/copy it.
2. **Open the repo** in Cursor, VS Code (Copilot), Claude Code, Antigravity, or another agent-capable editor.
3. **Ask the agent** to create a course, for example:
   - *“Using the Course Generator skill, outline a 1-day intermediate course on … then write the chapter files under `course/`.”*
4. **Put slides under `course/`** (multi-file: `00-introduction.md`, `01-….md`, …) and keep shared graphics in `course/images/`.
5. **Ask for a graphics pass** with the Course Graphics Designer skill after the draft exists.
6. **Ask for an editor pass** with the Course Editor skill (spelling, grammar, typography).
7. **Preview slides** in the hosted HTML Slides Viewer (paste your GitHub course folder URL):
   - https://slidesv.roitraining.com/
8. **Labs** go under `labs/lab-NN-slug/` with `lab.md` (see Lab Generator skill). Preview at https://labv.roitraining.com/ (paste the lab folder URL).

Full workflow: **[AUTHORING.md](AUTHORING.md)**.

## Sample

Open `course/sample-course.md` in the slides viewer to see layouts and stock intro/outro images.

## Courses in this repo

- [Introducing the ROI Course Factory](https://slidesv.roitraining.com/?course=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/course) — how authors, editors, and instructors use the template, the viewers, and the skills. Source: `introducing-the-roi-course-factory/`.

## Related products

- Slides viewer: https://slidesv.roitraining.com/ (source: https://github.com/roitraining/md-to-html-slides-viewer)
- Lab viewer: https://labv.roitraining.com/ (source: https://github.com/roitraining/md-to-html-lab-viewer)
