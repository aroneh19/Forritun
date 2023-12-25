n = int(input())

a, b, c = 1, 2, 3

if n >= 1:
    print(a)
if n >= 2:
    print(b)
if n >= 3:
    print(c)

for i in range(4, n+1):
    result = a + b + c
    print(result)
    a = b
    b = c
    c = result
