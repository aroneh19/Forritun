number_of_players = int(input())
total = 0
while number_of_players < 2:
    number_of_players = int(input())

for i in range(number_of_players):
    contribute = int(input())
    total += contribute

remainder = total % number_of_players

print(f"The sum of all contributions is {total}")
print(f"When {total} is divided by {number_of_players}, the remainder is {remainder}")
print(f"Player {remainder} is the winner!")