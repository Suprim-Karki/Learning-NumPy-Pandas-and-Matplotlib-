import pandas as pd

dict1={
    'name':['Ramesh','Surabhi','Dinesh','Mahima','Kamala','Paresh','Harish'],
    'marks':[90,98,85,70,95,79,82],
    'gender':['Male','Female','Male','Female','Female','Male','Male']
}

df=pd.DataFrame(dict1)
print(df)

''' Q1: Display top 3 Rows of dataset'''
print(df.head(3))

''' Q2: Display last 3 Rows of dataset'''
print(df.tail(3))