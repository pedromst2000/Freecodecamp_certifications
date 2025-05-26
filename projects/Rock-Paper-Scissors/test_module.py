import game  # Importing the game module to test
from classes.Game import (
    Game,
)  # Importing the Game class from the classes module to test its functionality
import unittest  # Importing unittest for testing
from unittest.mock import patch  # mocking library to simulate user input
from unittest import (
    TestCase,
)  # Importing TestCase to create test cases for the game module


class TestGameModule(TestCase):
    def setUp(self):
        """
        Sets up the test environment for the game module.
        Initializes valid choices, mode choices, player names, and a Game instance.
        """
        self.valid_choices = game.VALID_CHOICES
        self.mode_choices = game.MODE_CHOICES
        self.player1 = "Alice"
        self.player2 = "Bob"
        self.game = Game(self.player1, self.player2, "normal", self.valid_choices)

    @patch("builtins.input", return_value="normal")
    def test_get_mode_choice_normal(self, mock_input):
        """
        Tests the get_mode_choice function to ensure it returns 'normal' when input is 'normal'.
        """
        mode = game.get_mode_choice()
        self.assertEqual(
            mode,
            "normal",
            f"Expected mode to be 'normal', but got '{mode}'",
        )
        mock_input.assert_called_once_with(
            "Enter 'normal' for player vs player or 'computer' for player vs computer: "
        )
        
    @patch("builtins.input", return_value="computer")
    def test_get_mode_choice_computer(self, mock_input):
        """
        Tests the get_mode_choice function to ensure it returns 'computer' when input is 'computer'.
        """
        mode = game.get_mode_choice()
        self.assertEqual(
            mode,
            "computerr",
            f"Expected mode to be 'computer', but got '{mode}'",
        )
        mock_input.assert_called_once_with(
            "Enter 'normal' for player vs player or 'computer' for player vs computer: "
        )

    @patch("builtins.input", return_value="Alice")
    def test_get_player_name_valid(self, mock_input):
        """
        Tests the get_player_name function to ensure it returns a valid player name.
        """
        name = game.get_player_name("Enter your name: ")
        self.assertEqual(
            name,
            "Alice",
            f"Expected player name to be 'Alice', but got '{name}'",
        )
        mock_input.assert_called_once_with("Enter your name: ")

    @patch("builtins.input", return_value="")
    def test_get_player_name_invalid_empty(self, mock_input):
        """
        Tests the get_player_name function to ensure it raises an error for an empty name.
        """
        with self.assertRaises(ValueError):
            game.get_player_name("Enter your name: ")
        mock_input.assert_called_once_with("Enter your name: ")

    @patch("builtins.input", return_value="123")
    def test_get_player_name_invalid_numbers(self, mock_input):
        """
        Tests the get_player_name function to ensure it raises an error for a name with numbers.
        """
        with self.assertRaises(ValueError):
            game.get_player_name("Enter your name: ")
        mock_input.assert_called_once_with("Enter your name: ")
    @patch("builtins.input", return_value="rock")
    def test_get_player_choice_valid(self, mock_input):
        """
        Tests the get_player_choice function to ensure it returns a valid player choice.
        """
        choice = game.get_player_choice("Alice")
        self.assertEqual(
            choice,
            "rock",
            f"Expected player choice to be 'rock', but got '{choice}'",
        )
        mock_input.assert_called_once_with("Alice, enter your choice (rock/paper/scissors): ")
    @patch("builtins.input", return_value="invalid")
    def test_get_player_choice_invalid(self, mock_input):
        """
        Tests the get_player_choice function to ensure it raises an error for an invalid choice.
        """
        with self.assertRaises(ValueError):
            game.get_player_choice("Alice")
        mock_input.assert_called_once_with("Alice, enter your choice (rock/paper/scissors): ")
        self.assertIn(mock_input.return_value, self.valid_choices)
    @patch("builtins.input", return_value="paper")
    def test_get_player_choice_invalid_choice(self, mock_input):
        """
        Tests the get_player_choice function to ensure it raises an error for an invalid choice.
        """
        with self.assertRaises(ValueError):
            game.get_player_choice("Alice")
        mock_input.assert_called_once_with("Alice, enter your choice (rock/paper/scissors): ")
        self.assertIn(mock_input.return_value, self.valid_choices)
    @patch("builtins.input", return_value="scissors")
    def test_get_player_choice_invalid_choice2(self, mock_input):
        """
        Tests the get_player_choice function to ensure it raises an error for an invalid choice.
        """
        with self.assertRaises(ValueError):
            game.get_player_choice("Alice")
        mock_input.assert_called_once_with("Alice, enter your choice (rock/paper/scissors): ")
        self.assertIn(mock_input.return_value, self.valid_choices)
    @patch("builtins.input", return_value="rock")
    def test_get_player_choice_invalid_choice3(self, mock_input):
        """
        Tests the get_player_choice function to ensure it raises an error for an invalid choice.
        """
        with self.assertRaises(ValueError):
            game.get_player_choice("Alice")
        mock_input.assert_called_once_with("Alice, enter your choice (rock/paper/scissors): ")
        self.assertIn(mock_input.return_value, self.valid_choices)

    @patch("random.choice", return_value="paper")
    def test_computer_choice(self, mock_random_choice):
        """
        Tests the computer_choice method to ensure it returns a valid choice.
        """
        self.game.mode = "computer"
        choice = self.game.computer_choice()
        self.assertIn(
            choice,
            self.valid_choices,
            f"Expected computer choice to be one of {self.valid_choices}, but got '{choice}'",
        )
        mock_random_choice.assert_called_once_with(self.valid_choices)

    def test_set_choices(self):
        """
        Tests the set_choices method to ensure it sets the choices correctly.
        """
        self.game.set_choices("rock", "paper")
        self.assertEqual(
            self.game.choice1,
            "rock",
            f"Expected choice1 to be 'rock', but got '{self.game.choice1}'",
        )
        self.assertEqual(
            self.game.choice2,
            "paper",
            f"Expected choice2 to be 'paper', but got '{self.game.choice2}'",
        )

    def test_determine_winner(self):
        """
        Tests the determine_winner method to ensure it correctly determines the winner
        and uses the dynamic player name.
        """
        self.game.set_choices("rock", "scissors")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            self.player1,
            f"Expected winner to be '{self.player1}', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            f"{self.player1} wins!",
            f"Expected result to be '{self.player1} wins!', but got '{result}'",
        )

        self.game.set_choices("paper", "rock")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            self.player1,
            f"Expected winner to be '{self.player1}', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            f"{self.player1} wins!",
            f"Expected result to be '{self.player1} wins!', but got '{result}'",
        )

        self.game.set_choices("scissors", "paper")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            self.player1,
            f"Expected winner to be '{self.player1}', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            f"{self.player1} wins!",
            f"Expected result to be '{self.player1} wins!', but got '{result}'",
        )

        self.game.set_choices("rock", "rock")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            "tie",
            f"Expected winner to be 'tie', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            "It's a tie!",
            f"Expected result to be 'It's a tie!', but got '{result}'",
        )

        self.game.set_choices("paper", "paper")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            "tie",
            f"Expected winner to be 'tie', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            "It's a tie!",
            f"Expected result to be 'It's a tie!', but got '{result}'",
        )

        self.game.set_choices("scissors", "scissors")
        result = self.game.determine_winner()
        self.assertEqual(
            self.game.winner,
            "tie",
            f"Expected winner to be 'tie', but got '{self.game.winner}'",
        )
        self.assertEqual(
            result,
            "It's a tie!",
            f"Expected result to be 'It's a tie!', but got '{result}'",
        )


if __name__ == "__main__":
    unittest.main()
