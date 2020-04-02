# filter requires a function to filtering
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def scoreGreaterThan(num):
    return num > 75


over_75 = list(filter(scoreGreaterThan, scores))
print(over_75)


# another example on how to use filter for palindromes
# palindromes is the same words when we read it backwards
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)
