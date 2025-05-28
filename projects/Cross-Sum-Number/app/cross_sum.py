from tkinter import Entry, messagebox


def validate_input(input_string: Entry) -> bool:
    """
    Validates the input string to ensure it contains only digits and is not empty.

    :param input_string: Entry widget containing the input string.
    :return: True if the input is valid (non-empty and contains only digits), False otherwise.


    """
    if not input_string or not input_string.isdigit():
        return False
    return True


def show_message(message: messagebox, input_val: Entry) -> None:
    """
    Displays a message box with the given message.

    :param message: The message to be displayed in the message box.
    """
    if not validate_input(input_val):
        message.showerror("Error", "Please enter a valid number.")
    else:
        message.showinfo("Result", f"{calculate_cross_sum(input_val)}")   


def calculate_cross_sum(input_val: str) -> int:
    """
    Calculates the cross sum of the given input value.

    :param input_val: The input value as a string.
    
    :return: The cross sum of the digits in the input value.

    """
    return sum(
        int(digit) for digit in input_val if digit.isdigit()
    )  # This will sum only the digits in the input string
