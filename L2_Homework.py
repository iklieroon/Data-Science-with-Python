import numpy as np
import random

a1=np.arange(1,17).reshape(4,4)
print(a1)
a1[a1%2==0]=0
a1[a1%2==1]=1
print(a1)
print(np.count_nonzero(a1==0))
print(np.count_nonzero(a1==1))

a2=np.random.randint(1,51,size=10)
print(a2)
print(np.max(a2))
print(np.min(a2))
print(np.sort(a2))
print(a2.reshape((2,5)))

a3=np.arange(1,25)
print(a3)
shapes=[(1,24),(2,12),(3,8),(4,6),(6,4),(8,3),(12,2),(24,1)]
for i in shapes:
    reshaped=a3.reshape(i)
    print(reshaped)
sortedrows=np.sort(reshaped,axis=1)
print(sortedrows)