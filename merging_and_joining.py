import pandas as pd

#consumer data frame
df_c = pd.DataFrame({
    "Customer ID":[1,2,3],
    "Name":["A","B","C","D"]
})

#orders data frame
df_o = pd.DataFrame({
    "Customer ID":[1,2,4],
    "Order_amount" :[100,200,300]
})

