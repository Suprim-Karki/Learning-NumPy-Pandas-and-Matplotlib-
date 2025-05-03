''' Interpolation method fills the missing value with an estimate '''

import pandas as pd

''' Linear interpolation '''
data={
    'name':['Ram','Shyam','Gopal'],
    'age':[10,20,30],
    'salary':[10000,None,30000]
}

df=pd.DataFrame(data)

df['salary']=df['salary'].interpolate(method='linear')
print(df)