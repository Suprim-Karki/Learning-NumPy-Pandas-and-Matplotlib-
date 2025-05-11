import pandas as pd

dict1={
    'name':['Ramesh','Surabhi','Dinesh','Mahima','Kamala','Paresh','Harish'],
    'marks':[90,98,85,70,95,79,82],
    'gender':['Male','Female','Male','Female','Female','Male','Male']
}

df=pd.DataFrame(dict1)
# print(df)

''' Q1: Display top 3 Rows of dataset'''
# print(df.head(3))

''' Q2: Display last 3 Rows of dataset'''
# print(df.tail(3))

'''Q3: Find the shape of the dataset (rows,columns)'''
# print(df.shape)
# print(f"Number of rows= {df.shape[0]}")
# print(f"Number of columns= {df.shape[1]}")

'''Q4: Get all information about the dataset'''
# print(df.info())

'''Q5: Check null values in the dataset'''
# print(df.isnull())

'''Q6: Get overall statistics of the dataframe'''
# print(df.describe())

'''Q7: Find number of unique values from the gender column'''
# print(df['gender'].nunique())

'''Q8: Find unique values from the gender column'''
# print(df['gender'].unique())

'''Q9: Display count of unique values from gender column'''
# print(df['gender'].value_counts())

'''Q10: Find the total number of students having marks between 90 and 100(inclusie)'''
# print(df['marks'].between(90,100))

'''Q11: Find average marks'''
print(df['marks'].mean())


























































