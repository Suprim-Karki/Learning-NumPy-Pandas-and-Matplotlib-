import pandas as pd

#consumer data frame
df_c = pd.DataFrame({
    "CustomerID":[1,2,3],
    "Name":["A","B","C"]
})

#orders data frame
df_o = pd.DataFrame({
    "CustomerID":[1,2,4],
    "Order_amount" :[100,200,300]
})

'''Inner join'''
# joins only the intersection(same) values
df_inner=pd.merge(df_c,df_o,on="CustomerID",how="inner")
print(df_inner)

'''Outer join'''
# joins all values
df_outer=pd.merge(df_c,df_o,on="CustomerID",how="outer")
print(df_outer)

'''Left join'''
# left values are kept as it is and right values are put in accordance to left ones
df_left=pd.merge(df_c,df_o,on="CustomerID",how="left")
print(df_left)