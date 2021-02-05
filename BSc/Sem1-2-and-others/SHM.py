import math as m
import matplotlib.pyplot as plt

np = 3200
xmax = 5.0
x = x0 = 0.0
y = y0 = 1.0
h = (xmax - x0) / (np - 1)
xp = [0.0] * np
yp = [0.0] * np
dydx = 0.5
w = 5.0

for i in range(np):
    y = yp[i] = y + h * dydx + (h ** 2 / 2) * (-(w ** 2) * y)
    dydx = dydx + h * (-(w ** 2) * y)
    xp[i] = x
    x = x + h


plt.plot(xp, yp)
plt.savefig("shm.png")
