# traditional way of on make the words to upper
my_pets = ['alfred', 'tabitha', 'william', 'arla']
upper_pets = []

for pet in my_pets:
    b = pet.upper()
    # use capitalize() function to capitalize the first char
    upper_pets.append(b)

print(upper_pets)


# instead using map() we can use
family = ['yuza', 'adza', 'fauza', 'teza']
upper_family = list(map(str.upper, family))
print(upper_family)

# another example of on how easy to use map
cirle = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, cirle, range(0, len(cirle))))
print(result)


# using list python 3
myString = ['a', 'b', 'c', 'd', 'e']
myNumbers = [1, 2, 3, 4, 5]

result = list(zip(myString, myNumbers))

secResult = list(map(lambda x, y: (y, x), myString, myNumbers))

print(type(result))
print(result)

print(secResult)
