from typing import List

def main():
    throw = None

    while throw != "":
        throw = input() # input of all the throws
        if throw == "":
            break

        list_of_throw = throw.split() # List of throws

        counts = get_counts(list_of_throw)
        most_frequent, highest_average = calculate_count(counts)
        print_points(most_frequent, highest_average)


def get_counts(dice_results: List[int]) -> List[int]: # Checks how many times the dice rolled on x
    counts = [0, 0, 0, 0, 0, 0] # Empty list
    
    for dice in dice_results:
        counts[int(dice) - 1] += 1 # counter
    
    return counts

def calculate_count(counts: list[int]): # Calculates the dice the most frequent dice and the value
    most_frequent = 0

    for num, count in enumerate(counts, 1): # Loop through the list
        if count >= most_frequent: # checks if the count is more than the dice before
            most_frequent = count
            highest_num = num
    
    return most_frequent, highest_num # Returns what dice was the most frequent and the value of the dice
    
def print_points(most_frequent, highest_num): # Prints how many points the user gets
    if most_frequent == 5: # YATZY
        print(50)    
    elif most_frequent == 4: # Four of a kind
        highest_num *= 3
        print(highest_num)
    elif most_frequent > 1: # Pair or Three of a kind
        most_frequent *= highest_num
        print(most_frequent)
    else: # All dices have different values
        print(0)

if __name__ == "__main__":
    main()
