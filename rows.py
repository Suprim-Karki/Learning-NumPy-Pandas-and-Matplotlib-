''' Working with rows '''

import pandas as pd

''' head and tail functions'''
df=pd.read_json("sample_Data.json")

# print("Displaying first 5 rows")
# print(df.head())    #Can use head(n) n is the number of  rows, default is 5

# print("Displaying last 5 rows")
# print(df.tail())

''' info() method provides:
            1. number of rows and columns
            2. column names
            3. data types
            4. non null counts
            5. memory usage of data frame
'''

print("Displaying the info of data set")
print(df.info())

print("Displaying the descriptive Statistics")
print(df.describe())
