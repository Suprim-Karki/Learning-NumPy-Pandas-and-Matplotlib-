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

'''Q17: Most common language spoken by customers'''
# print(df['Language'].value_counts().head(1))

'''Q18: Most common credit card provider'''
# print(df['CC Provider'].value_counts().head(1))

'''Q19: Number of people whose purchase price is exactly $99.99'''
# print(len(df[df['Purchase Price'] == 99.99]))

'''Q20: List of unique job titles'''
# print(df['Job'].unique())

'''Q21: Average purchase price for people who use American Express'''
# print(df[df['CC Provider'] == 'American Express']['Purchase Price'].mean())

'''Q22: Percentage of users who use Gmail'''
# gmail_count = df['Email'].str.contains('gmail.com').sum()
# total = len(df)
# print((gmail_count / total) * 100)

'''Q23: Emails of people who made a purchase over $90 and use Hotmail'''
# print(df[(df['Purchase Price'] > 90) & (df['Email'].str.contains('hotmail.com'))]['Email'])

'''Q24: Number of people with credit card numbers starting with "4" (likely Visa)'''
# print(len(df[df['Credit Card'].astype(str).str.startswith('4')]))

'''Q25: Most common hour of the day for purchases (if time column exists)'''
# df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
# print(df['Hour'].value_counts().head(1))

'''Q26: Number of people who have the word "Manager" in their job title'''
# print(len(df[df['Job'].str.contains('Manager', case=False)]))

'''Q27: Number of people who use Yahoo as their email provider'''
print(len(df[df['Email'].str.contains('yahoo.com')]))








