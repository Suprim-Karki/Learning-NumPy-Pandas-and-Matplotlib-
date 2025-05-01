''' Working with rows '''

import pandas as pd

''' head and tail functions'''
df=pd.read_json("sample_Data.json")

print("Displaying first 5 rows")
print(df.head())    #Can use head(n) n is the number of  rows, default is 5

print("Displaying last 5 rows")
print(df.tail())

