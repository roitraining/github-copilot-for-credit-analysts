# Course and lab authoring guidelines (GitHub Copilot)

When drafting or modifying **presentation slides** in this repository, follow:

- [.agents/skills/course-generator/SKILL.md](.agents/skills/course-generator/SKILL.md)
- [.agents/skills/course-generator/examples/layout-templates.md](.agents/skills/course-generator/examples/layout-templates.md)

When polishing **course visuals** (layouts, SVG diagrams, generated images, screenshot placeholders), follow:

- [.agents/skills/course-graphics-designer/SKILL.md](.agents/skills/course-graphics-designer/SKILL.md)
- [.agents/skills/course-graphics-designer/examples/visual-patterns.md](.agents/skills/course-graphics-designer/examples/visual-patterns.md)

When **proofreading** for spelling, grammar, and house-style typography, follow:

- [.agents/skills/course-editor/SKILL.md](.agents/skills/course-editor/SKILL.md)
- [.agents/skills/course-editor/examples/editing-patterns.md](.agents/skills/course-editor/examples/editing-patterns.md)

When drafting or modifying **labs**, follow:

- [.agents/skills/lab-generator/SKILL.md](.agents/skills/lab-generator/SKILL.md)
- [.agents/skills/lab-generator/examples/lab-template.md](.agents/skills/lab-generator/examples/lab-template.md)

Place slide chapters under `course/` with shared assets in `course/images/`. Place each lab under `labs/lab-NN-slug/` (`lab.md` + `images/`).

Reuse stock slide images in `course/images/`. Do not use the ampersand character in titles or body text; write “and” instead.

Content chapters default to quizzes after What You Learned. Lab stubs use title and time only (no lab URL). Questions and Answers may use `Questions?` or stacked + `qa.png`.

Preview labs at https://labv.roitraining.com/ by pasting the lab folder URL.
