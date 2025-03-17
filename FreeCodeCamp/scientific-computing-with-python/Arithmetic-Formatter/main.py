def check_valid_operators(list: list) -> bool:
    """
    Check if all operators in the list are either '+' or '-'.

    Args:
        list (list): List of operators

    Returns:
        bool: True if all operators are valid, False otherwise
    """

    for operator in list:
        if operator != "+" and operator != "-":
            return False
    return True


def check_valid_digits(list: list) -> bool:
    """
    Check if all digits in the list are digits.

    Args:
        list (list): List of digits

    Returns:
        bool: True if all digits are valid, False otherwise
    """

    for digit in list:
        if not digit.isdigit():
            return False
    return True


def check_valid_length(list: list) -> bool:
    """
    Check if all digits in the list are less than 5 digits.

    Args:
        list (list): List of digits

    Returns:
        bool: True if all digits have valid length, False otherwise
    """

    for digit in list:
        if len(digit) > 4:
            return False
    return True


def format_problems(problems: list, show: bool) -> str:
    """
    Format the problems in a string.

    Args:
        problems (list): List of problems
        show (bool): Show answers if True

    Returns:
        str: Formatted problems
        bool: Show answers of the formatted problems if True
    """

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in problems:
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]

        length = max(len(first_operand), len(second_operand)) + 2
        first_line += first_operand.rjust(length) + "    "
        second_line += operator + second_operand.rjust(length - 1) + "    "
        third_line += "-" * length + "    "

        if show:
            if operator == "+":
                answer = str(int(first_operand) + int(second_operand))
            else:
                answer = str(int(first_operand) - int(second_operand))

            fourth_line += answer.rjust(length) + "    "

    if show:
        return (
            first_line.rstrip()
            + "\n"
            + second_line.rstrip()
            + "\n"
            + third_line.rstrip()
            + "\n"
            + fourth_line.rstrip()
        )
    else:
        return (
            first_line.rstrip()
            + "\n"
            + second_line.rstrip()
            + "\n"
            + third_line.rstrip()
        )


def arithmetic_arranger(problems: list, show_answers=False) -> str:
    """
    Arrange arithmetic problems in a string.

    Args:
        problems (list): List of problems
        show_answers (bool, optional): Show answers if True. Defaults to True.

    Returns:
        str: Formatted problems
    """

    if len(problems) > 5:
        return "Error: Too many problems."

    if not check_valid_operators([problem.split()[1] for problem in problems]):
        return "Error: Operator must be '+' or '-'."

    elif not check_valid_digits(
        [problem.split()[0] for problem in problems]
    ) or not check_valid_digits([problem.split()[2] for problem in problems]):
        return "Error: Numbers must only contain digits."

    elif not check_valid_length(
        [problem.split()[0] for problem in problems]
    ) or not check_valid_length([problem.split()[2] for problem in problems]):
        return "Error: Numbers cannot be more than four digits."

    problems = format_problems(problems, show_answers)

    return problems


# Test Cases Logs

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')

print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')

print(
    f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}'
)

print(
    f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}'
)

print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

print(
    f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}'
)
