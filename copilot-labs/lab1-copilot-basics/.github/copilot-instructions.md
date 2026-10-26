# Credit Analytics Team Copilot Instructions

## Coding Standards
- Use Python 3, pandas, numpy, and pytest for all analytical code.
- Include type hints and a concise docstring on every function.

## Data and Domain Guardrails
- Never generate or request real customer PII, names, or Social Security numbers.
- Exclude rows where status == 'charged_off' from all delinquency rate denominators.
- Treat delinquency_days > 365 (such as 9999) as a data error flag, not a valid delinquency observation.

## Verification Rules
- When generating tests, always include cases for an empty DataFrame, missing utilization values, and delinquency_days = 9999.
- State assumptions before modifying multiple files.
