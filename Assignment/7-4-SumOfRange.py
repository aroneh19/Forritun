def sum_of_range(start, end, step):
    result = 0
    for i in range(int(((end-start)/step)+1)):
        result += start + i * step
    return result
# print(sum_of_range(1, 10, 2))