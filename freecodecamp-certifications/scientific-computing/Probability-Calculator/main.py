from classes.Hat import Hat
import copy


def experiment(
    hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int
) -> float:
    """

    Function to run an experiment to determine the probability of drawing a certain number of balls from a hat.

    Args:
        hat: The hat object containing the balls.
        expected_balls: A dictionary of the expected balls and their quantities.
        num_balls_drawn: The number of balls to draw from the hat.
        num_experiments: The number of experiments to run.

    Returns:
        The probability of drawing the expected balls from the hat.
    """

    count = 0

    for _ in range(num_experiments):  # Running the experiment num_experiments times
        # Creating a deep copy of the hat object to avoid modifying the original hat
        hat_copy = copy.deepcopy(hat)
        # Drawing num_balls_drawn balls from the hat
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}

        for ball in drawn_balls:  # Counting the number of each ball drawn
            if ball in drawn_dict:
                drawn_dict[ball] += 1  # Incrementing the count of the ball
            else:
                drawn_dict[ball] = 1  # Adding the ball to the dictionary

        match = True  # Flag to check if the expected balls are drawn

        for (
            key,
            value,
        ) in (
            expected_balls.items()
        ):  # Checking if the expected balls are drawn in the correct quantities
            if key not in drawn_dict or drawn_dict[key] < value:
                match = False  # If the expected ball is not drawn or drawn in fewer quantities, setting the flag to False
                break

        if match:  # If the expected balls are drawn, incrementing the counts
            count += 1

    probability = count / num_experiments  # Calculating the probability

    return probability


# -------------------------------OUTPUT---------------------------------
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)

print(f"Probability: {probability}")
