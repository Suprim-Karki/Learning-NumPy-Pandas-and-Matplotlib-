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
# avg_basepay = df['BasePay'].mean()
# print((df['BasePay'] > avg_basepay).sum())

'''Q35: What percentage of employees earned more in OvertimePay than in BasePay?'''
# print((df['OvertimePay'] > df['BasePay']).mean() * 100)

'''Q36: List all unique job titles containing the word "Manager".'''
# print(df[df['JobTitle'].str.contains('Manager', case=False)]['JobTitle'].unique())

'''Q37: Which employee has the highest OvertimePay?'''
# print(df[df['OvertimePay'] == df['OvertimePay'].max()][['EmployeeName', 'OvertimePay']])

'''Q38: What is the distribution of employees across different years?'''
# print(df['Year'].value_counts().sort_index())

'''Q39: Among the employees with missing BasePay, what is the average TotalPayBenefits?'''
# print(df[df['BasePay'].isnull()]['TotalPayBenefits'].mean())

'''Q40: What is the average TotalPayBenefits for each year?'''
# print(df.groupby('Year')['TotalPayBenefits'].mean())

'''Q41: Which agency has the highest average TotalPay?'''
# print(df.groupby('Agency')['TotalPay'].mean().sort_values(ascending=False).head(1))

'''Q42: How many employees have negative TotalPayBenefits?'''
# print((df['TotalPayBenefits'] < 0).sum())

'''Q43: What is the standard deviation of BasePay by year?'''
# print(df.groupby('Year')['BasePay'].std())

'''Q44: What percentage of employees have TotalPayBenefits greater than the mean + 2 standard deviations?'''
# mean = df['TotalPayBenefits'].mean()
# std = df['TotalPayBenefits'].std()
# print((df['TotalPayBenefits'] > mean + 2*std).mean() * 100)

'''Q45: Which job title has the highest average OvertimePay?'''
# print(df.groupby('JobTitle')['OvertimePay'].mean().sort_values(ascending=False).head(1))

'''Q46: How many records have all pay-related fields (BasePay, OvertimePay, OtherPay) as NaN?'''
# print(df[['BasePay', 'OvertimePay', 'OtherPay']].isnull().all(axis=1).sum())

'''Q47: What is the median TotalPayBenefits by year?'''
# print(df.groupby('Year')['TotalPayBenefits'].median())

'''Q48: Are there any duplicate records in the dataset?'''
# print(df.duplicated().sum())

'''Q49: What is the correlation matrix for all numeric columns?'''
# print(df.corr(numeric_only=True))

'''Q50: Find the total compensation (BasePay + OvertimePay + OtherPay) for each employee.'''
# df['TotalCompensation'] = df[['BasePay', 'OvertimePay', 'OtherPay']].sum(axis=1)
# print(df[['EmployeeName', 'TotalCompensation']])

'''Q51: Which year had the greatest number of records?'''
# print(df['Year'].value_counts().idxmax())

'''Q52: List all job titles that include both "Deputy" and "Director".'''
# print(df[df['JobTitle'].str.contains('Deputy', case=False) & df['JobTitle'].str.contains('Director', case=False)]['JobTitle'].unique())

'''Q53: Find the number of employees whose TotalPay is exactly equal to BasePay.'''
# print((df['TotalPay'] == df['BasePay']).sum())

'''Q54: Identify any records where TotalPay is less than BasePay (possible data issue).'''
# print(df[df['TotalPay'] < df['BasePay']])

'''Q55: What are the top 5 most frequent employee first names?'''
# df['FirstName'] = df['EmployeeName'].str.split().str[0]
# print(df['FirstName'].value_counts().head(5))

'''Q56: What is the average OtherPay for employees whose BasePay is above $100,000?'''
# print(df[df['BasePay'] > 100000]['OtherPay'].mean())

'''Q57: Find the number of unique combinations of JobTitle and Year.'''
# print(df.groupby(['JobTitle', 'Year']).ngroups)

'''Q58: What is the maximum TotalPay recorded each year?'''
# print(df.groupby('Year')['TotalPay'].max())

'''Q59: How many employees have a name that includes "LEE"?'''
# print(df['EmployeeName'].str.contains('LEE', case=False).sum())

'''Q60: What percentage of total BasePay was contributed by the top 10 highest-paid employees?'''
# top_10_total = df.nlargest(10, 'BasePay')['BasePay'].sum()
# overall_total = df['BasePay'].sum()
# print((top_10_total / overall_total) * 100)

'''Q61: Which JobTitle has the highest total compensation (BasePay + OvertimePay + OtherPay)?'''
# df['TotalComp'] = df[['BasePay', 'OvertimePay', 'OtherPay']].sum(axis=1)
# print(df.groupby('JobTitle')['TotalComp'].sum().sort_values(ascending=False).head(1))

'''Q62: Identify top 5 job titles with the most missing BasePay entries.'''
# print(df[df['BasePay'].isnull()]['JobTitle'].value_counts().head(5))

'''Q63: Create a pivot table showing average TotalPay by Year and Agency.'''
# print(pd.pivot_table(df, values='TotalPay', index='Year', columns='Agency', aggfunc='mean'))

'''Q64: What is the median OtherPay for each job title? Show top 5.'''
# print(df.groupby('JobTitle')['OtherPay'].median().sort_values(ascending=False).head(5))

'''Q65: List all job titles where median BasePay is greater than $150,000.'''
# print(df.groupby('JobTitle')['BasePay'].median().loc[lambda x: x > 150000])

'''Q66: How does the average TotalPay differ between years for the job title "Police Officer"?'''
# print(df[df['JobTitle'].str.contains('Police Officer', case=False)].groupby('Year')['TotalPay'].mean())

'''Q67: Identify top 3 agencies with the highest median TotalPay in 2014.'''
# print(df[df['Year'] == 2014].groupby('Agency')['TotalPay'].median().sort_values(ascending=False).head(3))

'''Q68: How many job titles contain numerals (like 'II', '3', etc.)?'''
import re
# print(df['JobTitle'].apply(lambda x: bool(re.search(r'\d|[IVXLCDM]+', str(x)))).sum())

'''Q69: Compare average BasePay of employees with and without "Manager" in their job title.'''
# manager_avg = df[df['JobTitle'].str.contains('Manager', case=False)]['BasePay'].mean()
# non_manager_avg = df[~df['JobTitle'].str.contains('Manager', case=False)]['BasePay'].mean()
# print(manager_avg, non_manager_avg)

'''Q70: What is the trend of average BasePay over the years?'''
# print(df.groupby('Year')['BasePay'].mean())

'''Q71: Which job titles have the highest average pay volatility (std deviation of TotalPay)? Top 5'''
# print(df.groupby('JobTitle')['TotalPay'].std().sort_values(ascending=False).head(5))

'''Q72: Which department (Agency) has the most job title diversity?'''
# print(df.groupby('Agency')['JobTitle'].nunique().sort_values(ascending=False).head(1))

'''Q73: Find the average TotalPayBenefits for employees whose names contain "SMITH" (case-insensitive).'''
# print(df[df['EmployeeName'].str.contains('SMITH', case=False)]['TotalPayBenefits'].mean())

'''Q74: Compare median BasePay by gender if gender could be inferred from first names.'''
# import gender_guesser.detector as gender
# d = gender.Detector()
# df['FirstName'] = df['EmployeeName'].str.split().str[0]
# df['Gender'] = df['FirstName'].apply(lambda x: d.get_gender(x) if pd.notnull(x) else 'unknown')
# print(df.groupby('Gender')['BasePay'].median())

'''Q75: How many employees have consistent BasePay over all years (if an employee appears in multiple years)?'''
# print(df.groupby('EmployeeName')['BasePay'].nunique().value_counts().get(1, 0))

'''Q76: Show the 5 job titles with the most frequent appearance across multiple years.'''
# print(df.groupby('JobTitle')['Year'].nunique().sort_values(ascending=False).head(5))

'''Q77: Which JobTitle has the largest gap between mean and median BasePay (pay inequality)?'''
# stats = df.groupby('JobTitle')['BasePay'].agg(['mean', 'median'])
# stats['gap'] = stats['mean'] - stats['median']
# print(stats.sort_values('gap', ascending=False).head(5))

'''Q78: What is the average TotalPay of employees with over 10 years of repeated appearance (i.e., loyalty)?'''
# multi_year = df['EmployeeName'].value_counts()
# loyal_employees = multi_year[multi_year > 10].index
# print(df[df['EmployeeName'].isin(loyal_employees)]['TotalPay'].mean())

'''Q79: What percentage of total salary (BasePay) was paid to the top 1% of earners?'''
# threshold = df['BasePay'].quantile(0.99)
# top_1_total = df[df['BasePay'] >= threshold]['BasePay'].sum()
# overall_total = df['BasePay'].sum()
# print((top_1_total / overall_total) * 100)

'''Q80: What percentage of employees earned below the median BasePay?'''
median = df['BasePay'].median()
below_median_count = (df['BasePay'] < median).sum()
total_count = df['BasePay'].count()
print((below_median_count / total_count) * 100)



