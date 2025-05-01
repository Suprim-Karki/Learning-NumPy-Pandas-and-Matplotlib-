''' To save data into a file'''

import pandas as pd

data={
    "Name":["Ram","Shyam","Hari"],
    "Age":[10,20,30],
    "City":["KTM","Lalitpur","Bhaktapur"]

}
df=pd.DataFrame(data)
print(df)

df.to_csv("saved.csv",index=False)  #index=False is to remove 0,1,2 default index while saving
# df.to_excel("saved.csv",index=False)
# df.to_json("saved.csv",index=False)