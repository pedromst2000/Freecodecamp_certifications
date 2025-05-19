class Operator:
    op = None

    def __init__(self, op: str):  # Constructor
        """Initialize the operator with a string.

        Args:
            op (str): The operator string. It can be one of the following:
                - '+' for addition
                - '-' for subtraction
                - '*' for multiplication
                - '/' for division
                - '%' for modulus
                - '**' for power
                - 'sqrt' for square root
        Raises:
            ValueError: If the operator is not one of the above.
        Examples:
            >>> op = Operator('+')
            >>> op.op
            '+'
            >>> op = Operator('sqrt')
            >>> op.op
            'sqrt'

            >>> op = Operator('invalid')
            Traceback (most recent call last):
                ...
            ValueError: Invalid operator. Must be one of ['+', '-', '*', '/', '%', '**', 'sqrt'].
        """

        self.op = op

    def sum(self, a: float, b: float) -> float:
        """Perform addition of two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The sum of a and b.
        Examples:
            >>> op = Operator('+')
            >>> op.sum(2, 3)
            5
            >>> op.sum(2.5, 3.5)
            6.0

        """
        if self.op != "+":
            raise ValueError("Invalid operator. Must be '+' for addition.")
        return a + b

    def sub(self, a: float, b: float) -> float:
        """Perform subtraction of two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The difference of a and b.
        Examples:
            >>> op = Operator('-')
            >>> op.sub(5, 3)
            2
            >>> op.sub(2.5, 3.5)
            -1.0
        """
        if self.op != "-":
            raise ValueError("Invalid operator. Must be '-' for subtraction.")

        return a - b

    def mul(self, a: float, b: float) -> float:
        """
        Perform multiplication of two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The product of a and b.
        Examples:
            >>> op = Operator('*')
            >>> op.mul(2, 3)
            6
            >>> op.mul(2.5, 3.5)
            8.75

        """
        if self.op != "*":
            raise ValueError("Invalid operator. Must be '*' for multiplication.")
        return a * b

    def div(self, a: float, b: float) -> float:
        """Perform division of two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The quotient of a and b.
        Examples:
            >>> op = Operator('/')
            >>> op.div(6, 3)
            2.0
            >>> op.div(7.5, 2.5)
            3.0
        """
        if self.op != "/":
            raise ValueError("Invalid operator. Must be '/' for division.")
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def mod(self, a: float, b: float) -> float:
        """Perform modulus of two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The modulus of a and b.
        Examples:
            >>> op = Operator('%')
            >>> op.mod(5, 3)
            2
            >>> op.mod(7.5, 2.5)
            0.0
        """
        if self.op != "%":
            raise ValueError("Invalid operator. Must be '%' for modulus.")
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a % b

    def pow(self, a: float, b: float) -> float:
        """Perform exponentiation of two numbers.
        Args:
            a (float): The base.
            b (float): The exponent.
        Returns:
            float: The result of a raised to the power of b.
        Examples:
            >>> op = Operator('**')
            >>> op.pow(2, 3)
            8
            >>> op.pow(5, 2)
            25
        """
        if self.op != "**":
            raise ValueError("Invalid operator. Must be '**' for exponentiation.")
        return a**b

    def sqrt(self, a: float) -> float:
        """Perform square root of a number.
        Args:
            a (float): The number.
        Returns:
            float: The square root of a.
        Examples:
            >>> op = Operator('sqrt')
            >>> op.sqrt(4)
            2.0
            >>> op.sqrt(9)
            3.0
        """
        if self.op != "sqrt":
            raise ValueError("Invalid operator. Must be 'sqrt' for square root.")

        if a < 0:
            raise ValueError("Square root of negative number is not allowed.")
        return a**0.5
