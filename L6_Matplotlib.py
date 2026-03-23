import matplotlib.pyplot as plt
import numpy as np

'''x1=[1,2,3,4,5]
y1=[2,4,7,9,12]

plt.plot(x1,y1,'r^',label='y>x',linewidth=4)
#'r,[]' is to change what the lin looks like, e.g 'r-' makes a straight line but 'r--' makes a dashed line
plt.axis([0,10,0,50])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph')
plt.legend()
plt.show()

plt.plot([1,2,3,4,5],[2,3,4,5,6],'k-',label='y>x',linewidth=0.5)
plt.plot([1,2,3,4,5],[1,4,9,16,25],'r-',label='y=x**2',linewidth=1)
plt.axis([0,5,0,25])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('graph')
plt.legend()
plt.show()

l1=np.linspace(-3,3,100)
l2=l1**3+l1**2+l1

plt.plot(l1,l2)
plt.show()

x=np.arange(0,10,0.2)
print(x)
y1=x**2
y2=x**3
plt.plot(x,y1,'r-',x,y2,'b-')
plt.show()'''

#showing the categorical data using bar plot
plt.bar(['male literacy','female literacy'],[90,95])
plt.show()