UI = False

# Define a set of punctuation characters to remove
punctuation_chars = {'.', ',', '!', '?', '"', "'", ':', ';', '(', ')', '[', ']', '{', '}', '-', '_'}

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def process_words(text):
    words = text.split()
    processed_words = [word.strip(''.join(punctuation_chars)) for word in words]
    return set(processed_words)

def format_words(words_set):
    words = sorted(words_set)
    if len(words) > 1:
        formatted_words = ", ".join(words[:-1]) + " and " + words[-1]
    else:
        formatted_words = words[0] if words else ""
    return formatted_words

def main():
    filename1 = input("Enter the name of the first file:\n" if UI else "")
    filename2 = input("Enter the name of the second file:\n" if UI else "")

    text1 = read_file(filename1)
    text2 = read_file(filename2)

    words1 = process_words(text1)
    words2 = process_words(text2)

    common_words = words1.intersection(words2)
    unique_words = words1.symmetric_difference(words2)
    exclusive_words1 = words1.difference(words2)

    print(f"The two files have {len(common_words)} words in common.")
    if len(common_words) > 0:
        print("These words are as follows:")
        if format_words(common_words) == "The":
            print(str(format_words(common_words)))
        else:
            print(str(format_words(common_words)) + ".")
    print()
    print(f"There are {len(unique_words)} words that are only in either file but not both.")
    if len(unique_words) > 0:
        print("These words are as follows:")
        print(str(format_words(unique_words)) + ".")
    print()
    print(f"There are {len(exclusive_words1)} words that only appear in the first file.")
    if len(exclusive_words1) > 0:
        print("These words are as follows:")
        print(str(format_words(exclusive_words1)) + ".")

if __name__ == "__main__":
    main()
