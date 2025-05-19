from classes.Operator import Operator


def calculator(op: str, a: float, b: float = None) -> float:
    """Perform basic arithmetic operations.
    Args:
        op (str): The operator to use. Must be one of ['+', '-', '*', '/', '%', '**', 'sqrt'].
        a (float): The first number.
        b (float, optional): The second number. Required for all operations except 'sqrt'.
    Returns:
        float: The result of the operation.
    Raises:
        ValueError: If the operator is invalid or if division by zero is attempted.
    Examples:
        >>> calculator('+', 2, 3)
        5
        >>> calculator('-', 5, 3)
        2
        >>> calculator('*', 2, 3)
        6
        >>> calculator('/', 6, 3)
        2.0
        >>> calculator('%', 5, 2)
        1
        >>> calculator('**', 2, 3)
        8
        >>> calculator('sqrt', 4)
        2.0
    """
    op = Operator(op)
    match op.op:
        case "+":
            return op.sum(a, b)
        case "-":
            return op.sub(a, b)
        case "*":
            return op.mul(a, b)
        case "/":
            return op.div(a, b)
        case "%":
            return op.mod(a, b)
        case "**":
            return op.pow(a, b)
        case "sqrt":
            if b is not None:
                raise ValueError("Second argument should be None for 'sqrt' operation.")
            return op.sqrt(a)
        case _:
            raise ValueError(
                f"Invalid operator: {op.op}. Must be one of ['+', '-', '*', '/', '%', '**', 'sqrt']."
            )
    return None


def input_calculator():
    """Function to take user input for the calculator."""
    print("Welcome to the Basic Calculator!")
    print("Available operations: +, -, *, /, %, **, sqrt")
    op = input("Enter the operation: ")
    a = float(input("Enter the first number: "))
    b = None
    if op != "sqrt":
        b = float(input("Enter the second number: "))
    result = calculator(op, a, b)
    print(f"The result of {a} {op} {b if b is not None else ''} is: {result}")


if __name__ == "__main__":
    input_calculator()
