street_list = []
street_tuple = []

while True:
    street = input()

    if street == "q":
        break

    street_list.append(street)
    street = street.split(" ")
    street = tuple(street)
    street_tuple.append(street)

print(street_list)
print(street_tuple)