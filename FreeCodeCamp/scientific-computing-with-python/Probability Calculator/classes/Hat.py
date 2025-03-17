import random


class Hat:

    def __init__(self, **contents: dict):
        """
        Constructor for the Hat class.

        Initializes the Hat object with a dictionary of balls and their quantities.

        Args:
            **contents: A dictionary of balls and their quantities.

        """

        self.contents = []
        for key, value in contents.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, num_balls: int) -> list:
        """
        Method to draw a number of balls from the hat.

        Args:
            num_balls: The number of balls to draw from the hat.

        Returns:
            A list of balls drawn from the hat.
        """

        if num_balls >= len(self.contents):

            drawn_balls = self.contents[
                :
            ]  # Creating a copy of the contents list to avoid modifying the original list
            self.contents.clear()  # Clearing the original contents list
            return drawn_balls  # Returning a copy of the contents to avoid modifying the original list
        else:
            drawn_balls = random.sample(
                self.contents, num_balls
            )  # Randomly select balls from the hat
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls
