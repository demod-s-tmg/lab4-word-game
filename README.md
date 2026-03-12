# Lab 4 – Guess The Word Game

**EPITA – Generative AI for Software Engineering 2026**

A terminal-based word-guessing game (Wordle / Hangman style) built under strict lab constraints: **no loops**, **no string replacement**, and **clean logic/UI separation**.

---

## Rules

- A random 5-letter word is chosen at the start of each game.
- The player guesses one letter at a time.
- The masked word is displayed after each guess (e.g. `_ P _ L E`).
- The player has **6 lives**. Each unique wrong letter costs one life.
- Repeating an already-guessed letter does **not** cost a life.
- The game ends when the word is fully revealed (win) or lives reach 0 (loss).

---

## Project Structure

```
lab4-word-game/
├── main.py                     # Game logic and entry point
├── test_update_game_state.py   # Unit tests for update_game_state()
├── REPORT.md                   # Lab report
├── JOURNAL.md                  # Interaction journal (AI4SE requirement)
├── # My Original Thinking/
│   └── MY_NOTES.md             # Design notes and CoPilot suggestions
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- (Optional) a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Run the game

```powershell
python main.py
```

### Run the tests

```powershell
python -m unittest test_update_game_state.py -v
```

---

## Lab Constraints Met

| Constraint | How it is satisfied |
|---|---|
| No `for`/`while` loops | Game loop uses **recursion** (`game_loop` calls itself) |
| No string `.replace()` | Masked word built with **list comprehension** + `"".join()` |
| Logic / UI separation | `update_game_state` is a **pure function**; `display_game` handles all output |
| Immutable inputs | `update_game_state` never mutates its parameters; returns new state |
| Input validation | Only a single alphabetic character is accepted; invalid input recurses with no life loss |

---

## Key Functions

### `update_game_state(secret_word, guessed_letters, guess, lives) → (list, int)`
Pure function. Returns updated `guessed_letters` list and `lives` count based on the guess. Case-insensitive.

### `display_game(secret_word, guessed_letters, lives)`
Prints the masked word, guessed letters, and remaining lives. No mutation.

### `game_loop(secret_word, guessed_letters, lives)`
Recursive game driver. Handles win/lose detection, input validation, and state progression without any loops.

### `start_new_game()`
Selects a random 5-letter word from the built-in word list and starts a fresh `game_loop`.

---

## Word List

The current word pool (all 5 letters):

`apple`, `bread`, `cloud`, `dance`, `earth`, `flame`, `grape`, `house`

---

## Author

EPITA Student – AI4SE Lab 4, March 2026
