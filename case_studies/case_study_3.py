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
# print(df['native-country'].value_counts().head(5))

'''Q26: What is the average hours worked per week for each occupation?'''
# print(df.groupby('occupation')['hours-per-week'].mean().sort_values(ascending=False))

'''Q27: Which occupation has the highest proportion of people earning >50K?'''
# occupation_income = df[df['income'] == '>50K']['occupation'].value_counts() / df['occupation'].value_counts()
# print(occupation_income.dropna().sort_values(ascending=False).head(5))

'''Q28: How does average education number vary across different races?'''
# print(df.groupby('race')['educational-num'].mean().sort_values(ascending=False))

'''Q29: What is the most common workclass for people under the age of 30?'''
# print(df[df['age'] < 30]['workclass'].value_counts().head(1))

'''Q30: Among those who work the maximum hours per week, what percentage earn >50K?'''
# max_hours = df['hours-per-week'].max()
# over_50k = df[(df['hours-per-week'] == max_hours) & (df['income'] == '>50K')].shape[0]
# total = df[df['hours-per-week'] == max_hours].shape[0]
# print((over_50k / total) * 100 if total else 0)

'''Q31: What is the average age of individuals with a Bachelor's degree?'''
# print(df[df['education'] == 'Bachelors']['age'].mean())

'''Q32: Which native country has the highest average income (>50K percentage)?'''
# country_income = df[df['income'] == '>50K']['native-country'].value_co/

'''Q32: Which native country has the highest average income (>50K percentage)?'''
# country_income = df[df['income'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
# print(country_income.dropna().sort_values(ascending=False).head(5))

'''Q33: How does average age vary by marital status?'''
# print(df.groupby('marital-status')['age'].mean().sort_values(ascending=False))

'''Q34: What is the distribution of relationship types among people earning >50K?'''
# print(df[df['income'] == '>50K']['relationship'].value_counts())

'''Q35: What is the most common occupation for people aged between 25 and 40?'''
# print(df[(df['age'] >= 25) & (df['age'] <= 40)]['occupation'].value_counts().head(1))

'''Q36: What is the average fnlwgt for each education level?'''
# print(df.groupby('education')['fnlwgt'].mean().sort_values(ascending=False))

'''Q37: How many individuals are both divorced and earning <=50K?'''
# print(df[(df['marital-status'] == 'Divorced') & (df['income'] == '<=50K')].shape[0])

'''Q38: What percentage of government workers (workclass starts with "Gov") earn >50K?'''
# gov_workers = df[df['workclass'].str.startswith('Gov')]
# print((gov_workers[gov_workers['income'] == '>50K'].shape[0] / gov_workers.shape[0]) * 100 if gov_workers.shape[0] else 0)

'''Q39: Among people with Doctorate degrees, what is the most common occupation?'''
# print(df[df['education'] == 'Doctorate']['occupation'].value_counts().head(1))

'''Q40: How does income level relate to marital status? (i.e., count of income groups per marital status)'''
# print(df.groupby(['marital-status', 'income']).size().unstack())

'''Q41: What is the average number of hours worked per week by education level?'''
# print(df.groupby('education')['hours-per-week'].mean().sort_values(ascending=False))

'''Q42: Among married individuals, what percentage earn >50K?'''
# married = df[df['marital-status'].str.contains('Married')]
# percentage = (married[married['income'] == '>50K'].shape[0] / married.shape[0]) * 100
# print(percentage)

'''Q43: What are the top 3 occupations for females earning >50K?'''
# print(df[(df['sex'] == 'Female') & (df['income'] == '>50K')]['occupation'].value_counts().head(3))

'''Q44: What is the distribution of people by age group (e.g., 18-25, 26-35, etc.)?'''
# bins = [17, 25, 35, 45, 55, 65, 100]
# labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '66+']
# df['age-group'] = pd.cut(df['age'], bins=bins, labels=labels)
# print(df['age-group'].value_counts().sort_index())

'''Q45: Which race has the highest percentage of individuals earning >50K?'''
# race_income = df[df['income'] == '>50K']['race'].value_counts() / df['race'].value_counts()
# print(race_income.dropna().sort_values(ascending=False))

'''Q46: What percentage of individuals with only HS-grad education earn >50K?'''
# hs = df[df['education'] == 'HS-grad']
# percentage = (hs[hs['income'] == '>50K'].shape[0] / hs.shape[0]) * 100
# print(percentage)

'''Q47: What is the most common workclass among individuals aged 60 and above?'''
# print(df[df['age'] >= 60]['workclass'].value_counts().head(1))

'''Q48: Compare average hours worked per week for people from the US vs non-US countries.'''
# us = df[df['native-country'] == 'United-States']['hours-per-week'].mean()
# non_us = df[df['native-country'] != 'United-States']['hours-per-week'].mean()
# print("US:", us, "Non-US:", non_us)

'''Q49: What is the average age of individuals who never married?'''
# print(df[df['marital-status'] == 'Never-married']['age'].mean())

'''Q50: Among individuals earning >50K, what are the top 3 native countries (excluding US)?'''
# print(df[(df['income'] == '>50K') & (df['native-country'] != 'United-States')]['native-country'].value_counts().head(3))

'''Q51: What is the average age of individuals with income <=50K vs >50K?'''
# print(df.groupby('income')['age'].mean())

'''Q52: Which education level has the highest average hours-per-week?'''
# print(df.groupby('education')['hours-per-week'].mean().sort_values(ascending=False).head(1))

'''Q53: How many females are employed in the private sector?'''
# print(df[(df['sex'] == 'Female') & (df['workclass'] == 'Private')].shape[0])

'''Q54: What is the income distribution across different age groups?'''
# print(df.groupby('age-group')['income'].value_counts(normalize=True).unstack().fillna(0) * 100)

'''Q55: Among people working more than 50 hours per week, which occupation is most common?'''
# print(df[df['hours-per-week'] > 50]['occupation'].value_counts().head(1))

'''Q56: What is the gender ratio (Male to Female) in the dataset?'''
# males = df[df['sex'] == 'Male'].shape[0]
# females = df[df['sex'] == 'Female'].shape[0]
# print("Male to Female ratio:", males / females if females else 'Undefined')

'''Q57: What is the most common marital status among people aged 30 to 50?'''
# print(df[(df['age'] >= 30) & (df['age'] <= 50)]['marital-status'].value_counts().head(1))

'''Q58: What percentage of people with capital gain > 0 earn >50K?'''
# gainers = df[df['capital-gain'] > 0]
# print((gainers[gainers['income'] == '>50K'].shape[0] / gainers.shape[0]) * 100 if gainers.shape[0] else 0)

'''Q59: What is the average capital loss grouped by education level?'''
# print(df.groupby('education')['capital-loss'].mean().sort_values(ascending=False))

'''Q60: Which occupation has the highest average age?'''
# print(df.groupby('occupation')['age'].mean().sort_values(ascending=False).head(1))

'''Q61: What is the most common native country among females?'''
# print(df[df['sex'] == 'Female']['native-country'].value_counts().head(1))

'''Q62: Among people with a Master's degree, what is the average number of hours worked per week?'''
# print(df[df['education'] == 'Masters']['hours-per-week'].mean())

'''Q63: How many people have a capital loss greater than 1000?'''
# print((df['capital-loss'] > 1000).sum())

'''Q64: What is the most common relationship status among those aged under 25?'''
# print(df[df['age'] < 25]['relationship'].value_counts().head(1))

'''Q65: What is the total number of unique native countries represented in the dataset?'''
# print(df['native-country'].nunique())

'''Q66: Among people earning <=50K, which workclass is most represented?'''
# print(df[df['income'] == '<=50K']['workclass'].value_counts().head(1))

'''Q67: How many people are both widowed and above age 60?'''
# print(df[(df['marital-status'] == 'Widowed') & (df['age'] > 60)].shape[0])

'''Q68: What is the distribution of income by education level?'''
# print(df.groupby('education')['income'].value_counts(normalize=True).unstack().fillna(0) * 100)

'''Q69: Which gender has the higher average capital gain?'''
# print(df.groupby('sex')['capital-gain'].mean())

'''Q70: Among people working part-time (<30 hours/week), what is the most common occupation?'''
# print(df[df['hours-per-week'] < 30]['occupation'].value_counts().head(1))

'''Q71: What is the most common race among individuals earning >50K?'''
# print(df[df['income'] == '>50K']['race'].value_counts().head(1))

'''Q72: What percentage of people earning <=50K are from non-US countries?'''
# non_us = df[(df['income'] == '<=50K') & (df['native-country'] != 'United-States')]
# total = df[df['income'] == '<=50K']
# print((non_us.shape[0] / total.shape[0]) * 100 if total.shape[0] else 0)

'''Q73: What is the average educational number for people aged 50 and above?'''
# print(df[df['age'] >= 50]['educational-num'].mean())

'''Q74: Among people with zero capital gain, what is the average age?'''
# print(df[df['capital-gain'] == 0]['age'].mean())

'''Q75: How many individuals are both Female and Never-married?'''
# print(df[(df['sex'] == 'Female') & (df['marital-status'] == 'Never-married')].shape[0])

'''Q76: Which age group has the highest percentage of individuals earning >50K?'''
# print(df.groupby('age-group')['income'].value_counts(normalize=True).unstack().fillna(0)['>50K'].sort_values(ascending=False).head(1))

'''Q77: What is the average number of hours worked by people with different relationship statuses?'''
# print(df.groupby('relationship')['hours-per-week'].mean().sort_values(ascending=False))

'''Q78: Among people earning >50K, what is the most common education level?'''
# print(df[df['income'] == '>50K']['education'].value_counts().head(1))

'''Q79: What is the total number of people who are either separated or widowed?'''
# print(df[df['marital-status'].isin(['Separated', 'Widowed'])].shape[0])

'''Q80: Among those aged between 18 and 30, what is the gender distribution?'''
# print(df[(df['age'] >= 18) & (df['age'] <= 30)]['sex'].value_counts())

'''Q81: What percentage of individuals over age 40 have a Bachelor's degree?'''
# over_40 = df[df['age'] > 40]
# percentage = (over_40[over_40['education'] == 'Bachelors'].shape[0] / over_40.shape[0]) * 100
# print(percentage)

'''Q82: What is the most common workclass for individuals with a Doctorate?'''
# print(df[df['education'] == 'Doctorate']['workclass'].value_counts().head(1))

'''Q83: Among people working more than 70 hours/week, how many are earning <=50K?'''
# print(df[(df['hours-per-week'] > 70) & (df['income'] == '<=50K')].shape[0])

'''Q84: What is the median age for each marital status group?'''
# print(df.groupby('marital-status')['age'].median().sort_values(ascending=False))

'''Q85: What percentage of individuals with capital-loss > 0 are retired (relationship = Not-in-family or Other-relative)?'''
# cap_loss = df[df['capital-loss'] > 0]
# retired = cap_loss[cap_loss['relationship'].isin(['Not-in-family', 'Other-relative'])]
# print((retired.shape[0] / cap_loss.shape[0]) * 100 if cap_loss.shape[0] else 0)

'''Q86: Among individuals with 'Assoc-acdm' education, what is the average income in hours-per-week?'''
# print(df[df['education'] == 'Assoc-acdm'].groupby('income')['hours-per-week'].mean())

'''Q87: What is the most common occupation among people from India?'''
# print(df[df['native-country'] == 'India']['occupation'].value_counts().head(1))

'''Q88: Among divorced individuals, what is the gender distribution?'''
# print(df[df['marital-status'] == 'Divorced']['sex'].value_counts())

'''Q89: How many people with capital-gain > 5000 work in the private sector?'''
# print(df[(df['capital-gain'] > 5000) & (df['workclass'] == 'Private')].shape[0])

'''Q90: What is the most common education level among people aged 65 and older?'''
# print(df[df['age'] >= 65]['education'].value_counts().head(1))

'''Q91: Among individuals earning >50K, how many are working part-time (<30 hours/week)?'''
# print(df[(df['income'] == '>50K') & (df['hours-per-week'] < 30)].shape[0])

'''Q92: Among those who work exactly 40 hours per week, what is the most common occupation?'''
# print(df[df['hours-per-week'] == 40]['occupation'].value_counts().head(1))

'''Q93: What is the distribution of marital status among people with Master's degrees?'''
# print(df[df['education'] == 'Masters']['marital-status'].value_counts())

'''Q94: Among people who are Self-emp-not-inc, what is the average capital gain?'''
# print(df[df['workclass'] == 'Self-emp-not-inc']['capital-gain'].mean())

'''Q95: Among individuals with 'Some-college' education, what percentage earn >50K?'''
# some_college = df[df['education'] == 'Some-college']
# print((some_college[some_college['income'] == '>50K'].shape[0] / some_college.shape[0]) * 100)

'''Q96: What is the gender breakdown of people aged 18 to 25 with income <=50K?'''
# print(df[(df['age'] >= 18) & (df['age'] <= 25) & (df['income'] == '<=50K')]['sex'].value_counts())

'''Q97: Among individuals who never married, what is the average capital loss?'''
# print(df[df['marital-status'] == 'Never-married']['capital-loss'].mean())

'''Q98: How many people with educational-num > 12 earn >50K?'''
# print(df[(df['educational-num'] > 12) & (df['income'] == '>50K')].shape[0])

'''Q99: What is the most common relationship type for people from Mexico?'''
# print(df[df['native-country'] == 'Mexico']['relationship'].value_counts().head(1))

'''Q100: Among individuals who work more than 50 hours/week and have a capital loss > 0, what is the most common marital status?'''
print(df[(df['hours-per-week'] > 50) & (df['capital-loss'] > 0)]['marital-status'].value_counts().head(1))





























































