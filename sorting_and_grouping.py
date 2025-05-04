import pandas as pd

df=pd.read_json("sample_Data.json")

''' Sorting '''

#Sorting a datra
# Syntax df.sort_values(by="column_name",ascending=True/False)

df.sort_values(by="price",ascending=True,inplace=True)
print(df)
