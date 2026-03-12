# Copilot Instructions for Lab 4 Word Game

You are assisting in a Python terminal game project for EPITA AI4SE Lab 4.

## Project Context
- Main file: `main.py`
- Tests: `test_update_game_state.py`
- Notes source for prior suggestions: `# My Original Thinking/MY_NOTES.md`
- Keep core logic easy to test, especially `update_game_state`.

## Mandatory Constraints
- Do not introduce `for` or `while` loops in game flow logic.
- Prefer recursion where iterative game flow is needed.
- Do not use string replacement methods such as `.replace()` for masking.
- Keep logic and UI/output separated.
- Keep `update_game_state` pure: no hidden state, no global mutation.

## Suggested State Model
Use a small and explicit state model when relevant:
- `IDLE` -> `SETUP` -> `IN_PROGRESS`
- Temporary feedback states allowed: `CORRECT_GUESS`, `WRONG_GUESS`, `REPEATED_GUESS`
- Terminal states: `WON`, `LOST`
- Optional states: `PAUSED`, `QUIT`

## Suggested Tracked Data
Track and keep consistent:
- `secret_word`, optionally `normalized_secret_word`
- `guessed_letters` (unique guesses)
- `lives` or `attempts_used` plus `max_attempts`
- Last guess and last guess result (`correct`, `wrong`, `repeated`, `invalid`)
- Status/feedback message for CLI output

## Input and Rule Requirements
- Accept exactly one alphabetic character as a valid guess.
- Normalize case consistently for matching.
- Repeated guesses must not consume lives.
- Correct guesses should reveal all matching positions.
- Stop accepting guesses after win/loss is reached.

## Invariants to Preserve
- Lives/attempt counters remain within valid bounds.
- Guessed-letter collections remain internally consistent.
- Displayed masked word always matches secret word length.
- Win state implies full reveal; loss state implies no lives remaining.

## Common Bug Traps to Avoid
- Counting repeated guesses as wrong attempts.
- Revealing only first letter occurrence on correct guess.
- Off-by-one loss checks around last life.
- Case-sensitivity mismatches (`A` vs `a`).
- Accepting invalid input (empty, digit, symbol, multi-char).
- State not reset correctly on restart.

## Testing and Validation
- When behavior changes, run:
  - `python -m unittest test_update_game_state.py -v`
- Add or update tests when changing rules or validation behavior.
- Focus edge cases: repeated guesses, uppercase input, repeated letters, and last-attempt outcomes.
- If game rules change, update README and tests together.

## Coding Style and Change Discipline
- Keep code simple and readable.
- Preserve existing function names unless asked to refactor.
- Add type hints for new or updated functions.
- Avoid unnecessary dependencies.
- Make minimal, targeted edits; do not rewrite unrelated code.
- If uncertain about a rule change, ask before implementing.
