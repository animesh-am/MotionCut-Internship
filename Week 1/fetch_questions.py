import requests
import csv

# Define the category mappings based on the API specification
categories = {
    "music": "Music",
    "sport_and_leisure": "Sports",
    "film_and_tv": "Film and TV",
    "arts_and_literature": "Arts and Literature",
    "history": "History",
    "society_and_culture": "Society and Culture",
    "science": "Science",
    "geography": "Geography",
    "food_and_drink": "Food and Drink",
    "general_knowledge": "General Knowledge",
}


def fetch_questions(category, difficulty, amount=10):
    url = f'https://api.example.com/questions?amount={amount}&category={category}&difficulty={difficulty}'
    response = requests.get(url)
    data = response.json()

    # Debugging: Print the response data to understand the structure
    print(f"URL: {url}")
    print(f"Response: {data}")

    if 'questions' not in data:
        raise ValueError("The API response does not contain 'questions'. Check the API URL and parameters.")

    return data['questions']


def format_question(question_data):
    category = categories.get(question_data['category'], question_data['category'])
    difficulty = question_data['difficulty'].capitalize()
    question = question_data['question']
    options = question_data['incorrectAnswers']
    correct_answer = question_data['correctAnswer']
    options.append(correct_answer)
    options.sort()
    correct_option = chr(options.index(correct_answer) + ord('A'))
    formatted_question = [category, difficulty, question] + options + [correct_option]
    return formatted_question


def save_to_csv(filename, questions):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["category", "difficulty", "question", "A", "B", "C", "D", "answer"])
        for question in questions:
            writer.writerow(question)


# Example usage
all_questions = []
for category_name, category_id in categories.items():
    for difficulty in ['easy', 'medium', 'hard']:
        questions_data = fetch_questions(category_id, difficulty, amount=20)
        for question_data in questions_data:
            formatted_question = format_question(question_data)
            all_questions.append(formatted_question)

save_to_csv('questions.csv', all_questions)
