import math as m
import random as rnd
import matplotlib.pyplot as plt

N = 100000  # number of random points to be generated
xmax = 2.0  # x range
xmin = -2.0
ymax = ymin = 0.0
xp = x = [0.0] * N
y = [0.0] * N
yp = [0.0] * N
ya = [0.0] * N
n = 0
i = 0

for i in range(N):
    a = x[i] = rnd.uniform(xmin, xmax)
    ya[i] = pow(m.sin(a), 3)  # define the function
    # 	getting the inegration y range
    if ya[i] >= ymax:
        ymax = ya[i]
    if ya[i] <= ymin:
        ymin = ya[i]
# 	print (xmin ,ymin)

for i in range(N):
    y[i] = rnd.uniform(ymin, ymax)
    if y[i] >= 0:
        if y[i] <= ya[i]:
            xp[i] = x[i]
            yp[i] = y[i]
            n = n + 1
    if y[i] < 0:
        if y[i] >= ya[i]:
            xp[i] = x[i]
            yp[i] = y[i]
            n = n + 1

xd = xmax - xmin
yd = ymax - ymin
i_val = (n * xd * yd) / N
m = str(n)
print("integration value=", i_val)

# plotting graph
plt.plot(
    x,
    y,
    ".w",
    xp,
    yp,
    ".g",
)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Monte-Carlo Integration")
plt.savefig("monte carlo graph %s.png" % m, dpi=400)
