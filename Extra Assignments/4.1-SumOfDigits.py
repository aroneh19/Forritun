result = 0
n = int(input())

while n > 0:
    result +=  (n % 10)
    n = n // 10
print(result)