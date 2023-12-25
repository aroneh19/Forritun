import string


def main():
    filename = input()
    file_object = get_open_file(filename)
    list_of_files = get_all_files(file_object)
    file_dict = file_dictionary(list_of_files)
    word_dict = word_dictionary(list_of_files)
    while True:
        action = input().lower()
        if action == "search":
            search = input().lower().split()
            all = None
            for i in search:
                if i in word_dict:
                    if all is None:
                        all = word_dict[i]
                    else:
                        all = all & word_dict[i]
                else:
                    all = set()

            if all:
                all_sort = sorted(all)
                print("Documents matching search:", end=" ")
                print(*all_sort)
            else:
                print("No match")
        elif action == "print":
            file = int(input())
            if file in file_dict:
                print(f"document #{file}:")
                print(f"{(file_dict[file])}")
            else:
                print("No match")
        elif action == "quit":
            break
        else:
            continue

def get_open_file(filename):
    try:
        with open(filename, "r") as file:
            file_object = file.read()
    except FileNotFoundError:
        quit()
    return file_object

def get_all_files(file_object):
    delimeter = "<END OF DOCUMENT>"
    list_of_files = file_object.split(delimeter)
    return list_of_files

def file_dictionary(list_of_files):
    file_dict = dict()
    for i in range(len(list_of_files)-1):
            file_dict[i+1] = list_of_files[i]

    return file_dict

def word_dictionary(list_of_files):
    word_dict = {}
    for i, document in enumerate(list_of_files):
        words = [word.lower().strip(string.punctuation) for word in document.split()]
        for word in words:
            if word:
                if word not in word_dict:
                    word_dict[word] = set()
                word_dict[word].add(i + 1)
    return word_dict

if __name__ == "__main__":
    main()