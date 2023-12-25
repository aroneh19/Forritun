def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()  # Splits the word from the file
            return words  # Returns the all the words as a list
    except FileNotFoundError:
        return None

# Displays the word with guessed letters
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "- "
    return displayed.strip()

# Main function
def hangman_game():
    file_name = input()  # Gets the filename
    words = load_words(file_name)  # Gets the list of words
    if not words:
        return

    index = int(input()) - 1  # Gets the location of the word in the list 
    secret_word = words[index] # Locates the desired word in the list
    guessed_letters = []  # Creates a list of guessed letters

    attempt = 1

    while attempt <= 12:
        print(f"Secret word: {display_word(secret_word, guessed_letters)}") # Displays the progress
        print(f"Guess {attempt}/12") # Displays how many attempts are left
        guess = input()

        if guess in secret_word: # Checks if guess is in the secret word
            print(f"Correct letter {guess}!")
            guessed_letters.append(guess)
        else:
            print(f"Incorrect letter {guess}!") # Prints out that the guess is not in the secret word 

        if "-" not in display_word(secret_word, guessed_letters): # Checks if all the words have been guessed
            print(f"Secret word: {display_word(secret_word, guessed_letters)}") # Prints the secret word
            print("You won!")
            return

        attempt += 1 # Updates the attempt counter
    print(f"Secret word: {display_word(secret_word, guessed_letters)}") # Prints out if attemps exceed the limit
    print(f"You lost! The secret word was {secret_word}")

hangman_game() # Starts the game