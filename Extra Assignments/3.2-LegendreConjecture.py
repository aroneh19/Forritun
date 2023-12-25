
n = int(input())

print(f"Primes in the range {n ** 2} and {(n+1) ** 2} are:")

for i in range(n**2, (n+1) ** 2):
    if i > 1:
        for x in range(2, int(i/2)+1):
            if i % x == 0:
                break
        else:
            print(i)