def main():
    p1 = 301
    p2 = 301

    while p1 > 0 and p2 > 0:
        try:
            p1_throw = input("Input points for Player 1: ")
            if p1_throw == "":
                break
            p1_throw = int(p1_throw)

            if p1_throw <= p1:
                p1 -= p1_throw
                print(f"Player 1 remaining points: {p1}")

            else:
                print("Invalid input!")

            if p1 == 0:
                print("Player 1 won!")
                break

            p2_throw = input("Input points for Player 2: ")
            if p2_throw == "":
                break
            p2_throw = int(p2_throw)

            if p2_throw <= p2:
                p2 -= p2_throw
                print(f"Player 2 remaining points: {p2}")

            else:
                print("Invalid input!")

            if p2 == 0:
                print("Player 2 won!")
                break

        except ValueError:
            print("Invalid input!")

        except EOFError:
            print("Invalid input!")


if __name__ == "__main__":
    main()
