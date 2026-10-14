<!-- course-title: GitHub Copilot for Credit Analytics and Risk Modeling -->
<!-- course-theme: roi-alt-theme -->

<!-- layout: title -->
![ROI Logo](images/roi-logo-with-name.png)

GitHub Copilot for Credit Analytics and Risk Modeling

# Chapter 1: Copilot Fundamentals and Secure Context-Setting
---
# Chapter 1: Objectives

- Choose where the work belongs: VS Code, the website, or the Copilot app
- Keep live customer data out of prompts
- Select inline, Chat, or Agent, and constrain the prompt with scope, checks, and a stop
- Attach the smallest context that can succeed
- Store team defaults in `.github/copilot-instructions.md` and shared prompt files
---
<!-- layout: navigation -->
# Chapter 1

- **Where Copilot Runs**
- Prompting in VS Code
- Context, Instructions, and Reuse
---
<!-- layout: 3-column -->
# Where the Work Belongs

### VS Code
- Inline completions, Chat, and Agent mode
- Diffs, tests, and file-scoped edits
- This is where production changes land

### Web
- [github.com/copilot](https://github.com/copilot) for a quick question
- Useful before you open the repo
- Not a place to merge code

### Apps
- Desktop and mobile for a draft thought
- No test run, no diff, no approval
- Paste the idea into VS Code before you trust it

<!-- below-columns -->

> [!NOTE]
> GitHub’s policy docs call these places surfaces.
---
# Demo: Using the Copilot Website

1. Open [github.com/copilot](https://github.com/copilot).
2. Paste the following prompt, and read the results. 

```text
What is the difference between Copilot Chat and inline suggestions in VS Code?
```

3. At the bottom of the chat, open the model menu and choose a different model.

4. Paste this prompt:

```text
I have a CSV of credit accounts with balance, utilization, and delinquency_days. Which summary statistics should I compute first, and what would a bad value look like?
```

> [!NOTE]
> Compare the two answers. The second one should name count, missing values, min, max, and mean, and it should flag a blank utilization or a delinquency_days of 9999.
---
<!-- layout: title-image -->
# GitHub Copilot Website

![GitHub Copilot website](images/ch01-github-copilot-website.jpg)
---
# Demo: Using Copilot in Visual Studio

1. Open Visual Studio Code. Choose File, then Open Folder, and open an empty folder. Just create an empty folder anywhere on your computer. 
2. Open Copilot Chat from the Copilot icon in the title bar.
3. Paste the prompt below and press Enter. If asked, allow CoPilot to create the files requested in the prompt. 

```text
Create two files in this folder.

sample_accounts.csv
- Columns: account_id, balance, utilization, delinquency_days
- 12 realistic credit-card rows
- Leave utilization blank on 2 rows
- Set one delinquency_days value to 9999

stats.html
- One page I can open in a browser. No server and no install.
- An Upload CSV button
- After upload, show the row count
- For every column, show how many values are missing
- For every numeric column, show min, max, and mean
- Make the results a clear table
```

4. In the Explorer pane on the left, right-click `stats.html`, choose Reveal in Finder or Reveal in File Explorer, and open the file in a browser.

5. Click Upload CSV and choose `sample_accounts.csv` from the same folder.
---
<!-- layout: title-image -->
# Visual Studio with Copilot

![Visual Studio Code with Copilot Chat and the generated stats page](images/ch01-visual-studio-with-copilot.jpg)
---
# Prevent Data Leakage in Prompts

- A prompt leaves your computer. Copilot sends it to the model and stores it with the chat.
- Do not paste names, account IDs, Social Security numbers, or real customer rows.
- Do paste column names, a few rows you invented, and the cutoff as a parameter.
- If you would not email it outside the company, do not paste it into Copilot.

![Personal records stay out of the prompt. A made-up sample may go in.](images/ch01-prompt-data-leakage.jpg)
---
<!-- layout: 2-column -->
# Risky Ask vs Safe Ask

### Risky
- “Here are our customers’ names, account numbers, and Social Security numbers. Find who is behind on payments.”
- “This spreadsheet is a real export from our system. Tell me which accounts to close.”
- “Use last month’s customer list and decide who we should turn down.”

### Safe
- “Here are the column names and 10 rows I made up. Draft code that scores accounts.”
- “Keep the cutoff as a number I can change.”
- “List what you assumed. Do not invent columns.”
---
# Do Now: Inline Completion

1. In VS Code, create a file named `fizz-buzz.js`.
2. Type this line, add a space after the parenthesis, and pause.

```javascript
function fizzBuzz()
```

3. Wait for the gray ghost text.
4. Press Tab to accept it.
5. Read the inserted code. Undo it if it is not the loop you wanted.

> [!NOTE]
> Ghost text requires Copilot completions. If nothing appears, check the Copilot icon in the status bar.
---
# Accepting an Inline Suggestion

- Read the gray text before you press a key.
- Press Tab only when you understand it and it is what you meant to write.
- Press Esc when it is wrong, or when you do not understand it.
- If only the start is right, accept that part and leave the rest. On a Mac, press Command+Right. On Windows, press Ctrl+Right.
---
<!-- layout: navigation -->
# Chapter 1

- Where Copilot Runs
- **Prompting in VS Code**
- Context, Instructions, and Reuse
---
<!-- layout: title-image -->
# Inline, Chat, or Agent

![Inline versus Chat versus Agent](images/ch01-vscode-surfaces.svg)
---
<!-- layout: card-layout -->
# Three Slash Commands Worth Memorizing

### /explain
- Select a function and ask what it assumes, including how it treats blank values.

### /tests
- Name the cases, including an empty input, a missing column, and which accounts count.

### /fix
- Paste the error and ask for a change only to the lines that failed.
---
# What You Check After Each Command

| Command | A good reply | Send it back when |
| :--- | :--- | :--- |
| `/explain` | States assumptions and how blanks are treated | It only repeats the code |
| `/tests` | Covers the cases you named | It only tests the normal case |
| `/fix` | Changes the lines that failed | It rewrites functions that already worked |
---
<!-- layout: 2-column -->
# Weak Prompt vs Strong Prompt

### Weak
- “Analyze this data.”
- “Make a chart.”
- “Fix the bug.”

### Strong
- “Read scores.csv. Each row is one student. Print the average of the score column, and skip blank scores.”
- “Bar chart of cups sold by weekday. Weekday on the x-axis, cups on the y-axis.”
- “average() crashes on an empty list. Return None for an empty list, and do not change any other function.”
---
# File-Scoped Prompt You Will Reuse

```text
Task: Add a delinquency trend helper.
Use:
- #file src/analytics/delinquency.py
- #file tests/test_delinquency.py
Output:
- Edit only those two files.
- Add tests for an empty frame and a missing risk_band.
Stop:
- If you are not sure what one row represents, list assumptions and do not edit.
```
---
<!-- layout: 3-column -->
# When Another Prompt Will Not Help

### You left out a rule
- Copilot chose which accounts count, because you did not say.
- Write that rule, then prompt again.

### It edited the wrong file
- It changed a file you did not name.
- Send the prompt again with the file names.

### It made a business decision
- It recommended a cutoff or who to decline.
- That choice stays with you.
---
# Demo: Explain, Tests, and Fix

1. In VS Code, create a file named `average.py`. Then, paste this code and save the file.

```python
def average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

print(average([]))
```

2. Select the `average` function. Then, open Copilot Chat and paste the following prompt.

```text
/explain What does this function assume, and what happens when the list is empty?
```

3. Read the reply before you continue, and then paste this prompt.

```text
/tests Include a normal list and an empty list.
```

4. Read the tests. Confirm the empty list is one of the cases.
5. Open the terminal in the folder that contains the file, and run this command.

```bash
python average.py
```

6. Copy the error. Paste this prompt, and replace the second line with the error you copied.

```text
/fix
PASTE THE ERROR HERE
Change only the lines that failed. An empty list should return None.
```

7. Read the edit. Keep it only if an empty list returns None.

> [!NOTE]
> If `python` is not found, run `python3 average.py`. If a reply ignores the function, select `average` and send the prompt again.
---
<!-- layout: navigation -->
# Chapter 1

- Where Copilot Runs
- Prompting in VS Code
- **Context, Instructions, and Reuse**
---
<!-- layout: title-image -->
# Start with the Smallest Context

![Context selectors from selection to workspace](images/ch01-context-selectors.svg)
---
# How You Point Copilot at Code

- Select the function. Chat uses that selection.
- Type `#file` and choose the file. Add the test file when you want tests.
- Type `@workspace` only when the change needs other files.
- `@workspace` can change files you did not name. Name the files when you can.
---
<!-- layout: 2-column -->
# What copilot-instructions.md Is For

### The file
- It lives at `.github/copilot-instructions.md`
- Copilot adds it to every chat in that repo
- You do not paste it into the prompt
- It holds rules for the whole team, not today’s task

### Rules that belong there
- Write tests with the change
- Do not use real customer data in examples
- State assumptions before editing
- Leave out one-off questions, secrets, and live data
---
<!-- layout: 2-column -->
# Instructions vs a Prompt File

### `.github/copilot-instructions.md`
- Loaded on every chat in the repo
- Standing rules for the team
- You do not choose it each time

### `.github/prompts/name.prompt.md`
- One job you repeat, such as “add tests for this function”
- You run it by typing `/` and the file name
- It does not run until you ask for it
---
# Chapter 1 Hands-On Lab

- Lab: Effective Prompting and Context Engineering
- Time: 30 minutes
---
# What You Learned

- Chose where the work belongs: VS Code, the website, or the Copilot app
- Kept live customer data out of prompts
- Selected inline, Chat, or Agent, and constrained the prompt with scope, checks, and a stop
- Attached the smallest context that can succeed
- Stored team defaults in `.github/copilot-instructions.md` and shared prompt files
---
# Quiz 1 of 3

**You need Copilot to change one function in VS Code. What context should you give it?**

- A. `@workspace`, so it can see the whole repo
- B. The selected function, or `#file` on that file and its test
- C. Every file in the repo, pasted into the chat
- D. The website, with the repo described from memory
---
# Quiz 1: Answer

**You need Copilot to change one function in VS Code. What context should you give it?**

**Correct: B.** Start with the selection or the named files.

- Select the function when the change stays in that block
- Add the test file with `#file` when you want tests
- Use `@workspace` only when the change needs other files
- `@workspace` can change files you did not name
---
# Quiz 2 of 3

**The team wants the same rules on every chat, without pasting them each time. Where do the rules go?**

- A. In a prompt file that someone runs with `/`
- B. In `.github/copilot-instructions.md`
- C. In the ghost text, so Tab inserts the rules
- D. In one chat. Later chats will remember it
---
# Quiz 2: Answer

**The team wants the same rules on every chat, without pasting them each time. Where do the rules go?**

**Correct: B.** Copilot adds `copilot-instructions.md` to every chat in that repo.

- A prompt file is one job you repeat. It does not run until you ask
- Ghost text is an inline suggestion, not a store for team rules
- One chat does not set the default for the next chat
- Keep the file to standing rules, such as tests and no live customer data
---
<!-- layout: 2-column -->
# Quiz 3 of 3: Discussion

### Prompt
A teammate runs `/fix` on a function that crashes. They keep the edit without reading it. Copilot also rewrote a function that already worked.

### Discuss
- What should they have included with `/fix`?
- What should they check before keeping the edit?
- Which command comes first if they do not yet understand the function?
---
<!-- layout: 2-column -->
# Quiz 3: Discussion Points

**A teammate runs `/fix` on a function that crashes. They keep the edit without reading it. Copilot also rewrote a function that already worked.**

### Strong Answers Mention
- The error, and a limit to the lines that failed
- Keep the edit only if the crash is fixed and the other function is unchanged
- `/explain` first, when they cannot say what the function does
- `/tests` for the failing case, such as an empty list

### Watch For
- Keeping the edit because it looks finished
- Using `/fix` to rewrite the whole file
- Skipping `/explain` when the function is unclear
---
<!-- layout: stacked -->
# Questions and Answers


![Questions and Answers](images/qa.png)
