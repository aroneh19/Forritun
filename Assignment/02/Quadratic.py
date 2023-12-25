
val_a_int = int(input())
val_b_int = int(input())
val_c_int = int(input())
# Fill in the missing code below

d = val_b_int ** 2 - (4 * val_a_int * val_c_int)

if d > 0:
    print(2)
elif d == 0:
    print(1)
elif d < 0:
    print(0)