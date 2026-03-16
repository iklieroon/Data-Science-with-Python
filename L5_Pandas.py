import pandas as pd

data=pd.read_csv('titanic.csv')

'''data1=data.sort_values(by='Pclass',ascending=True)
data2=data.sort_values(by='Fare',ascending=False)
print(data1)
print(data2)

print(data.head(10))

data['NameLower']=data['Name'].str.lower()
print(data['NameLower'])'''

data['Surname']=data['Name'].str.split(',').str[0]

data['Sex_short']=data['Sex'].replace({'male':'M','female':'F'})
print(data['Sex_short'])

print(data['Surname'].nunique())