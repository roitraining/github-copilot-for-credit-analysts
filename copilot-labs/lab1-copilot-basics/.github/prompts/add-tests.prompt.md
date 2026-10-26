# Prompt File: .github/prompts/add-tests.prompt.md

Create or update a pytest test file in tests/ for the specified Python file:
1. Build synthetic test inputs only (never use real customer data).
2. Write unit tests for every function in the target file.
3. Explicitly test:
   - Normal inputs across Prime, Near-Prime, and Subprime accounts
   - An empty DataFrame or zero active accounts (asserting np.nan rather than ZeroDivisionError)
   - Exclusion of rows where status == 'charged_off'
   - Exclusion or flagging of rows where delinquency_days = 9999
4. Do not modify the production source file.