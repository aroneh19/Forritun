def main():
    heimilisverk = []
    num = int(input())

    for i in range(num):
        word = input()
        if word not in heimilisverk:
            heimilisverk.append(word)

    for i in heimilisverk:
        print(i)

if __name__ == '__main__':
    main()