import math as m
import matplotlib.pyplot as plt

N = 50
n = 10000
x0 = xi = -5.0
xf = 5.0
h = (xf - xi) / n

xx = [0.0] * n
yy = [0.0] * n

for i in range(n):
    k = -1.0
    y = 0.0
    x = x0 + i * h
    xx[i] = x
    while k < N:
        k = k + 2
        #print(k)
        y = y + (4 / k * m.pi) * m.sin(k * x)
    yy[i] = y

plt.plot(xx, yy)
plt.grid()
plt.savefig("graph.png")
