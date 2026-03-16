import pandas as pd

data=pd.read_csv('titanic.csv')

print(data.groupby('Sex')[['Age','Fare']].mean())
print(data.groupby(['Sex','Pclass'])['Fare'].mean())
print(data['Survived'].value_counts())
print(data.groupby(['Sex','Pclass'])['Age'].max())