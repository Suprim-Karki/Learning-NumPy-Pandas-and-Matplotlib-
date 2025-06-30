import pandas as pd

# Load the dataset
df = pd.read_csv("googleplaystore.csv")

'''Q1: Display the first 10 rows of the dataset.'''
# print(df.head(10))

'''Q2: What are the column names and how many are there?'''
# print(df.columns)
# print("Total columns:", len(df.columns))

'''Q3: What is the shape of the dataset (rows and columns)?'''
# print(df.shape)

'''Q4: How many unique app categories are there?'''
# print(df['Category'].nunique())

'''Q5: What are the top 5 most common app categories?'''
# print(df['Category'].value_counts().head(5))

'''Q6: What is the average app rating?'''
# print(df['Rating'].mean())

'''Q7: How many apps have a rating above 4.5?'''
print((df['Rating'] > 4.5).sum())
