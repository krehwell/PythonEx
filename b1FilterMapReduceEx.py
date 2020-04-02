from functools import reduce

# use map to print the squre of each number rounded
# to two decimal places
myFloats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# use filter to print only the names that are less than
# or equal to seven letters
myNames = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# use reduce to print the product of these numbers
myNumber = [4, 6, 9, 23, 5]

# fix all three respectively

mapResult = list(map(lambda x: round(x)**2, myFloats))

filterResult = list(filter(lambda name: len(name) == 7, myNames))

reduceResult = reduce(lambda num1, num2: num1 * num2, myNumber, 1)

# print all of them
print(mapResult)
print(filterResult)
print(reduceResult)
