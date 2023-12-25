from question import Question
from choice_question import ChoiceQuestion

class Exam:
    def __init__(self):
        self.questions = []
        self.points = 0

    def add_question(self, question):
        self.questions.append(question)  # Adds a question to the list of questions
    
    def take(self):
        # Takes the exam, prints each question, takes user input, and checks the response
        for question in self.questions:
            print(question.get_question())  # Prints the current question
            response = input()
            result = question.check_answer(response)  # Checks if the response is correct
            print(result)  # Prints whether the response was correct or not
            if result:
                self.points += 1  # Increases points if the response is correct
            print()
    
    def get_points(self):
        return self.points
    
    def get_num_questions(self):
        return len(self.questions)  # Returns the total number of questions in the exam
    
    def __repr__(self):
        result = ""
        for question in self.questions:
            result += repr(question) + "\n"  # Adds the representation of each question to the result string
        return result.strip()  # Returns the formatted result string without leading or trailing whitespaces
