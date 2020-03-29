sentence = "the quick brown fox jump over the lazy dog"

# split the sentence into word by word
words = sentence.split()

words_lengths = []

# here i save the number of length of each word using traditional way
'''
for word in words:
    if word != "the":
        words_lengths.append(len(word))
'''

# here using the list comprehension
words_lengths = [len(word) for word in words if word != "the"]


print(words)
print(words_lengths)
