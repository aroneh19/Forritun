class Hangman:

    def __init__(self, word: str):
        self.word = word.upper()
        self.hidden = ["_"] * len(self.word)
        self.incorrect = 0

    def guess_letter(self, letter: str) -> bool:
        letter = letter.upper()
        if letter in self.word and letter not in self.hidden:
            for i in range(len(self.word)):
                if letter == self.word[i]:
                    self.hidden[i] = letter
            return True
        else:
            self.incorrect += 1
            return False

    def __str__(self) -> str:
        display = " ".join(self.hidden)
        return f"{display}\nNumber of incorrect guesses: {self.incorrect}"
