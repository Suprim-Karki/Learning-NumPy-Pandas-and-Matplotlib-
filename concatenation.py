import pandas as pd

'''Concatenation'''

# region-1
df_region1=pd.DataFrame({
    "ID":[1,2],
    "Name":["A","B"]
})

df_region2=pd.DataFrame({
    "ID":[3,4],
    "Name":["C","D"]
})

''' Concat vertically (row) '''
df_v_concat=pd.concat([df_region1,df_region2], ignore_index=True)  #ignore index resets the index
print(df_v_concat)

''' Concat horizontally (column) '''
df_h_concat=pd.concat([df_region1,df_region2], axis=1,ignore_index=True)  #ignore index resets the index
print(df_h_concat)


















