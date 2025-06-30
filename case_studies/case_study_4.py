import pandas as pd

# Load the dataset
df = pd.read_csv("googleplaystore.csv")

'''Q1: Display the first 10 rows of the dataset.'''
# print(df.head(10))

'''Q2: What are the column names and how many are there?'''
print(df.columns)
print("Total columns:", len(df.columns))