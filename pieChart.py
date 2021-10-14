import matplotlib.pyplot as plt

slices = [20,35,10,60]
activites = ['study','sleep','break','coding']
cols = ['c','m','r','b']

plt.pie(slices,
    labels=activites,
    colors=cols,
    startangle=90, 
    shadow=True,
    autopct='%1.1f%%'
    )

plt.title('pie plot diagram')

plt.show()