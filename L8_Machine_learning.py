import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Splitting the data into training and testing

from sklearn.model_selection import train_test_split
#The algorithm that we will use to make predictions
from sklearn.tree import DecisionTreeClassifier
#For checking the accuracy
from sklearn import metrics
df=pd.read_csv('iris.csv')
print(df.head())
print(df.info())
df['species']=df['species'].replace({'setosa':0,'versicolor':1,'virginica':2})
print(df['species'])

'''a=df['petal_width']
b=df['petal_length']
plt.scatter(a,b)
plt.xlabel('petal width')
plt.ylabel('petal length')
plt.title('petal')
plt.show()

c=df['sepal_width']
d=df['sepal_length']
plt.scatter(a,b)
plt.xlabel('sepal width')
plt.ylabel('sepal length')
plt.title('sepal')
plt.show()
'''
x=df.drop('species',axis=1)
y=df['species']
print(x.head())

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
print(x_train.shape)
print(x_test.shape)

model=DecisionTreeClassifier(max_depth=3,random_state=1)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print('accuracy',metrics.accuracy_score(predictions,y_test))
