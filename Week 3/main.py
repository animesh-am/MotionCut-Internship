import tkinter as tk
from ExpenseDatabase import ExpenseDatabase
from ExpenseTrackerUI import ExpenseTrackerUI

if __name__ == "__main__":
    expense_database = ExpenseDatabase()

    root = tk.Tk()
    app = ExpenseTrackerUI(root, expense_database)
    root.mainloop()
