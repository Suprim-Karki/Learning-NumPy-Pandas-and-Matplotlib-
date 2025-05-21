import pandas as pd

df = pd.read_csv("Salaries.csv",low_memory=False)

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
# print(df['EmployeeName'].value_counts().head(10))

'''Q9: Find the occurance of Job Title. Top 5.'''
# print(df['JobTitle'].value_counts().head())

'''Q10: Find the number of unique job titles'''
# print(df['JobTitle'].nunique())

'''Q11: Total number of job titles that contain captain (case sensative)'''
# print(len(df[df['JobTitle'].str.contains("CAPTAIN")]))  #case sensative search

'''Q12: Total number of job titles that contain captain (case sensative)'''
print(len(df[df['JobTitle'].str.contains("CAPTAIN",case=False)]))  #case insensative search






















