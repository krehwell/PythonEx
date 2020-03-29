import pandas as pd

# print out as the pandas series
brands = pd.read_csv('cars.csv', index_col=0)

#this print does not have any heade above the data
print(brands['brand'])

#this print put the header name brand above the data
print(brands['brand'])

#print two data with header name all together
print(brands[['brand', 'color']])

print(brands[0:4])