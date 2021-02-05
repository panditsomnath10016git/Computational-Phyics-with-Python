import math as m
import matplotlib.pyplot as plt


def f(x, y):  # defining the function
    fx = 3 * x * x
    return fx


x0, y0 = 0.0, 0.0  # initial values
xmin, xmax = -1.5, 1.5  # range of solution
h = 0.01  # step size
np = int(abs(xmax - x0) / h)  # points in + direction
nm = int(abs(xmin - x0) / h)  # points in -  direction

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
            
        # rk4 formula
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h

# plotting the solution curve
plt.plot(xp, yp, xm, ym)
plt.xlabel("X ------>")
plt.ylabel("Y  ------>")
plt.grid()
plt.savefig("rk4.png", dpi=400)

# get values at different x
print(
    "X must be in between %r and %r \
\n\nto stop press 'exit'\n"
    % (xmin, xmax)
)
while 1 == 1:
    h = abs(h)
    xneed = input("value at point x=")
    if xneed == exit:
        break
    i = int(float(str(abs(xneed - x0) / h)))
    if xneed < x0:
        print(ym[i])
    else:
        print(yp[i])
