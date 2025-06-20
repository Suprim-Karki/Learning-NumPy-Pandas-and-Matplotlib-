import pandas as pd

df = pd.read_csv("adult.csv", encoding='latin1', sep=',', engine='python', error_bad_lines=False)


'''Q1: Display the first 10 rows of the dataset.'''
# print(df.head(10))

'''Q2: What are the column names and how many are there?'''
# print(df.columns)
# print("Total columns:", len(df.columns))

'''Q3: Display the number of rows and columns (shape).'''
# print(df.shape)

'''Q4: Count how many entries fall in each income category (<=50K or >50K).'''
print(df['income'].value_counts())
