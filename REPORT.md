# Project Report: Guess The Word

## First Impressions
The initial goal was to build a Hangman game using AI assistance. My main assumption was that the core challenge would be the logic, but the strict constraints (no loops and no `.replace()`) made the recursive implementation the real focus.

## Key Learnings
- **Recursion vs. Loops**: I learned how to replace a standard `while True` loop with a recursive `game_loop` to manage state.
- **Input Validation**: I discovered that without strict validation (length checks), the game logic could break if a user entered a whole word instead of a letter.

## CoPilot Prompting Experience
- **Effective Prompts**: "Can you review my `update_game_state` function for purity and no-loops?" worked well because it was specific.
- **Ineffective Prompts**: Asking for the "whole game" at once led to code that violated lab constraints, such as using `while` loops.

## Limitations and Reliability
CoPilot initially missed the need for case-insensitivity in the logic. I had to manually add `.lower()` normalization to fix a failing unit test. This showed me that AI-generated code requires human-led testing to be reliable.

## Overall Reflection
The AI improved my productivity by providing code scaffolding, but the strict lab constraints forced me to take full control of the final implementation to ensure compliance. I learned that AI is a great collaborator, but the developer is responsible for the final logic.