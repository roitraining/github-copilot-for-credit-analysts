# ROI course authoring

This repository is for authoring ROI Training slide courses and labs.

## Mandatory skills

Before creating or editing **slide decks**, read and follow:

- `.agents/skills/course-generator/SKILL.md`
- `.agents/skills/course-generator/examples/layout-templates.md`

Before polishing **course visuals** (layouts, diagrams, generated images, screenshots), read and follow:

- `.agents/skills/course-graphics-designer/SKILL.md`
- `.agents/skills/course-graphics-designer/examples/visual-patterns.md`

Before **proofreading** courses for spelling, grammar, and house-style typography, read and follow:

- `.agents/skills/course-editor/SKILL.md`
- `.agents/skills/course-editor/examples/editing-patterns.md`

Before creating or editing **labs**, read and follow:

- `.agents/skills/lab-generator/SKILL.md`
- `.agents/skills/lab-generator/examples/lab-template.md`

## Layout

- Slides: `course/` (Markdown chapters + `course/images/`)
- Labs: `labs/lab-NN-slug/lab.md` + `images/`
- Reuse stock slide images in `course/images/` (`welcome.png`, `agenda.png`, `who-should-attend.png`, `prerequisites.png`, `qa.png`, ROI logo). Do not regenerate them.
- Default chapter quizzes after What You Learned (see Course Generator skill).
- Lab stubs on slides: title and time only (no link).

## Preview

Slides: https://slidesv.roitraining.com/  
Labs: https://labv.roitraining.com/  
