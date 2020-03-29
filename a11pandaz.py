dict = {
    "country": ["brazil", "china", "denmark"],
    "capital": ["brasil", "beijing", "whatever"],
    "population":[200, 300, 400]
}

import pandas as pd

nation = pd.DataFrame(dict)
print(nation)

nation.index = ["br", "ch", "dm"]

print(nation)