class Question:
    def __init__(self, category, difficulty, question_text, options, correct_answer):
        self.category = category
        self.difficulty = difficulty
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        print(self.question_text)
        for option in self.options:
            print(option)

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
