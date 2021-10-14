from matplotlib import colors, pyplot as plt
from matplotlib import style

style.use('ggplot')



x = [5,7,9]
y = [5,6,2]

x2 = [6,8,10]
y2 = [7,10,4]

plt.plot(x, y,'g',label='line 1',linewidth='2')
plt.plot(x2, y2,'b',label='line 2',linewidth='2')

plt.title('info')
plt.xlabel('x bar')
plt.ylabel('y bar')

plt.legend()

plt.grid(True,color='k')

plt.show()