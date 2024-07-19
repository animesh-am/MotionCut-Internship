from csvhandler import CSVHandler
from quiz import Quiz


def main():
    # Create a CSVHandler object to read questions from a CSV file
    csv_handler = CSVHandler("questions.csv")
    questions = csv_handler.read_questions()

    # List available categories and difficulties
    categories = set(q.category for q in questions)
    difficulties = set(q.difficulty for q in questions)
    num_questions_options = [3, 5, 10]

    # Get user preferences
    print("Available categories:", ", ".join(categories))
    category = input("Select a category: ")

    print("Available difficulties:", ", ".join(difficulties))
    difficulty = input("Select a difficulty: ")

    print("Number of questions options:", ", ".join(map(str, num_questions_options)))
    num_questions = int(input("Select the number of questions: "))

    # Create a Quiz object with the list of questions
    quiz = Quiz(questions)

    # Run the quiz
    quiz.run(category.title(), difficulty.title(), num_questions)


if __name__ == "__main__":
    main()
