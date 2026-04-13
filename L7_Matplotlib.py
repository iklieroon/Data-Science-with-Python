import matplotlib.pyplot as plt

#Histogram
ages=[20,35,23,18,16,4,65,36,37,41,33,21,17,15,24,28,27]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('Age interval')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

#Scatter Plot
x=[1,2,3,4,5,6,7,8,9]
y=[0,1,0,1,0,1,0,1,0]
plt.scatter(x,y,label='Scatterplot',color='red',marker='o',s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Graph')
plt.legend()
plt.show()

#Pie Chart
slices=[1,2,3,4,5]
activities=['eating','sleeping','studying','talking','playing']
c=['c','m','r','b','g']
plt.pie(slices,labels=activities,colors=c,startangle=90,shadow=True)
plt.title('Pie Chart')
plt.show()