---
name: mrm-governance
description: Generates grounded Model Risk Management (MRM) Model Cards and HTML Governance Portals from Python credit monitoring modules and pytest logs.
---

# MRM Governance Skill

When asked to generate a Model Card or MRM Governance Portal:
1. Read `./model-card-template.md` in this skill folder and use its exact section structure to write `MODEL_CARD.md`.
2. Populate technical fields strictly from the attached Python modules, test files, and `pytest_run.txt` log.
3. Never invent validation metrics or mark a model as Approved; keep all Section 4 sign-off fields set to `TODO`.