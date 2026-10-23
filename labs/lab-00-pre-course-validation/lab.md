# Pre-Course Environment and GitHub Copilot Validation

## Time Required

15 minutes

## Overview

In this lab, you confirm that Python, Visual Studio Code, GitHub Copilot, and a browser are ready for the course labs.

### You will verify the following prerequisites:
- Python 3.10 or newer is installed and available in the terminal.
- Visual Studio Code is installed and Copilot Chat responds.
- A virtual environment can be created to run a Python script.

## Lab Instructions

### Task 1: Verify Python is installed

1. Open the **Terminal** app on macOS, or **PowerShell** on Windows.

2. Run the command for your operating system:

**macOS / Linux:**

```bash
python3 --version
```

**Windows (PowerShell):**

```powershell
python --version
```

3. Continue to Task 2 if the output is `Python 3.10` or newer.

4. If the command is not recognized, or the version is older than 3.10, download and install Python 3.10 or newer from [https://www.python.org/downloads/](https://www.python.org/downloads/). On Windows, check **Add python.exe to PATH** in the installer.

5. Close the terminal, open a new one, and run the version command again. Continue only after it prints `Python 3.10` or newer.

### Task 2: Confirm Visual Studio Code is installed and Copilot Chat responds

1. Create a new empty folder named `lab0-setup-check` on your Desktop or in your Documents folder.

2. Open **Visual Studio Code**.

3. In the top menu bar, click **File** > **Open Folder** (or **File** > **Open...** on macOS), select your new `lab0-setup-check` folder, and click **Open** (or **Select Folder** on Windows).

4. If Visual Studio Code displays a dialog asking **Do you trust the authors of the files in this folder?**, click **Yes, I trust the authors**.

5. Open the **Copilot Chat** panel by clicking the **Copilot icon** near the top center of the VS Code title bar (next to the search bar), or press CTRL+ALT+I on Windows / CTRL+CMD+I on macOS.

6. Look at the bottom of the Copilot Chat input box and confirm that `</> Agent` is selected.

![Copilot Chat input controls in VS Code](images/copilot-chat-box.png)

> [!IMPORTANT]
> If you see a **Sign in to use Copilot** button instead of the chat box, click it and sign in with the GitHub account that has your active GitHub Copilot license. If the Copilot icon is missing altogether, open the **Extensions** view (CTRL+SHIFT+X on Windows or CMD+SHIFT+X on macOS), search for `GitHub Copilot`, and click **Install**.

7. Paste the following prompt into the Copilot Chat input box and press ENTER:

```text
Reply with "GitHub Copilot is connected and ready!" and tell me in one sentence how you can help a credit analyst.
```

8. Confirm that Copilot replies in the chat panel with the confirmation message.

### Task 3: Create a Python virtual environment and run a setup check script

1. In the Copilot Chat input box (`</> Agent` mode), paste the following prompt and press ENTER:

```text
Create a file named check_env.py in this folder that:
1. Prints the running Python version.
2. Imports pandas, numpy, matplotlib, seaborn, sklearn, and pytest, and prints each package's version.
3. Creates a 3-row pandas DataFrame of synthetic credit accounts with columns account_id and balance, prints the mean balance, and prints "SUCCESS: Python environment is ready for the course labs!"
```

2. If Copilot asks for permission to create or save `check_env.py`, click **Keep** (or **Accept** / **Allow**). Verify that `check_env.py` now appears in the VS Code **Explorer** pane on the left.

3. Open the integrated terminal inside VS Code by clicking **Terminal** > **New Terminal**.

4. Copy and paste the command below for your operating system into the VS Code terminal and press ENTER to create a `.venv` virtual environment, install the course packages, and run `check_env.py`:

**macOS / Linux:**

```bash
python3 -m venv --clear .venv && .venv/bin/python -m pip install -q --upgrade pip && .venv/bin/python -m pip install -q pandas numpy matplotlib seaborn scikit-learn pytest ipykernel && .venv/bin/python check_env.py
```

**Windows (PowerShell):**

```powershell
python -m venv --clear .venv; .\.venv\Scripts\python -m pip install -q --upgrade pip; .\.venv\Scripts\python -m pip install -q pandas numpy matplotlib seaborn scikit-learn pytest ipykernel; .\.venv\Scripts\python check_env.py
```

5. Wait 30 to 60 seconds while the packages download and install. Confirm that the terminal output lists the package versions, prints the mean balance, and ends with:

```text
SUCCESS: Python environment is ready for the course labs!
```

> [!WARNING]
> If the terminal reports that `python3` or `python` is not found, return to Task 1. Quit Visual Studio Code, confirm the version command in a new system terminal, then reopen VS Code and run Step 4 again.

### Task 4: Generate a “Hello World” web page with Copilot and open it in your browser

1. In the Copilot Chat input box (`</> Agent` mode), paste the following prompt and press ENTER:

```text
Create a single-file web page named hello.html in this folder (no external servers or libraries needed) that displays:
1. A clean card with the heading "Hello World - Ready for Credit Analytics!"
2. A green status badge that says "VS Code + GitHub Copilot + Browser Verified"
3. A button labeled "Run Quick Check" that displays today's date and time on the page when clicked.
```

2. Click **Keep** (or **Accept**) in the chat panel or editor if prompted so `hello.html` is saved in your `lab0-setup-check` folder.

3. In the VS Code **Explorer** pane on the left, right-click `hello.html` and choose **Reveal in Finder** (macOS) or **Reveal in File Explorer** (Windows).

4. In the Finder or File Explorer window that opens, double-click `hello.html` to open it in your default web browser.

5. Click the **Run Quick Check** button on the page and confirm that today’s date and time appear.

### Bonus Task 5: Test inline ghost text (`Tab`) and `pytest`

If you have two extra minutes, test inline ghost-text completions in the editor and confirm `pytest` runs cleanly from your virtual environment.

1. In the VS Code Explorer pane, create a new file named `test_setup.py` and paste the following two lines:

```python
def add_balances(bal_a: float, bal_b: float) -> float:
    # Return the sum of bal_a and bal_b rounded to 2 decimal places
```

2. Place your cursor at the end of line 2, press ENTER, wait a moment for Copilot’s gray inline ghost text to appear, and press `Tab` to accept the code suggestion.

3. Add a simple `pytest` unit test at the bottom of `test_setup.py` and save the file (CMD+S on macOS or CTRL+S on Windows):

```python
def test_add_balances():
    assert add_balances(1200.50, 300.25) == 1500.75
```

4. Run `pytest` in the VS Code terminal to confirm your test runner works:

**macOS / Linux:**

```bash
.venv/bin/python -m pytest -v
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\python -m pytest -v
```

> [!NOTE]
> Once you see `1 passed` in green, your machine is 100% ready for the course! You can safely delete the temporary `lab0-setup-check` folder whenever you like.

## Congratulations!

In this lab, you have verified:
- Python 3.10 or newer is installed and available in the terminal.
- Visual Studio Code is installed and Copilot Chat responds.
- A virtual environment installs the course packages and runs a Python script.
- A Copilot-generated HTML page opens in the browser.
