import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('fallskjerm.txt', float, skiprows=1)

speedlist = [0]
timelist = [0]
S = 0

for i, _ in enumerate(data[:-1]):
    time1 = data[i][0]
    time2 = data[i+1][0]
    dx = time2-time1

    h1 = data[i][1]
    h2 = data[i+1][1]
    timelist.append(time1)

    A = dx*(h1+h2)/2

    speedlist.append(A+speedlist[i])
    S += A

plt.plot(timelist, speedlist, 'b-')
plt.show()
print(S)
