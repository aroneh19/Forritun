mb_per_month = int(input())
n = int(input())

mb_per_month *= (n + 1)

for i in range(n):
    usage = int(input())
    mb_per_month -= usage
print(mb_per_month)