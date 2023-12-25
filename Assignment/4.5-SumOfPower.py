k = int(input())
n = int(input())
the_sum = 0

for i in range(n):
    x = int(input())
    the_sum += k ** x
print(the_sum)