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
# print(len(df[df['JobTitle'].str.contains("CAPTAIN",case=False)]))  #case insensative search

'''Q13: Display all the names of employees from the fire department'''
# print(df[df['JobTitle'].str.contains('FIRE DEPARTMENT',case=False)]['EmployeeName'])

'''Q14: Desribe base pay'''
# print(df['BasePay'].describe())

'''Q15: Replace Not provided in employee name to NaN'''
# import numpy as np
# df['EmployeeName']=df['EmployeeName'].replace('Not provided',np.nan)
# print(df)

'''Q16: Show the rows having 3 missing values'''
# print(df.isnull().sum(axis=1)==3)

'''Q17: Show the rows having 3 missing values'''
# print(df.drop(df[df.isnull().sum(axis=1)==3].index,axis=0))

'''Q18: Find the job title of Albert Pardini'''
# print(df[df['EmployeeName']=='ALBERT PARDINI']['JobTitle'])

'''Q19: How much Albert Pardini make including benefits'''
# print(df[df['EmployeeName']=='ALBERT PARDINI']['TotalPayBenefits'])

'''Q20: What is the average BasePay of all employees?'''
df['BasePay'] = pd.to_numeric(df['BasePay'], errors='coerce')
# print(df['BasePay'].mean())

'''Q21: What is the maximum OvertimePay recorded?'''
# print(df['OvertimePay'].max())

'''Q22: Display the employee with the highest TotalPayBenefits.'''
# print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()])

'''Q23: Display the employee with the lowest TotalPayBenefits (excluding 0 or negative).'''
# print(df[df['TotalPayBenefits'] > 0].sort_values(by='TotalPayBenefits').head(1))

'''Q24: Find out how many unique agencies are there in the dataset.'''
# print(df['Agency'].nunique())

'''Q25: Find the average TotalPay for each job title (top 5 by average).'''
# print(df.groupby('JobTitle')['TotalPay'].mean().sort_values(ascending=False).head(5))

'''Q26: What is the most common BasePay value?'''
# print(df['BasePay'].mode()[0])

'''Q27: Display the frequency of TotalPay being exactly zero.'''
# print((df['TotalPay'] == 0).sum())

'''Q28: Show all records where BasePay is missing but OvertimePay is provided.'''
# print(df[df['BasePay'].isnull() & df['OvertimePay'].notnull()])

'''Q29: What is the correlation between BasePay and TotalPay?'''
# print(df[['BasePay', 'TotalPay']].corr())

'''Q30: What is the year with the highest average TotalPayBenefits?'''
# print(df.groupby('Year')['TotalPayBenefits'].mean().sort_values(ascending=False).head(1))

'''Q31: Which job title has the highest median BasePay?'''
# print(df.groupby('JobTitle')['BasePay'].median().sort_values(ascending=False).head(1))

'''Q32: Count how many job titles were represented by only one person in a year (i.e., rare roles).'''
# print(sum(df['JobTitle'].value_counts() == 1))

'''Q33: Find the average OvertimePay for each year.'''
# print(df.groupby('Year')['OvertimePay'].mean())


'''Q34: Find out how many employees have a BasePay above the overall average BasePay.'''
avg_basepay = df['BasePay'].mean()
print((df['BasePay'] > avg_basepay).sum())







