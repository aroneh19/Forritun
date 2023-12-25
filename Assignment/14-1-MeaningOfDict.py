def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)

def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""
    key = input()
    value = input()
    dictionary[key] = value

def more() -> bool:
    """Checks if the user wants to add more words."""
    yes_or_no = input()
    if yes_or_no == "y":
        return True
    else:
        return False

def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""
    sorted_dict = sorted(dictionary.items())
    for word, definition in sorted_dict:
        print()
        print(word + ":")
        print("    " + definition)
        
if __name__ == "__main__":
    main()
