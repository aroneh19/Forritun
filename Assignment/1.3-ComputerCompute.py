from math import *

x1_str = input()
y1_str = input()
x2_str = input()
y2_str = input()
# Convert strings to ints.
x_int = (int(x2_str) - int(x1_str)) ** 2
y_int = (int(y2_str) - int(y1_str)) ** 2

d = sqrt(x_int + y_int)

print(d)