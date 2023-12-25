# inputtið
stop_range = int(input())
num_divisor = int(input())

# 1. Finna og skrifa út allar jákvæðar tveggja stafa heiltölur stranglega minni en stop_range
for num in range(10, stop_range):
    num1 = num % 10  # Tekur og geymir bara seinasta tölustafinn
    num2 = num // 10  # Tekur seinasta tölustafinn út
    num2 = num2 % 10  # Tekur og geymir bara seinasta tölustafinn
    if (num1 + num2) ** 2 == num:  # Chekkar hvort tölustafirnir laggðir saman í öðruveldi er sú sama og num
        print(num)

# 2. Finna og skrifa út allar jákvæðar heiltölur stranglega minni en stop_range sem eiga sér nákvæmlega num_divisors deila.
for num in range(1, stop_range):
    divisor_count = 0  # Búa til teljara fyrir að deila
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_count += 1  # Telja hversu oft talan er deilanleg 
    if divisor_count == num_divisor:
        print(num)