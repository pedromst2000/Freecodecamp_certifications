class Category:

    def __init__(
        self,
        category: str,
        ledger: list = None,
    ):
        """
        constructor for the Category class

        Args:
        category (str): the name of the category
        ledger (list): a list of transactions (default is an empty)

        """
        self.category = category
        self.ledger = (
            ledger if ledger is not None else []
        )  # ledger is set to an empty list if ledger is None

    def deposit(self, amount: float, description: str = "") -> None:
        """
        method to deposit money into the category

        Args:
        amount (float): the amount of money to deposit
        description (str): the description of the deposit transaction (default is an empty string)

        Returns:
        None: None is returned on successful deposit

        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """
        method to withdraw money from the category

        Args:
        amount (float): the amount of money to withdraw
        description (str): the description of the withdrawal transaction (default is an empty string)

        Returns:
        bool: True if the withdrawal was successful, False otherwise

        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        """
        method to get the current balance of the budget category

        Returns:
        float: the balance of the budget category

        """
        return sum(transaction["amount"] for transaction in self.ledger)

    def transfer(self, amount: float, category: "Category") -> bool:
        """
        method to transfer money between categories

        Args:
        amount (float): the amount of money to transfer
        category (Category): the category to transfer the money to

        Returns:
        bool: True if the transfer was successful, False otherwise

        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        """
        method to check if there are enough funds in the category

        Args:
        amount (float): the amount of money to check

        Returns:
        bool: True if there are enough funds, False otherwise

        """
        return self.get_balance() >= amount

    def __str__(self) -> str:
        """
        method to return a string representation of the budget category

        Returns:
        str: a string representation of the budget category

        """
        title = f"{self.category:*^30}\n"  # centering the category name in a line of 30 asterisks
        items = ""
        for transaction in self.ledger:
            items += (
                f"{transaction['description'][:23]:<23}"  # limiting the description to 23 characters
                + f"{transaction['amount']:>7.2f}"  # formatting the amount to 2 decimal places
                + "\n"  # adding a newline character
            )
        total = f"Total: {self.get_balance()}"
        return title + items + total
