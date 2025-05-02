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


''' Using functions '''

def myfunc(x):
    if x%2==0:
        return x*2
    else:
        return x+2
    
print(df.price.apply(myfunc))


def myfunc2(x):
    if x.endswith('r'):
        return "Without Job"
    else:
        x
print(df.name.apply(myfunc2))

''' Adding new comumns'''
df['summary']=df.apply(lambda row: f"Id={row['id']} , Price={row['price']}",axis=1)
print(df)

''' Deleting a column/dropping '''
print(df.drop('summary',axis=1))   #use (df=) at start to save the change in df

''' To drop/fill Null/NaN values'''
# print(df.dropna())
print(df.fillna(0))  #fills the null values with 0

df.price.fillna(df.price.mean())

'''notna method'''
print(df.notna())  # provides true or false whether value is null or not
