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
# print(len(df[df['Email'].str.contains('yahoo.com')]))

'''Q28: Number of purchases made from IP addresses starting with "192."'''
# print(len(df[df['IP Address'].str.startswith('192.')]))

'''Q29: Number of people whose job title ends with "Engineer"'''
# print(len(df[df['Job'].str.lower().str.endswith('engineer')]))

'''Q30: Number of people whose language is English and have a purchase price above $80'''
# print(len(df[(df['Language'] == 'en') & (df['Purchase Price'] > 80)]))

'''Q31: Total purchase amount made by people using Mastercard'''
# print(df[df['CC Provider'] == 'Mastercard']['Purchase Price'].sum())

'''Q32: Count of credit cards expiring each year'''
# print(df['CC Exp Date'].str.split('/').str[1].value_counts())

'''Q33: Number of people whose email username (before @) starts with 'a' '''
# print(len(df[df['Email'].str.split('@').str[0].str.startswith('a')]))

'''Q34: Number of people with an IP address ending in ".com" (if present)'''
# print(len(df[df['IP Address'].str.endswith('.com')]))  # Might be 0 depending on data structure

'''Q35: Average purchase price for users who made purchases during AM'''
# print(df[df['AM or PM'] == 'AM']['Purchase Price'].mean())

'''Q36: Find all people whose job title is exactly 2 words long'''
# print(df[df['Job'].str.strip().str.split().apply(len) == 2])

'''Q37: Number of users whose email domain is ".edu"'''
# print(len(df[df['Email'].str.endswith('.edu')]))

'''Q38: Maximum purchase price made using Visa'''
# print(df[df['Credit Card'].astype(str).str.startswith('4')]['Purchase Price'].max())

'''Q39: Find users whose job title contains both "Senior" and "Engineer"'''
# print(df[df['Job'].str.contains('Senior', case=False) & df['Job'].str.contains('Engineer', case=False)])

'''Q40: Count of users who use a credit card that expires in a year ending with an odd number'''
# print(len(df[df['CC Exp Date'].str.split('/').str[1].astype(int) % 2 == 1]))

'''Q41: Find the domain with the least number of email users'''
# print(df['Email'].str.split('@').str[1].value_counts().idxmin())

'''Q42: Average purchase price for people whose job contains the word "Consultant"'''
# print(df[df['Job'].str.contains('Consultant', case=False)]['Purchase Price'].mean())

'''Q43: Count of users whose email starts with a digit'''
# print(len(df[df['Email'].str.split('@').str[0].str.match('^\d')]))

'''Q44: Number of users who purchased using credit cards that expire in November'''
# print(len(df[df['CC Exp Date'].str.startswith('11')]))

'''Q45: Find top 3 job titles among users who use Yahoo email'''
# print(df[df['Email'].str.contains('yahoo.com')]['Job'].value_counts().head(3))

'''Q46: Number of users whose name contain a hyphen (e.g., Mary-Jane)'''
# print(len(df[df['Name'].str.contains('-')])) 

'''Q47: Number of users whose purchase price is a whole number (no decimal cents)'''
# print(len(df[df['Purchase Price'] % 1 == 0]))

'''Q48: List all unique email domains used by users (after @)'''
# print(df['Email'].str.split('@').str[1].unique())

'''Q49: Number of users whose credit card number has a repeating digit sequence (e.g., "111", "2222")'''
# import re
# pattern = r"(.)\1{2,}"  # any digit repeated 3 or more times
# print(len(df[df['Credit Card'].astype(str).str.contains(pattern)]))

'''Q50: Number of purchases made during lunchtime (12 PM to 1 PM)'''
# df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
# print(len(df[df['Hour'] == 12]))

'''Q51: Find users whose job title starts and ends with the same letter (case-insensitive)'''
# print(df[df['Job'].str.lower().str[0] == df['Job'].str.lower().str[-1]])

'''Q52: Count of users whose email domain is exactly 5 characters long before ".com" or ".net" (e.g., "abcde.com")'''
# print(len(df[df['Email'].str.split('@').str[1].str.extract(r'^([a-zA-Z0-9]{5})\.(com|net)$').notnull().any(axis=1)]))

'''Q53: Number of users whose job title contains a digit (e.g., "Engineer2")'''
# print(len(df[df['Job'].str.contains(r'\d')]))

'''Q54: Find users who made purchases at exact hour 00:00 (midnight)'''
# df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
# df['Minute'] = pd.to_datetime(df['Time'], format='%H:%M').dt.minute
# print(df[(df['Hour'] == 0) & (df['Minute'] == 0)])

'''Q55: Number of users whose names have exactly three words (e.g., "John Michael Smith")'''
# print(len(df[df['Name'].str.strip().str.split().apply(len) == 3]))

'''Q56: Top 3 most common last names in the dataset'''
# print(df['Name'].str.split().str[-1].value_counts().head(3))

'''Q57: Number of users who have more than one capital letter in their email username'''
# print(len(df[df['Email'].str.split('@').str[0].str.count(r'[A-Z]') > 1]))

'''Q58: Number of users whose job title has exactly 10 characters'''
# print(len(df[df['Job'].str.len() == 10]))

'''Q59: Count of users whose name includes both a first and last name starting with the same letter'''
# print(len(df[df['Name'].str.split().apply(lambda x: len(x) >= 2 and x[0][0].lower() == x[1][0].lower())]))

'''Q60: Number of users who made a purchase price ending in .99'''
# print(len(df[df['Purchase Price'] % 1 == 0.99]))

'''Q61: Count of users whose job title contains special characters (e.g., &, @, #)'''
# print(len(df[df['Job'].str.contains(r'[&@#]')]))

'''Q62: Number of users whose IP address contains a palindrome (e.g., "121.45.121.45")'''
def is_palindrome(ip):
    return ip.replace('.', '') == ip.replace('.', '')[::-1]
print(len(df[df['IP Address'].apply(is_palindrome)]))

























