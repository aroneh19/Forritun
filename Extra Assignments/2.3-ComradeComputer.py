
temp_now = int(input())
temp_prev = int(input())

if temp_now < 300 and temp_now <= temp_prev:
    print("raise")
elif temp_now >= 350:
    print("shutdown")
elif temp_now < 300 and temp_now > temp_prev:
    print("keep")
elif temp_now == 300:
    print("keep")
elif temp_now > 300 and temp_now >= temp_prev:
    print("lower")
elif temp_now > 300 and temp_now < temp_prev:
    print("keep")