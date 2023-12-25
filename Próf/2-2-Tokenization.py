def main():
    file = input()
    print_words(file)
    print_tokens(file)

def print_words(filename): # Adds all the words to a list then prints the the length and the list
    try:
        with open(filename, "r") as file:
            list = []
            for line in file:
                split = line.split()
                for i in split:
                    list.append(i)
            print(len(list))
            for i in list:
                print(i)
    except FileNotFoundError:
        quit()
        

def print_tokens(filename): # Checks if there are any tokens removes it from the word and adds to the list
    with open(filename, "r") as file:
        list = []
        for line in file:
            tokens = line.strip().split()
            for token in tokens:
                if "," in token:
                    token = token[:-1]
                    list.append(token)
                    list.append(",")
                elif "!" in token:
                    token = token[:-1]
                    list.append(token)
                    list.append("!")
                elif "?" in token:
                    token = token[:-1]
                    list.append(token)
                    list.append("?")
                elif "." in token:
                    token = token[:-1]
                    list.append(token)
                    list.append(".")
                else:  
                    list.append(token)

        print(len(list))
        for i in list:
            print(i)

if __name__ == "__main__":
    main()