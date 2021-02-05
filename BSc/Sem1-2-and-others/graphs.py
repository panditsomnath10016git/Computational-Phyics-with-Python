import math as m
import matplotlib.pyplot as plt

n = 10000
x0 = xi = -m.pi
xf = m.pi
h = (xf - xi) / n
xx = [0.0] * n
yy = [0.0] * n
zz = [0.0] * n
p = [0.0] * n

for i in range(n):
    x = x0 + i * h
    xx[i] = x
    yy[i] = m.sin(x) * m.cos(2 * x)
    zz[i] = -(1 / 9) * m.sin(3 * x)
    p[i] = yy[i] + zz[i]

plt.plot(xx, yy, xx, zz, xx, p)
plt.grid(axis="both")
plt.savefig("graph.png", dpi=400)
