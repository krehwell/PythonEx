#import panda
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

#print brand colum as pandas series
print(cars['brand'])

#print brand column as panda data frame
print([['brand', 'color']])

#print out from observant
print(cars[0:1])

#print from 3rd row to 5th row
print(cars[3:5])