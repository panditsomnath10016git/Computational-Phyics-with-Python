import math as m
import matplotlib.pyplot as plt

np = 3200
xmax = 5.0
x = x0 = 0.0
y = y0 = 1.0
h = (xmax - x0) / (np - 1)
y1 = 0.5
w = 4
b = 0.5
xp = [0.0] * np
yp = [0.0] * np

for i in range(np):
    y2 = -(2 * b * y1 + w ** 2 * y)
    y = yp[i] = y + h * y1 + (h ** 2 / 2) * y2
    y1 = y1 + h * y2
    xp[i] = x + i * h


plt.plot(xp, yp)
plt.savefig("damp vibration.png")
