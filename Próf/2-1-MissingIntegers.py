def main():
    list = input().split()
    print_list(list)
    convert_list(list)

def print_list(list): # Prentar út listann
    print(list)

def convert_list(list): # Checkar hvort eintakið í listanum sé heiltala og bætir það við í nýjum lista
    integer_list = []
    maximum_integer = 0
    for i in list:
        try:
            i = int(i)
            integer_list.append(i)
            if i > maximum_integer: # Checkar fyrir hæstu tölunni í listanum
                maximum_integer = i
        except ValueError:
            continue
    print(integer_list) # Prentar út lista bara með heiltölum

    missing_integer = []

    for i in range(maximum_integer): # Checkar hvaða tölur eru á milli 0 og maxinu eru ekki í listanum
        if i not in integer_list:
            missing_integer.append(i)

    print(missing_integer) # Prentar út allar heiltölur sem eru ekki í listanum

if __name__ == "__main__":
    main()