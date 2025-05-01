import pandas as pd
# values=[10,20,30]
# s=pd.Series(values)
# print(s)

''' Series: A one dimensional array that can hold any data type: integer, float, string or even Python objects
            It is often used to track patterns or changes over time, such as daily temperatures, stock prices, etc.

    Dataframe: A dataframe is a 2 dimensional labeled data structure in Pandas, similar to a table in database, an excel spreadsheet or a SQL table.
               It consists rows and columns. 
'''

#read data from a csv file into a dataframe
df=pd.read_csv("sales_data_sample.csv", encoding="latin1")   #use encoding utf-8 if latin1 doesn't work

#read data from excel file
df=pd.read_excel("SampleSuperstore.xlsx")    #pip install xlrd for it to work

#read data from json file
df=pd.read_json("sample_Data.json")

print(df)
























































