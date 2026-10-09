<!-- course-title: Introducing the ROI Course Factory -->
<!-- course-theme: roi-alt-theme -->

<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

# Introducing the ROI Course Factory

## Author, edit, and present from one Markdown workflow
---
<!-- layout: full-bleed -->
# The ROI COurse Factory Illustrated

![ROI Course Factory](images/infographic.png)
---
<!-- layout: panel-right -->
# Welcome!

- ROI leads the industry in designing and delivering customized technology and management training solutions
- Meet your instructor
  - Name
  - Background
  - Contact info
- Let’s get started!

![Welcome](images/welcome.png)
---
# Course Objectives

- Teach a class from Markdown you can preview, revise, and hand to the next instructor
- Use the viewer, the editor, the skills, and the authoring template as one workflow
---
<!-- layout: panel-left -->
# Agenda

- Chapter 1: How the Factory Works
- Lab 1: Creating a Course

![Agenda](images/agenda.png)
---
<!-- layout: panel-right -->
# Who Should Attend

- Course authors who will brief an agent and review the deck
- Instructors who will present from the slides viewer
- Editing staff who will correct slides, images, and layouts

![Who Should Attend](images/who-should-attend.png)
---
<!-- layout: panel-left -->
# Prerequisites

- Comfortable cloning a Git repository and opening it in an editor
- A current browser. Chrome or Edge when you will use the editor
- A coding agent: Cursor, Claude Code, Visual Studio Code with CoPilot, or Antigravity
- No prior experience with this viewer, this editor, or these skills

![Prerequisites](images/prerequisites.png)
---
<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

Introducing the ROI Course Factory

# Chapter 1: How the Factory Works
---
# Chapter 1: Objectives

- Introduce the viewers, the editor, the skills, and the template, and say what each one is for
- Open a course locally or from GitHub and present it with the drawer, annotations, themes, and type size
- Edit slides on a local clone: change layouts, images, and Markdown, then save
- Start a new course from the template with a clear brief and an outline you approve
---
<!-- layout: navigation -->
# Chapter 1

- **Introduction**
- Using the Viewer
- Creating a Course
- Using the Editor
---
# One Factory, Two Lines

- **Two assembly lines** build every class: a slides line and a labs line
- **Authors** define the course, audience, length, and an outline
- **Agents** draft from the matching skill
- **Editors** finish layout, images, and wording
- **Instructors** present the slides and send students into the labs

> [!NOTE]
> The lines run side by side and ship together. The room sees one class, with a deck and a lab manual.
---
<!-- layout: full-bleed -->
# Factory Lines Diagram

![Two assembly lines, slides and labs, finishing as one course](images/factory-lines-diagram.svg)
---
<!-- layout: card-layout -->
# Four Main Components of the Factory

### Viewers
- The Slides Viewer is used by the instructor to present. 
- The Lab Viewer is used by students to do the labs. 
- The viewers are read-only and designed for the classroom

### Editor
- Editing staff use this to change a slide on a local clone.
- Saves changes to the Markdown file in that folder.

### Agent Skills
- Course Generator and Lab Generator are the rules the agent follows.
- They keep decks and labs in the ROI shape without you restating it.

### Template
- This is the GitHub repo you clone to start a course.
- It holds the folder layout, the stock images, and the skills.
---
<!-- layout: 2-column -->
# What Is the Course, and What is the Viewer

### The Course is markdown and images
- Slide text, layout comments, and images
- Chapter files and the course title in the footer
- This is what you commit and what the next person opens

### The Viewers control the look
- Theme, light or dark, and type size
- Pen, highlighter, pointer, and flipchart
- Handy while you teach, gone for the next instructor

<!-- below-columns -->

> [!IMPORTANT]
> If it is not in the Markdown, it is not part of the course.
---
<!-- layout: card-layout -->
# Who Does What

### Authors
- Brief the agent, approve the outline, and reject a draft that misses the audience
- Tell the agent to generate the course, and make changes

### Editing staff
Clone the repo and use the editor for layouts, images, and wording

Editing staff can also use the agent if they wish

### Instructors
Open the viewer and teach. They mark up the slide. They do not rewrite the file
### Everyone

Preview before the class. Can generate PDFs for students from the viewer
---
<!-- layout: card-layout -->
# Advantages of Using The ROI Course Factory

### Faster Course Development
- An initial course plus labs can be created in minutes.
- Testing and editing is aided by the agent. 

### Simpler Custom Course Creation
- Rewrite an existing course for a new audience with a single prompt.
- The agant can be pointed at multiple courses and asked to combine them. 

### Easier Editing
- The editor is designed for simple edits to content and images. 
- The agent can handle mass edits on request. 

### Flexible Styling
- Multiple page layouts
- Can skin content by simply. selecting themes. 
- Custom themes can be added.
---
<!-- layout: title-image -->
# Comparing Manual versus Factory Course Creation

![Timelines for manual and factory course creation](images/manual-vs-factory-timeline.svg)
---
<!-- layout: navigation -->
# Chapter 1

- Introduction
- **Using the Viewer**
- Creating a Course
- Using the Editor
---
# Open the Viewer

- **Start here:** [slidesv.roitraining.com](https://slidesv.roitraining.com/)
- The first load is a sample course, so you can click around before you bring your own
- The folder icon (or Command+O on a Mac, Ctrl+O on Windows) opens a course
- Nothing you do in this window writes back to GitHub

> [!TIP]
> Bookmark the viewer. You do not install it, and you do not put the viewer source in the course repo.
---
# How the Viewers Work

- The slides viewer opens the folder named in the __`course`__ parameter
   - This link opens this course:

[https://slidesv.roitraining.com/?course=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/course](https://slidesv.roitraining.com/?course=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/course)

- The lab viewer opens the folder named in the __`lab`__ parameter
   - This link opens the lab in this course:

[https://labv.roitraining.com/?lab=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/labs/lab-01-create-a-short-web-course](https://labv.roitraining.com/?lab=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/labs/lab-01-create-a-short-web-course)
---
<!-- layout: stacked -->
# Open a Course from Your Machine

- Choose **Local**, then **Choose Folder**
- Point to the folder that holds the chapter Markdown files and `images/`
- Several Markdown files in that folder become chapters in the chapter menu
- This is read-only. Closing the tab does not change the files

![Open Course dialog on the Local tab](images/viewer-open-local.png)
---
<!-- layout: stacked -->
# Open a Course from GitHub

- Choose **GitHub** and paste a repo, a folder, or a single Markdown file URL
- A folder URL is the usual choice: the viewer lists each chapter file
- **Open** loads it. **Copy share link** gives you a URL that reopens this course
- Recent GitHub courses stay on this browser so you can jump back

![Open Course dialog on the GitHub tab](images/viewer-open-github.png)
---
# What the Viewer Expects in the Folder

- Chapter files named like `00-introduction.md` and `01-how-the-factory-works.md`
- The same `course-title` comment at the top of every chapter, so the footer matches
- An `images/` folder beside those files, with relative links such as `images/welcome.png`
- Slides separated by a line that contains only `---`

> [!IMPORTANT]
> Open the course folder, not a random parent directory full of unrelated Markdown. The viewer treats the Markdown it finds there as the course.
---
<!-- layout: default -->
# The Viewer Toolbar 

- **Folder** opens a course. 
- **Printer** builds a 16:9 handout
- **Fullscreen** hides this bar
- **Theme** restyles the slides
- **Moon** switches light and dark. 
- **Minus and plus** change type size

![Viewer toolbar over a content slide](images/viewer-toolbar.png)
---
<!-- layout: default -->
# The Annotation Controls 

- **Pen**
- **Highlighter** 
- **Flipchart** opens a blank canvas
- **Broom** erases the current slide
- **Trash can** erases all slides 

![Viewer toolbar over a content slide](images/annotation-controls.png)
---
<!-- layout: card-layout -->
# Four Ways to Point at the Slide

### Pen
- Draw a line the room can see. Press P.
- Choose a color before you draw, or you will get the last one.

### Highlighter
- Lay a translucent stroke over a phrase. Press H.
- Yellow, green, or blue. It does not cover the words completely.

### Pointer
- Drop one pointer on the spot you mean. Press O.
- A second click moves it. You do not get a trail of pointers.

### Flipchart
- Open a blank sheet over the slide and sketch.
- Close the sheet to come back to the slide. The slide is still there.
---
# The Slide Drawer

- The hamburger opens **Course Slides**: every slide title, in order
- Click a row to jump. The current slide is highlighted
- **Pin** keeps the list open while you teach. Close it when you want the stage back
- Use this when someone asks you to return to an earlier picture

![Slide drawer in list view](images/viewer-drawer-list.png)
---
# The Thumbnail Tray

- The grid icon in the drawer header switches from titles to thumbnails
- Scan the tray when you need the picture, not the title
- The list is faster when you already know the slide name
- Either view jumps to that slide. Neither one edits it

![Slide drawer in thumbnail view](images/viewer-drawer-thumbnails.png)
---
<!-- layout: title-image -->
# Fullscreen

![Fullscreen hides the toolbar and keeps the annotation dock](images/viewer-fullscreen.png)
---
# Present Without the Mouse

- **Right arrow** or **Space** advances. **Left arrow** goes back. **Home** and **End** jump to the ends
- **F** toggles fullscreen. The toolbar hides. The annotation dock stays
- **P** pen, **H** highlighter, **O** pointer, **C** clear this slide
- Print from the printer icon: 16:9, margins none, background graphics on

> [!TIP]
> Fullscreen is for the room. Leave it when you need the chapter menu, the theme, or a different course.
---
# Themes Change the Look, Not the Words

- The theme menu restyles type, color, and the title slide
- **ROI Theme** is the default classroom look. **ROI Alt Theme** is the darker, site-like look
- **Demo**, **Demo 2**, and **Holcim** are other skins for the same Markdown
- Switching themes does not edit the file, and it does not travel with a share link as content

![The same slide in the ROI Alt theme](images/viewer-theme-alt.png)
---
# Change the Font Size so Everyone Can See

- Minus and plus shrink or enlarge the slide text
- Use it when the back row cannot read a code sample, or when a slide is cramped
- The viewer remembers the size in this browser
- It does not change the Markdown, and a colleague’s browser starts at the normal size

![The same slide after increasing the type size](images/viewer-font-size.png)
---
# Do Now: Using the Viewer

1. Open the [Slides Viewer](https://slidesv.roitraining.com/).
2. Use the arrow keys to move through a few slides of the sample course.
3. Try a couple of themes, then keep the one you like.
4. Switch to full screen.
5. Try the pen, the highlighter, and the pointer.
6. Open the flipchart and sketch on it.
7. Close the flipchart, then press Escape to leave full screen.
8. Click the print icon and save the PDF on your machine.
---
<!-- layout: navigation -->
# Chapter 1

- Introduction
- Using the Viewer
- **Creating a Course**
- Using the Editor
---
# Start from the Template, Not a Blank File

- Copy the contents of the ROI Course Authoring Template when creating a new course
- This template includes the agent Skills, a Sample course, and `course` and `labs` folders
- The template is not the viewer. You do not need the viewer source in the course repo
- The command below, clones the repo into a new folder

```bash
git clone https://github.com/roitraining/roi-course-authoring-template.git web-development-course
```
---
<!-- layout: 2-column -->
# Course Folder and Lab Folder

### course/
- One Markdown file per chapter: `00-introduction.md`, then `01-…`
- Shared `images/` for every chapter, including the stock welcome and agenda art
- This is the folder you open in the slides viewer

### labs/
- One folder per lab: `labs/lab-01-short-name/`
- Inside it: `lab.md` and `images/`
- Open that folder in the lab viewer at labv.roitraining.com

<!-- below-columns -->

> [!IMPORTANT]
> A chapter ends with a lab stub: title and time only. The steps live in `lab.md`. Do not paste the lab URL onto the slide. A person adds that link later.
---
<!-- layout: card-layout -->
# The Skills Are the House Style

### Course Generator
- Builds the intro spine, the chapter order, and the layouts the viewer accepts.
- It will not invent an instructor bio or write the lab steps on a slide.

### Lab Generator
- Builds one lab folder: overview, tasks, a bonus, and a closing.
- Steps are second person. Setup belongs in Task 1.

### What you still decide
- Audience, prerequisites, length, and the story of the course.
- The skill cannot guess who is in the room.

### When the agent drifts
- Tell it to read the Course Generator and Lab Generator skills and follow them.
- The template’s agent files already point at those skills. Say it again if you must.
---
# Any Agent That Can Use Skills

- **Cursor**, **Claude Code**, **Visual Studio Code** with Copilot, and **Antigravity** are the ones we already point at the skills
- The repo carries `.cursorrules`, `CLAUDE.md`, `AGENTS.md`, and Copilot instructions so the agent finds the skills
- Any other coding agent that can read a skill file can do this work
- If it starts inventing layouts, stop it and name the skill. Do not argue with a draft that ignored the rules

> [!TIP]
> You drive every step. A strong agent with a vague prompt still writes the wrong course quickly.
---
<!-- layout: 2-column -->
# A Weak Prompt and a Strong One

### Weak
- “Write a course on web development.”
- No audience, so you get a beginner textbook
- No length, so you get a four-day dump
- No outline, so chapter 1 is a surprise

### Strong
- Title, audience, prerequisites, and hours
- Inlcude an outline if you have one
- Tell the agent to use the Course and/or Lab Generator Skills

<!-- below-columns -->

> [!NOTE]
> Providing a detailed outline will save you time in the long run. The initial generated course will be closer to what you want.
---
# A Prompt You Can Reuse

- Supply details about the course, the audience, the length, and provide an outline. 

```text
Use the Course Generator skill and the Lab Generator skill.
Read both skills and follow them.

Build a complete half-day course and its three labs.
Write every chapter file and every lab.

Course title: Understanding Web Development with HTML, CSS, and JavaScript
Audience: professionals who work with web teams and need to
read, sketch, and lightly change pages. Not a first-week bootcamp.
Prerequisites: files and folders, a text editor, and a current
browser. No prior HTML required.
Length: half a day, about 4 hours, including three short labs.

Follow this outline.

Introduction
- Title, welcome, objectives, agenda, who should attend, prerequisites

Chapter 1: HTML and the Structure of a Page
- Documents and elements
- Text, links, and images
- How a page is organized
Lab: Build a Simple Page (20 minutes)

Chapter 2: CSS and How the Page Looks
- Selectors and the cascade
- The box model and simple layout
- Type, color, and spacing
Lab: Style the Page (20 minutes)

Chapter 3: JavaScript and Behavior in the Browser
- Finding elements on the page
- Responding to events
- Reading and changing what the visitor sees
Lab: Make the Page Respond (20 minutes)

Write these files:
- course/00-introduction.md
- one Markdown file per chapter under course/
- labs/lab-01-build-a-simple-page/lab.md
- labs/lab-02-style-the-page/lab.md
- labs/lab-03-make-the-page-respond/lab.md

Reuse the stock images already in course/images/.
On each chapter, the lab stub is a title and a time only.
```
---
<!-- layout: 3-column -->
# Preview, Then Polish, Then Share

### Preview
- Open the course folder in the viewer
- Teach the draft to yourself, out loud
- Stop on any slide you would not say in class

### Polish
- Fix layout and images in the editor
- Send the agent back when the story is wrong
- Be specific: which slide, what to change

### Share
- Commit and push the folder you meant
- Paste the course folder URL on the GitHub tab
- Copy the share link and send that to the instructor

<!-- below-columns -->

> [!WARNING]
> Do not regenerate `welcome.png`, `agenda.png`, or the other stock images. Copy the files that shipped with the template.
---
# Lab: Create a Short Web Development Course

**Time:** 20 minutes

- [Open Lab](https://labv.roitraining.com/?lab=https://github.com/roitraining/roi-course-authoring-template/tree/main/introducing-the-roi-course-factory/labs/lab-01-create-a-short-web-course)
---
<!-- layout: navigation -->
# Chapter 1

- Introduction
- Using the Viewer
- Creating a Course
- **Using the Editor**
---
# Edit on a Clone on Your Local Machine

- Clone the course repo first. The editor opens that folder on your machine
  - It does not open a GitHub URL, and it does not commit or push
- Use **Chrome or Edge**. Other browsers cannot grant the folder write access it needs
- When you are done, commit and push to GitHub to publish your changes

> [!IMPORTANT]
> The viewer is for presenting. The editor is for changing files. You can't edit a course opened from GitHub in the viewer.
---
# What You See When the Editor Opens

- **Open folder** picks the course directory. **Save** writes the current chapter
- The stage is a live preview of the slide you are on
- The inspector on the right holds the course title, the layout, the image, and the Markdown
- Until a folder is open, those fields stay disabled on purpose

![Slide editor before a course folder is open](images/editor-shell.png)
---
<!-- layout: 3-column -->
# The Inspector Does Three Jobs

### Layout
- The menu sets the layout comment for this slide
- Title, columns, cards, panels, and image layouts are all in that list
- The preview updates before you save

### Image
- **Add image** copies a file into `images/` and places it on this slide
- **Use** places an image that is already in the folder
- Adding a file does not replace one that already has that name

### Markdown
- This is the slide, as text
- Type here when the menus are the wrong tool
- The preview follows each keystroke. Save is what writes the file
---
# Layouts Are a Comment, Then a Shape

- Each slide may start with a layout comment. No comment means the default stack of title and bullets
- A list plus an image, and no layout comment, splits on its own: bullets on the left, picture on the right
- The layout menu writes that comment for you. You can also type it
- A two-column slide starts with the comment `<!-- layout: 2-column -->` on its own line
- The next three slides are the layouts, not pictures of them. This is what the room sees
---
<!-- layout: 2-column -->
# Two Columns: Put a Choice Side by Side

### Viewer
- Open a folder or a GitHub URL
- Present, annotate, and print
- Leave the file alone

### Editor
- Open a local clone
- Change layout, image, and text
- Save, then commit

<!-- below-columns -->

> [!NOTE]
> Two columns start at each `###` heading. Use them for a contrast, not for a second topic.
---
<!-- layout: 3-column -->
# Three Columns: Three Parallel Options

### Default
- Title and bullets, top to bottom
- Add an image and it sits beside the list
- The workhorse slide

### Columns and cards
- Two or three comparisons
- Cards when each idea is a short sentence
- One idea per column

### Picture-led
- Title and image, image only, full bleed, or stacked
- Use these when the picture is the point
- Keep a heading so the drawer still has a name
---
<!-- layout: card-layout -->
# Cards: Four Ideas, No Bullet Noise

### Panels
- A colored third on the left or the right holds an image.
- Title and bullets stay on the light area. Welcome and Agenda use this.

### Stacked
- Bullets on top, picture across the bottom.
- Use it when a side-by-side split would shrink the diagram.

### Image only
- The picture fills the stage. The heading is only for the drawer.
- Full bleed also covers the top bar and the footer.

### Title
- The cover and the chapter divider.
- Logo, course name, and a short subtitle. You rarely edit these mid-class.
---
# Put a Picture on the Slide

- **Add image** copies your file into the course `images/` folder and inserts the Markdown link
- **Use** points this slide at a file that is already in that folder
- If the name is taken, the editor saves a new name. It will not overwrite the old file
- You can also drop a file in `images/` yourself and write the link

```markdown
![Welcome panel](images/welcome.png)
```

> [!TIP]
> Name the file for the slide, not `image1.png`. The alt text is what a colleague sees if the file is missing.
---
<!-- layout: 2-column -->
# Add a New File, or Reuse One

### Add image
- Pick a PNG, JPEG, GIF, WebP, or SVG from disk
- The editor copies it into `images/`
- The current slide now references that copy
- Save the chapter so the Markdown link sticks

### Use
- The menu lists images already in the folder
- Choose one and click **Use**
- No second copy is made
- Stock art such as `welcome.png` is already there. Use it. Do not redraw it
---
# Add, Duplicate, Delete, Save

- Right-click a slide in the list, or right-click the stage: **Add slide**, **Duplicate slide**, **Delete slide**
- A new slide starts as a title and an empty bullet. Duplicate is the fast way to keep a layout
- Delete asks you to confirm. A chapter must keep at least one slide
- **Save** writes this chapter only. The status line says **Unsaved changes** until you do

> [!WARNING]
> Switching chapters, or opening another folder, asks you to save, discard, or cancel. Discard throws away the unsaved Markdown for this chapter. The image file you already added stays on disk.
---
# Do Now: Using the Editor

1. Open the [Slide Editor](https://md-to-html-slides-editor-1077635956541.us-east4.run.app/). Use Chrome or Edge.
2. Click **Open folder** and choose the `course` folder from the lab (`web-development-course/course`).
3. Scroll through the slides the agent wrote.
4. Change the wording on one slide, then click **Save**.
5. Change that slide’s layout, check the preview, and save again.
6. Experiment with making changes to the slides.
---
<!-- layout: 2-column -->
# What You Learned

### You can present
- Named the viewer, the editor, the skills, and the template
- Opened a course locally or from GitHub
- Used the drawer, annotations, themes, and type size

### You can author
- Edited slides on a local clone, then saved
- Changed layouts, images, and Markdown
- Started from the template with a brief and an outline you approved
---
# Quiz 1 of 3

**Where do you change slide Markdown?**

- A. In the viewer, on the GitHub tab, then click Save
- B. In the editor, after you open a local course folder
- C. With the pen tool, which writes the strokes into the file
- D. In the theme menu, which stores a second copy of the deck
---
# Quiz 1: Answer

**Where do you change slide Markdown?**

**Correct: B.** In the editor, after you open a local course folder

- The viewer presents a folder or a GitHub URL. It does not write the course
- The editor saves the chapter file on your machine. You commit from Git
- Pen strokes and the theme stay in this browser
- Chrome or Edge is required because the editor needs folder write access
---
# Quiz 2 of 3

**What should you settle before the agent writes chapter files?**

- A. The PDF margins and the pen color
- B. Audience, prerequisites, length, and an outline you have approved
- C. A custom theme, so the draft matches the classroom
- D. The lab URL, so the stub can link to the manual
---
# Quiz 2: Answer

**What should you settle before the agent writes chapter files?**

**Correct: B.** Audience, prerequisites, length, and an outline you have approved

- Those three facts plus a title change the altitude and the size of the draft
- An approved outline is cheaper to fix than a finished chapter
- Themes and pen color are presentation choices, not authoring inputs
- The lab stub carries a title and a time. A person adds the URL later
---
<!-- layout: 2-column -->
# Quiz 3 of 3: Discussion

### Prompt
An author tells the agent only: “Write a 3-hour web course.” The agent returns one Markdown file that afternoon.

### Discuss
- What is missing from that brief?
- What will you check before anyone teaches from the file?
- What do you send back, in one message?
---
<!-- layout: 2-column -->
# Quiz 3: Discussion Points

**An author tells the agent only: “Write a 3-hour web course.” The agent returns one Markdown file that afternoon.**

### Strong Answers Mention
- No audience and no prerequisites, so the altitude is a guess
- No outline approval, so the story was never reviewed
- A single file skips the chapter pattern a 3-hour course should use
- Send back: skill name, audience, prerequisites, length, and “outline only”

### Watch For
- “The agent knows our style, so a one-line prompt is enough”
- Teaching from the file because it looks long
- Asking for all chapters again before anyone has seen slide one in the viewer
---
<!-- layout: stacked -->
# Questions and Answers

![Questions and Answers](images/qa.png)
