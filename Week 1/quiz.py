import random
import time


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.start_time = None

    def filter_questions(self, category, difficulty, num_questions):
        filtered_questions = [q for q in self.questions if q.category == category and q.difficulty == difficulty]
        return random.sample(filtered_questions, min(num_questions, len(filtered_questions)))

    def run(self, category, difficulty, num_questions):
        self.questions = self.filter_questions(category, difficulty, num_questions)
        self.start_time = time.time()
        for question in self.questions:
            question.display()
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)
        self.display_final_score()

    def get_user_answer(self):
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()
        return user_answer

    def check_answer(self, question, user_answer):
        if question.check_answer(user_answer):
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong. The correct answer is {question.correct_answer}")
        print()

    def display_final_score(self):
        end_time = time.time()
        total_time = end_time - self.start_time
        print(f"Your final score is {self.score} out of {len(self.questions)}")
        print(f"You completed the quiz in {total_time:.2f} seconds")
