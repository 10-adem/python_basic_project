
#Given two integer values, return their sum. If the two values are the same, then return double their sum.

def sum_double(x, y):
    return ((lambda x, y : (x + y) if x != y else (x + y)*2) (x, y))

print(sum_double(1, 2)) result ==> 3
print(sum_double(5, 7)) result ==> 12
print(sum_double(5, 5)) result ==> 20

