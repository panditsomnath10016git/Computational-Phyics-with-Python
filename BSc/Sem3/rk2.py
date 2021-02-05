# pylint:disable=W0312
import math as m
import matplotlib.pyplot as plt


def f(x, y):  # defining the function
    fx = 2 * x + y
    return fx


a1 = 0.5
a2 = 1 - a1  # coefficients
q = p = 0.5 / a2
x0, y0 = 0.0, 0.0  # initial values
xmin, xmax = -0.5, 1.5  # range of solution
h = 0.1  # step size
np = 1 + int(abs(xmax - x0) / h)  # points in + direction
nm = 1 + int(abs(xmin - x0) / h)  # points in -  direction

xp = [0.0] * np
yp = [0.0] * np
xm = [0.0] * nm
ym = [0.0] * nm
for d in range(2):
    if d == 0:  # finding values in positive direction
        x = x0
        y = y0
        N = np
    else:  # finding values in negative direction
        x = x0
        y = y0
        h = -h
        N = nm
    for i in range(N):
        if d == 0:
            xp[i] = x
            yp[i] = y
        else:
            xm[i] = x
            ym[i] = y
        # rk2 formula
        k1 = f(x, y)
        k2 = f(x + p * h, y + k1 * q * h)
        y = y + (a1 * k1 + a2 * k2) * h
        x = x + h
# 		print x,k1,k2,y

# plotting the solution curve
plt.plot(xp, yp, ".-", xm, ym, ".-")
plt.xlabel("X ------>")
plt.ylabel("Y  ------>")
plt.grid()
plt.savefig("rk2.png", dpi=400)

# get values at different x
print "X must be in between %r and %r \
\n\nto stop press 'exit'\n" % (
    xmin,
    xmax,
)
a = 1
while 1 == 1:
    h = abs(h)
    xneed = xmin - 1
    while xneed < xmin or xneed > xmax:
        xneed = input("value at point x=")
        if xneed == exit:
            a = 2
            break
    if a != 1:
        break
    i = int(float(str(abs(xneed - x0) / h)))
    if xneed < x0:
        print ym[i]
    else:
        print yp[i]
