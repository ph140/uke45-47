from numpy import linspace, sqrt, pi, e
from matplotlib import pyplot as plt


def f(x):
    return (1/sqrt(2*pi)) * e**((-x**2)/2)


def rektangelmetoden(f, a, b, N, offset=0.5):
    S = 0
    dx = (b-a)/N

    for n in range(N):
        x = a + n*dx
        h = f(x+offset*dx)
        A = dx*h
        S += A

    return S


def trapesmetoden(f, a, b, N):
    S = 0
    dx = (b-a)/N

    for n in range(N):
        x = a + n*dx
        h1 = f(x)
        h2 = f(x+dx)
        A = dx*(h1+h2)/2
        S += A

    return S


def res(h):
    for k in range(1, 4):
        N = int((k*2)/h)
        rek = rektangelmetoden(f, -k, k, N)
        trapes = trapesmetoden(f, -k, k, N)
        print(f"k={k}, h={h}")
        print(f"Rektangelmetoden: {rek}")
        print(f"Trapesmetoden: {trapes}\n")


res(0.1)
res(0.00001)
