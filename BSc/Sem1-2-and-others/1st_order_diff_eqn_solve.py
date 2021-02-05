import math as m
import matplotlib.pyplot as plt

n = 50000
x = x0 = 0.0
y0 = 1.0
xmax = 3.0
h = (xmax - x0) / (n - 1)
xp = [0.0] * n
yp = [0.0] * n
i = 0

for i in range(n):
    x = x0 + i * h
    # tackling the value of log(0)
    if x == 0.0:
        y1 = 0.0
    else:
        y1 = x * m.log(x)  # y1==dydx=f(x,y), the eqn.
    y0 = yp[i] = y0 + h * y1
    xp[i] = x

plt.plot(xp, yp)
plt.savefig("1st order diff eqn solve.png")
