## CoPilot Suggestions

For a Word Game like Hangman, use a small state machine so game flow is clear and testable.

Suggested core states:

- `IDLE`: App loaded, no active game yet.
- `SETUP`: Preparing or selecting the secret word and resetting counters.
- `IN_PROGRESS`: Player can submit guesses.
- `CORRECT_GUESS`: Temporary feedback state after a valid correct guess.
- `WRONG_GUESS`: Temporary feedback state after a valid wrong guess.
- `REPEATED_GUESS`: Temporary feedback state when a letter was already tried.
- `WON`: Terminal state when all letters are revealed.
- `LOST`: Terminal state when max mistakes is reached.
- `PAUSED` (optional): Game is paused.
- `QUIT` / `EXIT` (optional): Session ends intentionally.

Useful transition rules:

- `IDLE -> SETUP -> IN_PROGRESS`
- `IN_PROGRESS -> CORRECT_GUESS -> IN_PROGRESS`
- `IN_PROGRESS -> WRONG_GUESS -> IN_PROGRESS`
- `IN_PROGRESS -> REPEATED_GUESS -> IN_PROGRESS`
- `IN_PROGRESS -> WON`
- `IN_PROGRESS -> LOST`
- `IN_PROGRESS -> PAUSED -> IN_PROGRESS` (if pause is supported)

Useful tracked data with states:

- Secret word (or phrase)
- Revealed letters / masked pattern
- Tried letters
- Remaining attempts
- Current status message

Variables to keep track of (practical list):

- `secret_word` (str): Word to guess.
- `normalized_secret_word` (str): Lowercased/cleaned version for matching.
- `display_word` (str): Current masked view (example: `_ a _ g _ a n`).
- `guessed_letters` (set[str]): Unique letters already tried.
- `correct_letters` (set[str]): Letters found in the word.
- `wrong_letters` (set[str]): Incorrect guesses for display and penalties.
- `attempts_used` (int): Number of wrong attempts so far.
- `max_attempts` (int): Loss threshold.
- `attempts_left` (int): Usually `max_attempts - attempts_used`.
- `game_state` (enum/str): Current state (`IN_PROGRESS`, `WON`, `LOST`, etc.).
- `last_guess` (str): Most recent input for feedback.
- `last_guess_result` (enum/str): `correct`, `wrong`, `repeated`, `invalid`.
- `status_message` (str): UI/CLI message shown to player.

Optional but useful variables:

- `word_category` (str): Theme/hint category (animals, cities, etc.).
- `hint_text` (str): Optional hint shown to player.
- `start_time` / `end_time` (datetime): Measure duration.
- `score` (int): Your scoring model.
- `streak` (int): Consecutive wins.
- `round_number` (int): Track multi-round sessions.

Validation helpers:

- `is_valid_guess` (bool): Single alphabetic char (or allowed token).
- `is_new_guess` (bool): Guess not in `guessed_letters`.
- `is_word_complete` (bool): All letters revealed.

Rules to define clearly:

- A guess must be valid input (usually one alphabetic character).
- Repeated guesses do not change game progress.
- Correct guess reveals all matching positions in the word.
- Wrong guess increases mistakes by exactly 1.
- Game is won when all unique letters in the word are guessed.
- Game is lost when `attempts_used == max_attempts`.
- No guesses are accepted once state is `WON` or `LOST`.
- Case handling must be consistent (for example, compare lowercase forms).
- Non-letter characters in phrases (space, hyphen, apostrophe) are pre-revealed.

Core invariants (should always stay true):

- `attempts_used >= 0`
- `max_attempts > 0`
- `0 <= attempts_left <= max_attempts`
- `attempts_left == max_attempts - attempts_used`
- `correct_letters` and `wrong_letters` are disjoint.
- `guessed_letters == correct_letters union wrong_letters`
- `display_word` length matches `secret_word` length.
- Every revealed letter in `display_word` appears in `secret_word`.
- If `game_state == WON`, then `is_word_complete == True`.
- If `game_state == LOST`, then `attempts_used == max_attempts`.

State-specific invariants:

- `IN_PROGRESS`: `attempts_used < max_attempts` and word not complete.
- `WON`: word complete and `attempts_used <= max_attempts`.
- `LOST`: word not complete and `attempts_used == max_attempts`.

Good assertion checks after each turn:

- Recompute `display_word` from `secret_word` + `guessed_letters` and compare.
- Verify set relationships (`disjoint`, `union`) for guessed letters.
- Verify counters (`attempts_used`, `attempts_left`) are consistent.

Possible bugs in Word Guess / Hangman implementations:

- Repeated guess counted as wrong attempt.
- Correct guess reveals only first occurrence instead of all occurrences.
- Off-by-one loss condition (`>` vs `>=` around max attempts).
- `attempts_left` not synchronized with `attempts_used`.
- Win condition checks full string equality instead of unique-letter completion.
- Case-sensitivity mismatch (`A` and `a` treated differently by mistake).
- Invalid input (empty, digit, symbol, multi-char) accidentally accepted.
- Whitespace around input not trimmed before validation.
- Non-letter characters in phrases hidden when they should be auto-revealed.
- Guessed-letter sets not updated atomically (state partially updated on error).
- Guess handling still allowed after `WON`/`LOST`.
- Restart/new game forgets to reset one or more variables.
- Random word selection can return empty string or out-of-range index.
- Unicode/accent handling inconsistent (example: `e` vs `é`).
- CLI/UI desynchronization (displayed word does not match internal state).

Defensive checks to prevent these bugs:

- Normalize input and secret word once (case, trim, optional accent policy).
- Use a single `process_guess()` path that updates state in one place.
- Run invariant assertions after every guess during development/tests.
- Add tests for edge cases: repeated guesses, repeated letters, last-attempt win/loss, invalid inputs, restart behavior.

## Auto-Play Design:

Design Decision: Create an auto game loop that mimics the standard game loop but picks a random letter from the alphabet excluding guessed letters.

Constraint: Use recursion to continue the computer's guesses until a win or loss is reached.

Question: How to ensure the computer doesn't pick the same letter twice?
Solution: Subtract guessed letters from a string/list of all possible letters.