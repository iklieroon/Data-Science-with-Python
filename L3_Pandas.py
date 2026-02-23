import pandas as pd

data={'name':['Joe','Jeff','Jay','Carl','Ryan','Shaun','Jeffrey','Joseph','Zach','Zachary'],'age':[21,22,18,17,16,19,20,23,25,32],'salary':[4000,5000,3000,0,10,2500,3500,5000,7500,10000]}
df=pd.DataFrame(data)
print(df)

print(df.head())
#The head function helps us to see a limited number of rows, defaulted to 5

print(df.shape)
#This shows how many rows and columns there are in your dataframe

print(df['name'])
#How to access values

print(df['age'].max())
print(df['age'].min())
#Gives the max and min values of the column

print(type(df['age']))
#Gives the type of the column

print(df['age'].shape)
#This gives the amount of rows there are in the said column

print(df.info())
#This gives the summary of the data

print(df.describe())
#Gives the importiant on all the numerical columns

data1=pd.read_csv('titanic.csv')
#This is how to download CSV files 
