import matplotlib.pyplot as plt
import random

'''marks=[]
score=0
for i in range(50):
    i=random.randint(0,100)
    marks.append(i)
    if i>75:
        score+=1
bins=[0,30,50,70,90,100]
plt.hist(marks,bins,histtype='bar',rwidth=0.8,label='Marks')
plt.xlabel('mark ranges')
plt.ylabel('frequency')
plt.title('Marks')
plt.show()
print(score)'''

slices=[4,1,1,2,3]
expenses=['Rent','Food','Transport','Entertainment','Savings']
c=['c','m','r','g','b']
plt.pie(slices,labels=expenses,colors=c,startangle=90,shadow=True)
plt.title('Expenses')
plt.show()
percentages=[]
for i in slices:
    j=(i/11)*100
    percentages.append(j)

print(round(max(percentages),2))