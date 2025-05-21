from classes.Generator import Generator


def check_empty_string(input_string: str) -> str:
    """
    Checks if the input string is empty.

    Args:
        input_string (str): The string to check.

    Returns:
        str: The validated input string.
    """
    if input_string.strip() == "":
        raise ValueError("Input cannot be empty.")
    return input_string


def start_generator():
    """
    Starts the Mad Libs game by prompting the user for input and generating a story.
    """
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:")

    # Prompt the user for input

    place = check_empty_string(
        input("Enter a place: ")
    )  # check if the input is empty and prompt again if it is

    adjective = check_empty_string(
        input("Enter an adjective: ")
    )

    noun = check_empty_string(
        input("Enter a noun: ")
    )

    verb = check_empty_string(
        input("Enter a verb: ")
    )

    emotion = check_empty_string(
        input("Enter an emotion: ")
    )

    gen = Generator(
        place, adjective, noun, verb, emotion
    ).generate()  # create an instance of the Generator class and generate the story

    print("Here is your stodsary:")
    print(gen)
