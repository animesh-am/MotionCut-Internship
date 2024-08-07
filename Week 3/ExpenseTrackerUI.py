import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from datetime import datetime


class ExpenseTrackerUI:
    def __init__(self, root, database):
        """
        Initialize the ExpenseTrackerUI class.

        Parameters:
        root (tk.Tk): The main window object.
        database (ExpenseDatabase): The database object to handle expense data.
        """
        self.database = database
        self.root = root
        self.root.title("Expense Tracker")

        # Variables to hold user input
        self.amount_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.category_var = tk.StringVar()

        # Create and place widgets in the main window
        self.create_widgets()

    def create_widgets(self):
        """
        Create and place widgets in the main window.
        """
        font = ("Helvetica", 14)  # Define a font with a larger size

        # Label and Entry for Amount
        tk.Label(self.root, text="Amount:", font=font).grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.amount_var, font=font).grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for Description
        tk.Label(self.root, text="Description:", font=font).grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.description_var, font=font).grid(row=1, column=1, padx=10, pady=10)

        # Label and Entry for Category
        tk.Label(self.root, text="Category:", font=font).grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.category_var, font=font).grid(row=2, column=1, padx=10, pady=10)

        # Button to Add Expense
        tk.Button(self.root, text="Add Expense", command=self.add_expense, font=font).grid(row=3, column=0,
                                                                                           columnspan=2, pady=10)

        # Button to View Summary
        tk.Button(self.root, text="View Summary", command=self.view_summary, font=font).grid(row=4, column=0,
                                                                                             columnspan=2, pady=10)

    def add_expense(self):
        """
        Add an expense to the database and clear input fields.

        This method gets the values from the input fields, validates them,
        adds the expense to the database, and then clears the input fields.
        """
        try:
            # Get input values and convert category to lower case
            amount = float(self.amount_var.get())
            description = self.description_var.get()
            category = self.category_var.get().upper()

            # Add expense to the database
            self.database.add_expense(amount, description, category)
            messagebox.showinfo("Success", "Expense added successfully!")

            # Clear input fields
            self.amount_var.set("")
            self.description_var.set("")
            self.category_var.set("")
        except ValueError:
            # Handle invalid input for amount
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value for the amount.")

    def view_summary(self):
        """
        Display a summary of expenses, including a pie chart.

        This method retrieves the summary data from the database,
        creates a new window to display the total and category-wise expenses,
        and shows a pie chart for visual representation.
        """
        month = simpledialog.askstring("Input", "Enter the month in YYYY-MM format:",
                                       initialvalue=datetime.now().strftime("%Y-%m"))

        if month:
            # Get summary data from the database for the specified month
            total_amount, category_totals = self.database.get_summary(month)

            # Create a new window for the summary
            summary_window = tk.Toplevel(self.root)
            summary_window.title("Expense Summary")

            font = ("Helvetica", 14)

            if total_amount > 0:
                # Display total expenses
                tk.Label(summary_window, text=f"Total Expenses for {month}: Rs. {total_amount:.2f}", font=font).pack(
                    pady=10)

                # Display category-wise expenses
                tk.Label(summary_window, text="Category-wise Expenses:", font=font).pack(pady=10)
                for category, total in category_totals.items():
                    tk.Label(summary_window, text=f"{category}: Rs. {total:.2f}", font=font).pack()

                # Show pie chart for expense distribution
                self.show_pie_chart(category_totals)
            else:
                # Display a message indicating no expenses were found
                tk.Label(summary_window, text=f"No expenses recorded for {month}.", font=font).pack(pady=10)
        else:
            messagebox.showwarning("Warning", "No month entered. Please try again.")

    def show_pie_chart(self, category_totals):
        """
        Display a pie chart of the expenses by category.

        Parameters:
        category_totals (dict): A dictionary with category names as keys and total amounts as values.
        """
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title("Expense Distribution")
        plt.show()
