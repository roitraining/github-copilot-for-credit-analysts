# Sample Lab: Explore the Lab Viewer Format

## Time Required

30 minutes

## Overview

In this lab, you will practice the Markdown patterns used by ROI hands-on labs: overview and learning objectives, numbered tasks, copyable commands, optional screenshots, callouts, and a bonus challenge. Use this file as a reference when drafting real labs with the Lab Generator skill.

### You learn how to:
- Preview a lab folder in the HTML Lab Viewer.
- Reference images from an `images/` folder beside `lab.md`.
- Recognize the required lab section order and when to use NOTE, IMPORTANT, and WARNING callouts.

## Scenario

You are preparing a new ROI lab manual. Before writing production content, you need a working example of the Lab Viewer format so every lab in the course looks and behaves the same way.

## Lab Instructions

### Task 1: Open the sample lab in the Lab Viewer

In this task, you locate the sample files and open this lab folder in the HTML Lab Viewer.

1. Open this repository in your editor.

2. Locate this folder: `labs/lab-01-sample-lab-viewer-format/`.

3. Confirm the folder contains `lab.md` and an `images/` directory kept together.

4. Open the Lab Viewer at [https://labv.roitraining.com/](https://labv.roitraining.com/).

5. Paste the GitHub URL to **this lab folder** (not a deep link to a single file unless you are debugging).

6. Confirm the table of contents lists Time Required, Overview, Lab Instructions, and Congratulations.

> [!NOTE]
> Point the viewer at the lab folder. The preferred manual filename inside the folder is `lab.md`.

### Task 2: Review the image reference pattern

In this task, you see how screenshots are linked for the viewer.

1. Notice that screenshot paths are relative to `lab.md`:

```markdown
![Sample diagram placeholder](images/sample-note.png)
```

2. Keep real UI captures under `images/` with descriptive filenames when authoring production labs.

3. Always include meaningful alt text.

> [!IMPORTANT]
> Do not leave a broken image link. If the screenshot is not ready yet, keep the Markdown image reference and add a `<!-- TODO IMAGE: … -->` comment describing what to capture.

<!-- TODO IMAGE: Optional small diagram illustrating lab folder layout -->
![Lab folder layout](images/sample-note.png)

### Task 3: Sketch the outline for your next lab

In this task, you map a real topic onto the required section order.

1. Pick a short lab topic from your course (about 30 minutes).

2. Write a Title Case `#` title and a `## Time Required` line (`30 minutes` unless you agree on a different duration).

3. Draft `## Overview` with a short *In this lab, you will…* narrative and a `### You learn how to:` list (one verb-led bullet per main task).

4. List `### Task 1: …` through `### Task N: …` under `## Lab Instructions`, putting setup steps in Task 1.

5. Add a preferred `### Bonus Task N: …` unless a bonus truly does not fit.

6. Plan where callouts help: use NOTE for expected results, IMPORTANT for must-follow constraints, and WARNING for easy mistakes.

> [!WARNING]
> Do not invent credentials, project IDs, or secrets in lab steps. Use placeholders such as `YOUR_PROJECT_ID`.

### Bonus Task 4: Tighten the outline without new hand-holding

Using fewer step-by-step hints, improve the outline you sketched in Task 3.

1. Rewrite each “You learn how to” bullet so it starts with a strong verb and ends with a period.

2. Check that Congratulations can mirror those bullets in past tense.

3. Optional: add a one-paragraph `## Scenario` that states the business problem in plain language.

4. Add at least one NOTE, IMPORTANT, or WARNING callout where it would genuinely help a learner.

## Congratulations!

In this lab, you have:
- Previewed a lab folder in the HTML Lab Viewer.
- Referenced images from an `images/` folder beside `lab.md`.
- Recognized the required lab section order and when to use NOTE, IMPORTANT, and WARNING callouts.
