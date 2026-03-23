import pandas as pd

data=pd.read_csv('titanic.csv')

data['FarePerPerson']=data['Fare']/(data['Siblings/Spouses Aboard']+1)
print(data['FarePerPerson'])

data['AgeGroup']=0
for i in data['Age']:
    if i<12:
        data['AgeGroup']='Child'
    if i>=12 and i<=18:
        data['AgeGroup']='Teen'
    if i>18:
        data['AgeGroup']='Adult'
print(data['AgeGroup'])

print((data['AgeGroup'].value_counts()).head())