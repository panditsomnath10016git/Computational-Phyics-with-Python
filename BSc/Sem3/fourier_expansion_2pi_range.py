# fourier expansion of a function in 2π range

import math as m

pi = m.pi
import matplotlib.pyplot as plt

N = 100
k = 10000
x0 = xi = -10.0
xf = 5.0
a0 = 0.0
h = (xf - xi) / k
xx = [0.0] * k
yy = [0.0] * k

for i in range(k):
    n = 0.0
    y = 0.0
    x = x0 + i * h
    xx[i] = x
    while n < N:
        n = n + 1
        an = 0.0
        bn = 1 / n
        y = y + an * m.cos(n * x) + bn * m.sin(n * x)
    yy[i] = a0 + y

plt.plot(xx, yy)
plt.grid(axis="both")
plt.savefig("graph.png", dpi=400)
