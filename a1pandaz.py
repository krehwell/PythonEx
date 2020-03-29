#make a dictionary for later usage in panda
dictionary = {
    "country": ["brazil", "russia", "india", "china"],
    "capital": ["brasilia", "moscow", "new delhi", "beijing"],
    "population": [420, 69, 13, 88]
}

import pandas as pd 
brics = pd.DataFrame(dictionary)
brics.index = ["br", "ru", "in", "ch"]
print(brics)
