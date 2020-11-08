import numpy as np
from matplotlib import pyplot as plt


data = np.loadtxt('vogn.txt', float, skiprows=1)
time = []
position = []
speed1 = []
speed2 = []


def derivert(x):
    return data[x+1][1] - data[x][1]


def symmetrisk_derivert(x):
    return (data[x+1][1] - data[x-1][1])/2


for i, j in enumerate(data[:-1]):
    if i:
        speed1.append(derivert(i))
        speed2.append(symmetrisk_derivert(i))
        time.append(j[0])

plt.plot(time, speed1, 'g-')
plt.plot(time, speed2, 'r-')
plt.show()
