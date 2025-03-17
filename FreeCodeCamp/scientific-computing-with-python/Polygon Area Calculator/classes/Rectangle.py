class Rectangle:

    width = 0
    height = 0

    def __init__(self, width: int, height: int) -> None:
        """
        Constructor method to initialize the Rectangle class with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Returns:
            None
        """

        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        """
        Method to set the width of the rectangle.

        Args:
            width (int): The width of the rectangle.

        Returns:
            None
        """
        self.width = width

    def set_height(self, height: int) -> None:
        """
        Method to set the height of the rectangle.

        Args:
            height (int): The height of the rectangle.

        Returns:
            None
        """
        self.height = height

    def get_area(self) -> int:
        """
        Method to calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.width * self.height

    def get_perimeter(self) -> int:
        """
        Method to calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """

        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        """
        Method to calculate the diagonal of the rectangle.

        Returns:
            float: The diagonal of the rectangle.
        """

        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        """
        Method to return a string that represents the shape of the rectangle.

        Returns:
            str: The shape of the rectangle.
        """

        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        """
        Method to calculate how many times a shape can fit inside the rectangle.

        Args:
            shape (Rectangle): The shape to fit inside the rectangle.

        Returns:
            int: The number of times the shape can fit inside the rectangle.
        """

        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self) -> str:
        """
        Method to return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """

        return f"Rectangle(width={self.width}, height={self.height})"
