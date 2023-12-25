
n = int(input())
i = n - 1

if n == 1:
    print("not prime")
else:
    while i > 1:
        if n % i == 0:
            print("not prime")
            break
        else:
            i -= 1
    else:
        print("prime")