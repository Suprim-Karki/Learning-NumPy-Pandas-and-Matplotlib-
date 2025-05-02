import pandas as pd

''' Adding data frames '''

# This way elements are added to their consecutive counterparts i.e. 1+10, 2+20,...
#   It shows NaN if the elements number don't match
df1=pd.DataFrame({
    "a":[1,2,3]}
    )

df2=pd.DataFrame({
    "a":[10,20,30,40]}
    )

print(df1+df2)



