import unittest

from main import update_game_state


class TestUpdateGameState(unittest.TestCase):
    def test_new_correct_guess_adds_letter_without_losing_life(self):
        new_letters, new_lives = update_game_state("python", ["p"], "y", 6)

        self.assertEqual(new_letters, ["p", "y"])
        self.assertEqual(new_lives, 6)

    def test_repeated_guess_does_not_change_letters_or_lives(self):
        original_letters = ["p", "y"]
        new_letters, new_lives = update_game_state("python", original_letters, "y", 5)

        self.assertEqual(new_letters, ["p", "y"])
        self.assertEqual(new_lives, 5)
        self.assertIsNot(new_letters, original_letters)

    def test_wrong_new_guess_decrements_life_once(self):
        new_letters, new_lives = update_game_state("python", ["p"], "z", 6)

        self.assertEqual(new_letters, ["p", "z"])
        self.assertEqual(new_lives, 5)

    def test_uppercase_guess_should_be_treated_case_insensitively(self):
        # Desired behavior: uppercase input should match lowercase secret words.
        new_letters, new_lives = update_game_state("python", ["p"], "Y", 6)

        self.assertEqual(new_letters, ["p", "y"])
        self.assertEqual(new_lives, 6)

    def test_repeated_letters_in_secret_word_are_covered_by_single_guess(self):
        # Guessing 'e' once should still be considered a correct guess for "letter".
        new_letters, new_lives = update_game_state("letter", ["l"], "e", 6)

        self.assertEqual(new_letters, ["l", "e"])
        self.assertEqual(new_lives, 6)


if __name__ == "__main__":
    unittest.main()
