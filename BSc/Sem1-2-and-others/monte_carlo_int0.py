import math as m
import random as rnd
import matplotlib.pyplot as plt

n = 0
N = 1000000     # number of random points
xmax = 3.0
ymax = 0.0
xp = x = [0.0] * N
y = [0.0] * N
yp = [0.0] * N
ya = [0.0] * N
i = 0

for i in range(N):
    x[i] = xmax * rnd.random()
    ya[i] = m.exp(-x[i] * x[i])
    if ya[i] >= ymax:
        ymax = ya[i]

for i in range(N):
    y[i] = ymax * rnd.random()
    if y[i] <= ya[i]:
        xp[i] = x[i]
        yp[i] = y[i]
        n = n + 1
        
int_val = (n * xmax * ymax) / N

print("integration value=", int_val)
plt.plot(x, y, ".", xp, yp, ".")
plt.savefig("monte carlo graph.jpg")
