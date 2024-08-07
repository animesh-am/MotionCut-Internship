import csv
from datetime import datetime
from ExpenseRecord import ExpenseRecord


class ExpenseDatabase:
    def __init__(self, filename="expenses.csv"):
        """
        Initialize the ExpenseDatabase class with a CSV file.

        Parameters:
        filename (str): The name of the CSV file to store expenses.
        """
        self.filename = filename
        # Create the file if it doesn't exist and write the header
        self.create_file()

    def create_file(self):
        """
        Create the CSV file with headers if it does not exist.
        """
        try:
            with open(self.filename, mode='x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Amount", "Description", "Category"])
        except FileExistsError:
            # File already exists
            pass

    def add_expense(self, amount, description, category):
        """
        Add a new expense to the CSV file with the current date.

        Parameters:
        amount (float): The amount of the expense.
        description (str): A brief description of the expense.
        category (str): The category of the expense.
        """
        date = datetime.now().strftime("%Y-%m-%d")  # Get the current date
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, description, category])

    def get_summary(self, month=None):
        """
        Get the total expenses and category-wise expenditure for a specific month.

        Parameters:
        month (str): The month in YYYY-MM format. If None, use the current month.

        Returns:
        tuple: A tuple containing the total amount of expenses and a dictionary of category-wise expenditure.
        """
        if month is None:
            month = datetime.now().strftime("%Y-%m")

        category_totals = {}
        total_amount = 0.0

        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                date, amount, _, category = row
                if date.startswith(month):
                    amount = float(amount)
                    total_amount += amount
                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

        return total_amount, category_totals
