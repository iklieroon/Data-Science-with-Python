import matplotlib.pyplot as plt

days=[1,2,3,4,5]
eating=[2,3,1,5,4]
working=[3,4,6,8,5]
playing=[1,3,4,2,5]
plt.plot([],[],color='m',label='eating',linewidth=5)
plt.plot([],[],color='c',label='working',linewidth=3)
plt.plot([],[],color='r',label='playing',linewidth=1)
plt.stackplot(days,eating,working,playing,colors=['m','c','r'])
plt.xlabel=('x')
plt.ylabel=('y')
plt.title=('Stackplot')
plt.legend()
plt.show()