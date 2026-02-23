import numpy as np

a1=np.arange(9).reshape(3,3)
a2=np.arange(9).reshape(3,3)

ans=[]
for i in range(3):
    for j in range(3):
        ans.append(a1[i,j]*a2[i,j])
print(ans)

print(a1*a2)