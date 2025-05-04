import pandas as pd

df=pd.read_json("sample_Data.json")

''' Sorting '''

#Sorting a datra
# Syntax df.sort_values(by="column_name",ascending=True/False)

df.sort_values(by="price",ascending=True,inplace=True)
print(df)

'''Sorting by multiple columns'''
df.sort_values(by=["price","id"],ascending=[True,False],inplace=True)
print(df)

'''Summary'''
avg_price=df['price'].mean()      #you can also use max(), min(), sum()
print(avg_price)


'''Grouping'''
grouped=df.groupby("price")["id"].sum()
print(grouped)

'''Grouping multiple column'''
grouped2=df.groupby(["price","name"])["id"].sum()
print(grouped2)
