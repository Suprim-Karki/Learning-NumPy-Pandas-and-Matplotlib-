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

''' Shape and columns '''

print("Printing shape and columns")
print(f"Shape: {df.shape}")             #gives (rows,columns)
print(f"Shape: {df.columns}")           #gives column names



''' Selecting a column '''
#Selecting single column
#variable=daraframe_name[column_name]

name=df['name'] 
print(name)

#selecting multiple columns
subset=df[['id','name']]
print(subset)

'''Filtering'''

#single filtering condition
high_price=df[df['price']>500]
print(high_price)

#multiple filtering conditions
filtered=df[(df['price']>500) & (df['id']>10)]
print(filtered)


















