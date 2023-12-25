import random

DECK_CARDS = ['A', 'K', 'Q', 'J', '10', '9', '8', 
              '8', '7', '6', '5', '4', '3', '2']
CARD_VALUES = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, '9': 9, 
               '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
DEALER = 'Dealer'
PLAYER = 'Player'

def main():
    seed = input("Enter a seed: ")
    random.seed(seed)

    dealer_wins, player_wins = 0, 0
    number_of_rounds = int(input("Number of rounds: "))
    
    for round in range(number_of_rounds):
        deck = initialize_deck()
        player_hand = []
        dealer_hand = []
        while get_hand_value(player_hand) < 17 and len(player_hand) < 5:
            player_hand.append(deck.pop())
            if get_hand_value(player_hand) > 21:
                break
        while get_hand_value(dealer_hand) < 17 and len(dealer_hand) < 5:
            dealer_hand.append(deck.pop())

        print_hand(PLAYER, player_hand)
        print_hand(DEALER, dealer_hand)
        winner = get_winner(player_hand, dealer_hand)
        print(f"Winner: {winner}")
        if winner == DEALER:
            dealer_wins += 1
        else:
            player_wins += 1
    
    print(f"Player won {player_wins} times")
    print(f"Dealer won {dealer_wins} times")

def get_winner(player_hand, dealer_hand):
    player_points = get_hand_value(player_hand)
    dealer_points = get_hand_value(dealer_hand)

    if player_points > 21:
        return DEALER
    elif dealer_points > 21:
        return PLAYER
    elif player_points == dealer_points:
        return DEALER
    elif player_points > dealer_points:
        return PLAYER
    else:
        return DEALER

def print_hand(player, hand):
    print(f"{player}: {get_hand_value(hand)} ->", end=" ")
    for card in hand:
        print(f"{card}", end=" ")
    print()

def get_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += CARD_VALUES[card]
    return hand_value

def initialize_deck() -> list:
    shuffled_deck = DECK_CARDS*4
    random.shuffle(shuffled_deck)
    return shuffled_deck

if __name__ == '__main__':
    main()