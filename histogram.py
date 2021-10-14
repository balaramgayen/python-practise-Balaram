import matplotlib.pyplot as plt

histography_data = [4,78,14,25,45,15,85,36,45,44,11,45,88,45,12,25,78,45,96,25,38,48,45,14,45,9]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

plt.hist(histography_data,bins,histtype='bar',rwidth=0.5)

plt.title("histography data analysis")

plt.xlabel('this is X axis')
plt.ylabel('this is Y axis')

plt.legend()

plt.show()