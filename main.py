"""
Guess The Word Game
EPITA - Generative AI for Software Engineering 2026
"""

import random
import string # Moved to the top so all functions can see it

# --- LOGIC LAYER ---

def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int]:
    """
    Updates the game state based on the user's guess.
    Constraints: No Loops, Pure Function, Immutable inputs.
    """
    normalized_guess = guess.lower() 
    normalized_secret_word = secret_word.lower()

    # Create new list to preserve immutability
    new_guessed_letters = guessed_letters[:] if normalized_guess in guessed_letters else guessed_letters + [normalized_guess]

    # Only decrement lives for new incorrect guesses
    if normalized_guess not in normalized_secret_word and normalized_guess not in guessed_letters:
        lives -= 1
        
    return new_guessed_letters, lives

# --- UI LAYER ---

def display_game(secret_word: str, guessed_letters: list[str], lives: int):
    """
    Displays the masked word and status.
    Constraint: No string replacement functions.
    """
    masked = "".join([char if char in guessed_letters else "_" for char in secret_word])
    print(f"\nWord: {masked}")
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Lives remaining: {lives}")

# --- GAME MODES (RECURSION) ---

def game_loop(secret_word: str, guessed_letters: list[str], lives: int):
    """Main game logic using recursion to avoid 'while True'."""
    display_game(secret_word, guessed_letters, lives)
    
    # Win/Lose Detection
    if all(char in guessed_letters for char in secret_word):
        print(f"Congratulations! You won! The word was: {secret_word}")
        return
    if lives <= 0:
        print(f"Game Over! The word was: {secret_word}")
        return

    raw_input = input("Guess a letter: ").lower().strip()

    # Input Validation
    if len(raw_input) != 1 or not raw_input.isalpha():
        print("Invalid input! Please enter exactly one letter (a-z).")
        return game_loop(secret_word, guessed_letters, lives)
    
    new_letters, new_lives = update_game_state(secret_word, guessed_letters, raw_input, lives)
    game_loop(secret_word, new_letters, new_lives)

def auto_game_loop(secret_word: str, guessed_letters: list[str], lives: int):
    """Computer plays the game automatically using recursion."""
    display_game(secret_word, guessed_letters, lives)
    
    if all(char in guessed_letters for char in secret_word):
        print(f"Computer WON! The word was: {secret_word}")
        return
    if lives <= 0:
        print(f"Computer LOST! The word was: {secret_word}")
        return

    # Logic: Filter out letters already guessed to avoid repeats
    available_letters = [l for l in string.ascii_lowercase if l not in guessed_letters]
    computer_guess = random.choice(available_letters)
    
    print(f"Computer guesses: {computer_guess}")
    
    new_letters, new_lives = update_game_state(secret_word, guessed_letters, computer_guess, lives)
    auto_game_loop(secret_word, new_letters, new_lives)

# --- SETUP ---

def select_mode():
    """Gives the user the option to play or watch the computer play."""
    print("\n--- MODE SELECTION ---")
    print("1. Manual Play")
    print("2. Auto-Play (Computer)")
    choice = input("Enter '1' or '2': ").strip()
    
    words = ["apple", "bread", "cloud", "dance", "earth", "flame", "grape", "house"]
    secret_word = random.choice(words)
    
    if choice == '1':
        game_loop(secret_word, [], 6)
    elif choice == '2':
        auto_game_loop(secret_word, [], 6)
    else:
        print("Invalid choice.")
        return select_mode()

if __name__ == "__main__":
    def play():
        select_mode() 
        if input("\nPlay or Auto-Play again? (y/n): ").lower() == 'y':
            play()
    play()