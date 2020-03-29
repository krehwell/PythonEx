import pandas as pd
brands = pd.read_csv('cars.csv', index_col=0)

#print observation for miamiza, because miamiza is from the number of 2
print(brands.iloc[2])

#print observant from 2 and 3
print(brands.loc[[2, 3]])