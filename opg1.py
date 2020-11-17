import numpy as np
from matplotlib import pyplot as plt


def d(x):
    return (np.e)**x - 5*x


def g(x):
    return x**2 - 4*x + 5


def i(x):
    return 2*x + 1


def derivert(f, x, h):
    return ((f(x+h)-f(x))/h)


h = 0.001
xmin = 2
xmax = 5
N = int((xmax - xmin)/h)+1
xes = np.linspace(xmin, xmax, N)


def showres(f):
    func = f(xes)
    df = derivert(f, xes, h)

    plt.plot(xes, func, label='f(x)')
    plt.plot(xes, df, label="f'(x)")
    plt.xlabel('x')
    plt.grid('both')
    plt.legend()
    plt.show()


showres(d)
showres(g)
showres(i)
