# Prompt File: .github/prompts/mrm-evidence.prompt.md

Using the specified source files, test file, and pytest run log, generate `AUDIT_EVIDENCE.md`:
- **Scope of Refactoring**: Functions modularized and vectorized.
- **Defensive Assertions Inventory**: Table of every `ValueError` guard in the codebase.
- **Pytest Verification Log**: Table of every unit test and the exact pass count from the pytest output log.
- **Reviewer Sign-Off Checklist**: Leave human reviewer name, date, and decision as `TODO`.

Rule: Cite only facts and test results present in the specified files. Do not invent metrics or mark the package as "Approved."