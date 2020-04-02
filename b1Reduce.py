# pytohn 3 tho
from functools import reduce

number = [3, 4, 6, 9, 34, 12]


def customSum(first, second):
    return first + second


result = reduce(customSum, number, 10)
print(result)
