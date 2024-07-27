import tkinter as tk
import re
from tkinter import messagebox


def count_words(text):
    """Function to count the number of words in a given text"""
    # Regular expression to replace the multiple punctuation marks with a single space
    cleaned_text = re.sub(r'[^\w\s]', ' ', text)
    # Split the cleaned text into words
    words = cleaned_text.split()
    return len(words)


def count_button_click():
    """Function to handle the count button click event"""
    # Get the text from the text entry widget
    user_input = text_entry.get("1.0", tk.END).strip()

    # Check if the input is empty
    if not user_input:
        # Show error if empty
        messagebox.showerror(title="Input Error", message="The input cannot be empty. Please enter some text.")
    else:
        # Count the number of words
        word_count = count_words(user_input)
        # Display the word count in a label
        messagebox.showinfo(title="Success", message=f"The number of words in the given text is: {word_count}")


# Create the main window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x400")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter a sentence or paragraph below:", font=("Arial", 13))
instruction_label.pack(pady=10)

# Create a text entry widget
text_entry = tk.Text(root, height=10, width=40, wrap=tk.WORD, font=("Arial", 13))
text_entry.pack(pady=10)

# Create a button to count words
count_button = tk.Button(root, text="Count Words", command=count_button_click, font=("Arial", 13))
count_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()
