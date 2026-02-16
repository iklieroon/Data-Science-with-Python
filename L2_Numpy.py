import numpy as np
import random

a1=np.array([1,2,3,4,5,6,7,8])

print(a1[0:5])
print(a1[::-1])
print(a1[0:8:2])

a2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2[2][0])

a3=np.array([1,2,3,4,5,6,7,8])
evenarray=a3[a3%2==0]
print(evenarray)
array1=a3[a3==5]
print(array1)
array2=a3[a3[[2,4,6]]]
print(array2)
a3=a3+1
print(a3)

m1=np.random.permutation(16).reshape(4,4)
m2=np.random.permutation(16).reshape(4,4)
print(m1)
print(m2)
print(m1+m2)

#Create a function to solve an equasion: y=2x+3

def solver(x):
    return 2*x+3
x1=np.array([1,2,3,4,5,6])
y=solver(x1)
print(y)
