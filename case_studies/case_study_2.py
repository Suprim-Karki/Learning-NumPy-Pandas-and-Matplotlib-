import pandas as pd

df = pd.read_csv("Salaries.csv")

'''Q1: Display top 10 rows of the dataset.'''
# print(df.head(10))

'''Q2: Display bottom 10 rows of the dataset.'''
# print(df.tail(10))

'''Q3: Display the shape of the dataset.'''
# print(df.shape)

'''Q4: Display all information about the dataset.'''
# print(df.info())

'''Q5: Check for null values in the dataset.'''
print(df.isnull().sum())

























