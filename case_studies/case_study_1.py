import pandas as pd

df=pd.read_csv("Ecommerce Purchases")

'''Q1: Check null values in the dataset'''
print(df.isnull().sum())
