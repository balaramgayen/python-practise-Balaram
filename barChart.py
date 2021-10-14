from matplotlib import pyplot as plt

plt.bar([3,5,14],[5,2,19], label='first', color='g')
plt.bar([2,9,8],[7,2,5], label='second')

plt.legend()

plt.title('Bar chart practice')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()