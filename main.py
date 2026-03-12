"""
Guess The Word Game
EPITA - Generative AI for Software Engineering 2026
"""

import random

def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    """
    Updates the game state based on the user's guess.
    
    Constraints:
    - No Loops 
    - Must be pure (no global variables) 
    - Input parameters are immutable 
    """
    normalized_guess = guess.lower() 
    normalized_secret_word = secret_word.lower()

    # Create a new list for immutability 
    new_guessed_letters = guessed_letters[:] if normalized_guess in guessed_letters else guessed_letters + [normalized_guess]

    # Only decrement lives if it's a new wrong guess
    if normalized_guess not in normalized_secret_word and normalized_guess not in guessed_letters:
        lives -= 1
        
    return new_guessed_letters, lives

def display_game(secret_word: str, guessed_letters: list[str], lives: int):
    """
    Displays the masked word (e.g., __S_E__) and current status[cite: 15, 16].
    Constraint: No string replacement functions[cite: 215].
    """
    # Use list comprehension to avoid loops and .replace() [cite: 214, 215]
    masked = "".join([char if char in guessed_letters else "_" for char in secret_word])
    print(f"\nWord: {masked}")
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Lives remaining: {lives}")

def game_loop(secret_word: str, guessed_letters: list[str], lives: int):
    """
    Main game logic using recursion to avoid 'while True'[cite: 214].
    """
    display_game(secret_word, guessed_letters, lives)
    
    # Win/Lose Detection [cite: 18, 212]
    if all(char in guessed_letters for char in secret_word):
        print(f"Congratulations! You won! The word was: {secret_word}")
        return
    if lives <= 0:
        print(f"Game Over! The word was: {secret_word}")
        return

    # Get input and normalize
    raw_input = input("Guess a letter: ").lower().strip()

    # NEW: Input Validation to prevent whole-word guessing bugs [cite: 11, 126]
    if len(raw_input) != 1 or not raw_input.isalpha():
        print("Invalid input! Please enter exactly one letter (a-z).")
        # Recurse with original state so no life is lost
        return game_loop(secret_word, guessed_letters, lives)
    
    # Process valid single-letter guess
    new_letters, new_lives = update_game_state(secret_word, guessed_letters, raw_input, lives)
    
    game_loop(secret_word, new_letters, new_lives)

def start_new_game():
    """Sets up and starts a game session[cite: 14, 208]."""
    # Updated to 5-letter words only for better consistency
    words = ["apple", "bread", "cloud", "dance", "earth", "flame", "grape", "house"]
    secret_word = random.choice(words)
    game_loop(secret_word, [], 6) # Default 6 turns [cite: 13]

if __name__ == "__main__":
    # Support replay without restarting [cite: 216]
    def play():
        start_new_game()
        if input("\nPlay again? (y/n): ").lower() == 'y':
            play()
    play()