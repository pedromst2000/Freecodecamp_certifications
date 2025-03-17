from classes.Rectangle import Rectangle


class Square(Rectangle):  # inherits from Rectangle class (properties and methods)

    def __init__(self, side: int) -> None:
        """
        Constructor method to initialize the Square class with side.

        Args:
            side (int): The side of the square.

        Returns:
            None
        """

        super().__init__(
            side, side
        )  # to inherit properties and methods from Rectangle class (parent class)

        self.side = side  # to set the side of the square

    def set_side(self, side: int) -> None:
        """
        Method to set the side of the square.

        Args:
            side (int): The side of the square.

        Returns:
            None

        """

        self.width = side
        self.height = side

    def set_width(self, width: int) -> None:
        """
        Method to set the width of the square.

        Args:
            width (int): The width of the square.

        Returns:
            None

        """

        self.set_side(width)

    def set_height(self, height: int) -> None:
        """
        Method to set the height of the square.

        Args:
            height (int): The height of the square.

        Returns:
            None

        """

        self.set_side(height)

    def __str__(self) -> str:
        """
        Method to return a string that represents the square.

        Returns:
            str: The square.

        """

        return f"Square(side={self.width})"
