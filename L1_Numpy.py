import numpy as np

l1=[1,2,3]
l2=[]
for i in l1:
    a=i*2
    l2.append(a)
print(l2)

a1=np.array([1,2,3])
print(a1*2)

#Numpy is a python library which stands for numerical python. It is used for numerical and scientific computations. It is efficient, fast and handles multi-dimentional arrays well.

a2=np.array([4,5,6])
print(a1+a2)

print(np.__version__)

print(type(a2))

a3=np.array((7,8,9))
print(a3)

#Scalers - 0D arrays
a4=np.array(10)
print(a4)

#2D arrays
a5=np.array([[1,2,3],[4,5,6]])
print(a5)

#3D arrays
a6=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a6)

print(a4.ndim)
print(a5.ndim)
print(a6.ndim)

a7=np.array([1,2,3,4],ndmin=5)
print(a7)