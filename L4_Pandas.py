import pandas as pd

data=pd.read_csv('titanic.csv')

print(data.describe())
print(data.info())

names=data.loc[data['Age']>18,'Name']
print(names)
#Here we have got a column out of a condition.

print(data.iloc[9:25,2:5])
#This is slicing a dataframe, the first index is the row index and the second is the column index

#data.iloc[0:5,2]='charles'
#print(data['Name'])
#This is how you can change the value in a dataset. First you give the row and column you want to change, then what you want to change it to.

data.to_csv('titanic1.csv')

data['Test']=data['Fare']+2
print(data)
#This is how to create a new column

data_rename=data.rename(columns={'Pclass':'Passenger Class','Fare':'Fares'})
print(data_rename.info())
#This is how to rename a column in a dataframe

print(data[['Age','Fare']].mean())
#This is how to see the mean

print(data.agg({'Age':['min','max','median'],'Fare':['min','max','median']}))