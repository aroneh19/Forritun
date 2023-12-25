from question import Question

class ChoiceQuestion(Question):
    def __init__(self, question):
        super().__init__(question, "")  # Calls the parent class's constructor
        self.choices = []  # Initializes an empty list to store choices

    def add_choice(self, choice, correct):
        self.choices.append((choice, correct))  # Adds a new choice to the list of choices
        if correct:
            self.correct_choice = len(self.choices)  # Sets the correct_choice attribute if the choice is correct
    
    def check_answer(self, response):
        return str(response) == str(self.correct_choice)  # Checks if the response matches the correct choice

    def get_question(self):
        question = super().get_question() + "\n"  # Gets the question text from the parent class
        for i, choice in enumerate(self.choices, 1):
            if i == len(self.choices):
                question += f"{i}. {choice[0]}"  # Adds the choice text to the question string
            else:
                question += f"{i}. {choice[0]}\n"  # Adds the choice text with a newline to the question string
        return question

    def __repr__(self):
        answer_number = 0
        for i, choice in enumerate(self.choices, 1):
            if choice[1]:
                answer_number = i  # Sets the answer_number to the index of the correct choice
                break
        return super().__repr__() + str(answer_number)  # Returns the representation of the question with the correct answer number
