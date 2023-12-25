a = bool(int(input()))
b = bool(int(input()))
c = bool(int(input()))

if a and not b:
    print(1)
elif not a and c:
    print(1)
else:
    print(0)