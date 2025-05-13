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
print(len(df[(df['CC Provider']=='Mastercard') & (df['Purchase Price']>50)]))


















