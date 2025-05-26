import random


class Game:

    # attributes
    player1: str
    player2: str
    mode: str
    valid_choices: list
    choice1: str
    choice2: str
    winner: str

    def __init__( # class constructor
        self,
        player1: str,
        player2: str,
        mode: str = "normal",
        valid_choices: list = None,
        choice1: str = None,
        choice2: str = None,
        winner: str = None,
    ) -> None:
        """
        Initializes the Game class with player names and mode.


        :param player1: Name of player 1
        :param player2: Name of player 2
        :param mode: Game mode (normal or computer)
        :param valid_choices: List of valid choices for the game
        :param choice1: Choice of player 1
        :param choice2: Choice of player 2
        :param winner: Winner of the game
        """
        self.player1 = player1
        self.player2 = player2
        self.mode = mode
        self.valid_choices = valid_choices
        self.choice1 = choice1
        self.choice2 = choice2
        self.winner = winner

    def set_choices(self, choice1: str, choice2: str) -> None:
        """
        Sets the choices for both players.
        :param choice1: Choice of player 1
        :param choice2: Choice of player 2

        :return: None

        """
        self.choice1 = choice1
        self.choice2 = choice2

    def computer_choice(self) -> str:
        """
        Generates a random choice for the computer player.
        :return: A string representing the computer's choice
        """
        return random.choice(self.valid_choices)

    def determine_winner(self) -> str:
        """
        Determines the winner based on the choices made by both players.

        :return: A string indicating the result of the game
        """
        if self.choice1 == self.choice2:
            self.winner = "tie"
            return "It's a tie!"

        wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if wins[self.choice1] == self.choice2:
            self.winner = self.player1
            return f"{self.player1} wins!"
        else:
            self.winner = self.player2
            return f"{self.player2} wins!"
