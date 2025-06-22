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
# print(df['education'].value_counts())

'''Q12: What is the average educational number for each education category?'''
# print(df.groupby('education')['educational-num'].mean().sort_values(ascending=False))

'''Q13: What are the top 5 most common marital statuses?'''
# print(df['marital-status'].value_counts().head(5))

'''Q14: How many unique occupations are present in the dataset?'''
# print(df['occupation'].nunique())

'''Q15: What is the most common combination of race and gender?'''
# print(df.groupby(['race', 'gender']).size().sort_values(ascending=False).head(1))

'''Q16: Show the average age for each workclass.'''
# print(df.groupby('workclass')['age'].mean().sort_values(ascending=False))

'''Q17: Which relationship type has the highest average education level?'''
# print(df.groupby('relationship')['educational-num'].mean().sort_values(ascending=False))

'''Q18: What is the minimum and maximum value of `fnlwgt`?'''
# print("Min fnlwgt:", df['fnlwgt'].min())
# print("Max fnlwgt:", df['fnlwgt'].max())

'''Q19: Count how many entries are missing or marked as '?' in the workclass column.'''
# print((df['workclass'] == '?').sum())

'''Q20: What is the average hours-per-week grouped by income category (<=50K and >50K)?'''
# print(df.groupby('income')['hours-per-week'].mean())

'''Q21: Which education level has the highest percentage of individuals earning >50K?'''
# edu_income = df[df['income'] == '>50K']['education'].value_counts(normalize=True) * 100
# print(edu_income.sort_values(ascending=False))

'''Q22: What is the average age of females vs males?'''
# print(df.groupby('sex')['age'].mean())

'''Q23: How many people are self-employed? (Self-emp-not-inc and Self-emp-inc)'''
# print(df[df['workclass'].isin(['Self-emp-not-inc', 'Self-emp-inc'])].shape[0])

'''Q24: What is the distribution of hours worked per week for people earning >50K vs <=50K?'''
# print(df.groupby('income')['hours-per-week'].describe())

'''Q25: List the 5 most common native countries in the dataset.'''
print(df['native-country'].value_counts().head(5))









































