import csv
from question import Question


class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_questions(self):
        questions = []
        with open(self.filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) != 8:
                    continue
                category = row[0]
                difficulty = row[1]
                question_text = row[2]
                options = row[3:7]  # Assuming there are exactly 4 options
                correct_answer = row[7]
                question = Question(category, difficulty, question_text, options, correct_answer)
                questions.append(question)
        return questions
