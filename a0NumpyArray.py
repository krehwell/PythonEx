# create  2 new list height and weight
height = [69.0, 420.0, 13.0]
weight = [169.0, 4.0, 20.0]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

#calculate the number from both
bmi = np_height / np_height ** 2
print(bmi)

#boolean return of each checked
print(bmi > 23)

#print only observant above 23
print(bmi[bmi > 0.023])