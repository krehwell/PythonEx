import pandas as pd

brands = pd.read_csv('cars.csv', index_col=0)

#print base on its index number on cell
print(brands.iloc[3])

#print base on the name it searched
print(brands.loc[3])

