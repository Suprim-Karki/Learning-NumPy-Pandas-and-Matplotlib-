import pandas as pd

# Load the dataset
df = pd.read_csv("googleplaystore.csv")

'''Q1: Display the first 10 rows of the dataset.'''
# print(df.head(10))

'''Q2: What are the column names and how many are there?'''
# print(df.columns)
# print("Total columns:", len(df.columns))

'''Q3: What is the shape of the dataset (rows and columns)?'''
# print(df.shape)

'''Q4: How many unique app categories are there?'''
# print(df['Category'].nunique())

'''Q5: What are the top 5 most common app categories?'''
# print(df['Category'].value_counts().head(5))

'''Q6: What is the average app rating?'''
# print(df['Rating'].mean())

'''Q7: How many apps have a rating above 4.5?'''
# print((df['Rating'] > 4.5).sum())

'''Q8: Which app has the highest number of reviews?'''
# print(df.loc[df['Reviews'].astype(str).str.replace('.', '', regex=False).str.isnumeric(), 'Reviews'] = df['Reviews'].astype(str).str.replace(',', '', regex=False))
# df['Reviews'] = df['Reviews'].astype(float)
# print(df.loc[df['Reviews'].idxmax()])

'''Q9: What is the most common type of app (Free/Paid)?'''
# print(df['Type'].value_counts())

'''Q10: What is the average size of apps (excluding "Varies with device")?'''
# df_clean = df[~df['Size'].str.contains('Varies', na=False)]
# print(df_clean['Size'].head())

'''Q11: How many apps have over 1 million installs?'''
# df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True)
# df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
# print((df['Installs'] > 1000000).sum())

'''Q12: What are the top 5 apps by number of installs?'''
# print(df.sort_values(by='Installs', ascending=False).head(5)[['App', 'Installs']])

'''Q13: What is the distribution of app types across categories?'''
# print(df.groupby(['Category', 'Type']).size().unstack(fill_value=0))

'''Q14: What is the average rating for each category?'''
# print(df.groupby('Category')['Rating'].mean().sort_values(ascending=False))

'''Q15: Which category has the most apps?'''
# print(df['Category'].value_counts().head(1))

'''Q16: What is the most common content rating?'''
# print(df['Content Rating'].value_counts())

'''Q17: What is the average rating for Free vs Paid apps?'''
# print(df.groupby('Type')['Rating'].mean())

'''Q18: How many apps are rated 5.0?'''
# print((df['Rating'] == 5.0).sum())

'''Q19: Which category has the highest average number of installs?'''
# print(df.groupby('Category')['Installs'].mean().sort_values(ascending=False).head(1))

'''Q20: What is the most expensive app in the dataset?'''
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print(df.loc[df['Price'].idxmax()])































































