from classes.Game import Game


VALID_CHOICES = ["rock", "paper", "scissors"]
MODE_CHOICES = ["normal", "computer"]

__all__ = ["VALID_CHOICES", "MODE_CHOICES"] # Exporting constants for use in other modules


def get_mode_choice() -> str:
    while True:  # Loop until a valid mode is returned
        mode = (
            input(
                "Enter 'normal' for player vs player or 'computer' for player vs computer: "
            )
            .strip()
            .lower()
        )
        if mode in MODE_CHOICES:
            return mode
        else:
            msg = "Invalid mode. Please enter 'normal' or 'computer'."
            print(msg)


def get_player_name(prompt: str) -> str:
    while True:  # Loop until a valid name is returned
        name = input(prompt).strip()
        if len(name) > 0 and name.isalpha():
            return name
        else:
            msg = "Name cannot be empty or contain numbers. Please try again."
            print(msg)


def get_player_choice(player_name: str) -> str:
    while True:  # Loop until a valid choice is returned
        choice = (
            input(f"{player_name}, enter your choice (rock/paper/scissors): ")
            .strip()
            .lower()
        )
        if choice in VALID_CHOICES:
            return choice
        else:
            msg = "Invalid choice. Please enter 'rock', 'paper', or 'scissors'."
            print(msg)


def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    mode = get_mode_choice()

    if mode == "normal":
        player1 = get_player_name("Enter the name of Player 1: ")
        player2 = get_player_name("Enter the name of Player 2: ")
    else:
        player1 = get_player_name("Enter your name: ")
        player2 = "Computer"

    game = Game(player1, player2, mode, VALID_CHOICES)  # Initialize the game

    while True:  # Loop to allow multiple games
        choice1 = get_player_choice(player1)
        choice2 = (
            game.computer_choice() if mode == "computer" else get_player_choice(player2)
        )

        game.set_choices(choice1, choice2)
        result = game.determine_winner()

        print(f"{player1} chose: {choice1}")
        print(f"{player2} chose: {choice2}")
        print(result)

        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            break
