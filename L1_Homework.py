import numpy as np

l1=[1,2,3,4,5,6,7,8,9,10]

a1=np.array([1,2,3,4,5,6,7,8,9,10])


l2=[]
for i in l1:
    a=i*2
    l2.append(a)
print(l2)
print(a1*2)
#They both give the same output

l3=[1,2,3]
l4=[4,5,6]
l5=[]
for i in range(len(l3)):
    l5.append(l3[i]+l4[i])
print(l5)

a2=np.array([1,2,3])
a3=np.array([4,5,6])
print(a2+a3)