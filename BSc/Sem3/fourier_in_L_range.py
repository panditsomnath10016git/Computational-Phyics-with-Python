# Fourier expansion of a function in any range for given an, bn

import math as m

pi = m.pi
import matplotlib.pyplot as plt

N = 100  # number of fourier terms
k = 10000  # number of points for graph

x0 = xi = -8.0  # range of graph
xf = 8.0
a0 = 2.0
l = 16  # periodicity
h = (xf - xi) / k
xx = [0.0] * k
yy = [0.0] * k

for i in range(k):
    n = 0.0  # sum index -1
    y = 0.0
    x = x0 + i * h
    xx[i] = x
    while n < N:
        n = n + 1
        
        # fourier coefficients
        an = (
            16
            * (2 * m.cos(n * pi / 2) - m.cos(n * pi) - 1)
            / (n * n * pi ** 2)
        )
        bn = 0.0
        
        # fourier series formula
        y = y + an * m.cos(2 * pi * n * x / l) + bn * m.sin(2 * pi * n * x / l)
    yy[i] = a0 + y  # fourier series value at x


# plot the function of fourier expansion
plt.plot(xx, yy)
plt.grid()
plt.savefig("fourier any range.png", dpi=300)
