import pandas as pd
df=pd.read_json("sample_Data.json")

''' Using loc to update values'''
#df.loc[row_index, "column_name"] = new_value

# df.loc[0,"Price"]=10.00
# print(df)

''' Updating multiple values '''
df["Price"]=500
print(df)
















