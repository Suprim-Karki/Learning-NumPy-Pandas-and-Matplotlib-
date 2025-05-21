import pandas as pd

df=pd.read_csv("Ecommerce Purchases")

'''Q1: Check null values in the dataset'''
# print(df.isnull().sum())

'''Q2: Highest and lowest purchase price'''
# print(df['Purchase Price'].max())
# print(df['Purchase Price'].min())

'''Q3: Average purchase price'''
# print(df['Purchase Price'].mean())

'''Q4: Number of people with French (fr) as their language of choice'''
# print(df[df['Language']=='fr'])

'''Q5: Job title containing the word "engineer"'''
# print(df[df['Job'].str.contains('engineer',case=False)])

'''Q6: Number of people who have the job title "Lawyer"'''
# print(df[df['Job']=='Lawyer'].count())

'''Q7: Email of the person with following ip address 132.207.160.22'''
# print(df[df['IP Address']=='132.207.160.22']['Email'])

'''Q8: Number of people who have mastercard as their credit card provider and made a purchase above 50'''
# print(len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price']>50)]))

'''Q9: Number of people who have a credit card that expires in 2025'''
# print(len(df[df['CC Exp Date'].str.contains('25')]))

'''Q10: Number of people who made a purchase between $50.00 and $100.00'''
# print(len(df[(df['Purchase Price']>=50) & (df['Purchase Price']<=100)]))

'''Q11: Find the email of the person with the following credit card number 4926535242672853'''
# print(df[df['Credit Card']==4926535242672853]['Email'])

'''Q12: Number of people who have a credit card that expires in December 2025'''
# print(len(df[df['CC Exp Date'].str.contains('12/25')]))

'''Q13: How many prople purchased during the AM and how many during PM?'''
# print(df['AM or PM'].value_counts())

'''Q14: Top 5 most popular email providers'''
# print(df['Email'].str.split('@').str[1].value_counts().head(5))

'''Q15: Top 5 most common job titles'''
# print(df['Job'].value_counts().head(5))

'''Q16: Number of people who have a credit card that expires in 2025 and have the job title "Lawyer"'''
# print(len(df[(df['CC Exp Date'].str.contains('25')) & (df['Job']=='Lawyer')]))

''''''



