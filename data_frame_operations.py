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

''' Adding data frames but with indexing'''
#Here dataframes are added according to index 0 with 0 and so on

df3=pd.DataFrame({
    "a":[1,2,3]},index=[0,1,2]
    )

df4=pd.DataFrame({
    "a":[10,20,30]},index=[1,2,0]
    )

print(df3+df4)

''' Sample '''

#gives a random row as a sample
df=pd.read_json("sample_Data.json")
print(df.sample())
print(df.sample(10))  #for 10 samples

''' To display only n number of columns'''
# pd.options.display.max_columns=2
# print(df)

''' To operate directly on the df '''
df.price=df.price*2
df.price=df.price**2
df.id=df.id+2
print(df['price'])
print(df['id'])