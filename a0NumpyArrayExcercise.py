import numpy as np

#function to convert taking one parameter
def convertKgToPound(kg):
    return kg * 2.2

weight = [420.69, 69.420, 69.69, 420.420]
np_weight = np.array(weight)

kgToPound = convertKgToPound(np_weight)

print(kgToPound)