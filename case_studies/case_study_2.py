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
# print(df.isnull().sum())

'''Q6: Drop Id, Notes, Agency and Status columns from the dataset.'''
# data = df.drop(['Id', 'Notes', 'Agency', 'Status'],axis=1)
# print(data)

'''Q7: Get overall statistics of the dataset.'''
# print(df.describe())

'''Q8: Find the occurance of Employee Name. Top 10.'''
print(df['EmployeeName'].value_counts().head(10))

























