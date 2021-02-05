import math as m
import matplotlib.pyplot as plt

np = 64
xmax = 5.0
x = x0 = 1.00000000001
y = y0 = 0.0
l = 1
h = (xmax - x0) / (np - 1)
xp = [0.0] * np
yp = [0.0] * np
y1 = 0.5
w = 5.0

for i in range(np):
    y2 = -(l * (l + 1) + 2 * x * y1) / (1 - x ** 2)
    y = yp[i] = y + h * y1 + (h ** 2 / 2) * y2
    y1 = y1 + h * y2
    xp[i] = x
    x = x + h


plt.plot(xp, yp)
plt.savefig("eular eqn.png")
