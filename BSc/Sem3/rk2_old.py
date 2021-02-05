import math as m
import matplotlib.pyplot as plt


def f(x, y):  # defining the function
    fx = 2 * x
    return fx


x0 = 1.0  # initial values
y0 = 1.0
a1 = 0.5
a2 = 1 - a1
q = p = 0.5 / a2
xmax = 1.5  # range of solution
xmin = 0.0
h = 0.1  # step size
np = 1 + int(abs(xmax - x0) / h)  # points in + direction
nm = 1 + int(abs(xmin - x0) / h)  # points in -  direction
print np, nm

xp = [0.0] * np
yp = [0.0] * np
xm = [0.0] * nm
ym = [0.0] * nm

x = xp[0] = x0
y = yp[0] = y0

# finding values in positive direction
for i in range(1, np):
    k1 = f(x, y)
    k2 = f(x + p * h, y + k1 * q * h)
    y = yp[i] = y + (a1 * k1 + a2 * k2) * h
    x = xp[i] = x + h

x = xm[0] = x0
y = ym[0] = y0

# finding values in negative direction
h = -h
for i in range(1, nm):
    k1 = f(x, y)
    k2 = f(x + p * h, y + k1 * q * h)
    y = ym[i] = y + (a1 * k1 + a2 * k2) * h
    x = xm[i] = x + h

# plotting the solution curve
plt.plot(xp, yp, xm, ym)
plt.xlabel("X ------>")
plt.ylabel("Y  ------>")
plt.grid()
plt.savefig("rk2.png", dpi=400)

# get values at different x
print "X must be in between %r and %r \nto stop press 'exit'" % (xmin, xmax)
print
while 1 == 1:
    h = abs(h)
    xneed = input("value at point x=")
    if xneed == exit:
        break
    i = int(abs(xneed - x0) / h)
    if xneed < x0:
        print ym[i]
    else:
        print yp[i]
