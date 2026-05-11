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