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
# print(df['income'].value_counts())

'''Q5: What is the average age of people in the dataset?'''
# print(df['age'].mean())

'''Q6: Find the top 5 most common occupations.'''
# print(df['occupation'].value_counts().head(5))

'''Q7: What is the maximum number of hours worked per week?'''
# print(df['hours-per-week'].max())

'''Q8: How many people work more than 60 hours per week?'''
# print((df['hours-per-week'] > 60).sum())

'''Q9: What percentage of individuals earning >50K are female?'''
# print((df[(df['sex'] == 'Female') & (df['income'] == '>50K')].shape[0] /
#        df[df['income'] == '>50K'].shape[0]) * 100)

'''Q10: What is the gender distribution within each occupation?'''
# print(df.groupby(['occupation', 'gender']).size().unstack(fill_value=0))

'''Q11: What is the distribution of education levels in the dataset?'''
print(df['education'].value_counts())








































