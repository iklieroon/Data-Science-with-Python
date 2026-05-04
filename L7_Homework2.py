import matplotlib.pyplot as plt
import random

traffic=[3,2,4,4,5,6,10,14,11,12,8,2]
time=[0,2,4,6,8,10,12,14,16,18,20,22]
plt.bar(time,traffic,label='vehicles per hour')
plt.scatter(time,traffic,label='traffic',color='orange')
plt.legend()
plt.xlabel('time')
plt.ylabel('cars per hour')
plt.title('traffic')
plt.show()

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
steps=[]
for i in range(30):
    i=random.randint(5000,15000)
    steps.append(i)
steps10=[]
for i in steps:
    if i>10000:
        steps10.append(15000)
    else:
        steps10.append(0)

plt.plot(days,steps,label='daily steps')
plt.scatter(days,steps10,label='steps above 10k',color='red')
plt.legend()
plt.grid()
plt.xlabel('days')
plt.ylabel('steps')
plt.title('steps per day')
plt.show()