from classes.Category import Category


def create_spend_chart(categories) -> str:
    """
    function to create a bar chart that shows the percentage spent in each category passed in

    Args:
    categories (list): a list of Category objects

    Returns:
    str: a string that represents the bar chart

    """
    chart = "Percentage spent by category\n"
    # dictionary comprehension to get the total amount spent in each category
    spent = {
        category.category: sum(
            transaction["amount"]
            for transaction in category.ledger
            if transaction["amount"]
            < 0  # only considering withdrawals (negative amounts in the ledger)
        )
        for category in categories
    }
    total_spent = sum(spent.values())  # total amount spent in all categories
    percentages = {
        category: int(spent[category] / total_spent * 100)
        for category in spent  # dictionary comprehension to get the percentage spent in each category
    }

    for i in range(
        100, -10, -10
    ):  # loop to create the chart with the percentages spent in each category in 10% increments from 100% to 0%
        chart += f"{i:>3}| "  # adding the percentage to the chart with right alignment and a pipe character at the end
        for category in spent:
            chart += (
                "o  " if percentages[category] >= i else "   "
            )  # adding an 'o' if the percentage spent in the category is greater than or equal to the current percentage, otherwise adding a space
        chart += "\n"  # adding a newline character at the end of each row
    chart += (
        "    " + "---" * len(spent) + "-\n"
    )  # adding the x-axis of the chart with dashes and a newline character at the end
    longest_category = max(
        len(category) for category in spent
    )  # getting the length of the longest category name in the list of categories passed in
    for i in range(
        longest_category
    ):  # loop to create the category names in the chart with the correct spacing
        chart += "     "  # adding 5 spaces before the category name
        for category in spent:  # loop to add the category name with the correct spacing
            chart += f"{category[i] if i < len(category) else ' '}  "
        chart += "\n"  # adding a newline character at the end of each row
    return chart.rstrip("\n")


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
auto = Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(15, "insurance")
categories = [food, clothing, auto]
print(create_spend_chart(categories))
