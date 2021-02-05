import math as m
import matplotlib.pyplot as plt

np = 3200
xmax = 2.0
x = x0 = 0.0
y = y0 = 1.0
h = (xmax - x0) / (np - 1)
xp = [0.0] * np
yp = [0.0] * np
w = 5.0

for i in range(np):
    y1 = y * x ** 3 - y ** 2 * m.sin(x)  # diff. equation
    y = yp[i] = y + h * y1
    xp[i] = x
    x = x + h

plt.plot(xp, yp)
plt.savefig("1st order homogenious.png")
