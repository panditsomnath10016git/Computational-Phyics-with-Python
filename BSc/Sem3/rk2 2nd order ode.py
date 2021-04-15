# pylint:disable=W0312
import math as m
import matplotlib.pyplot as plt


def f(x,phi):  # defining the function
    return phi


def g(x, psi,k):  # g=f '
    return -k*psi


x0, psi0, phi0 = 0.0, 0.0, 1.0  # initial values
xmin, xmax = -0.0, 1.0  # range of solution
n_slice = 500
n_points = n_slice+1
h = (xmax-xmin)/n_points # step size

np = int(abs(xmax - x0) / h)  # points in + direction
nm = int(abs(xmin - x0) / h)  # points in -  direction
xp = [0.0] * np
yp = [0.0] * np
xm = [0.0] * nm
ym = [0.0] * nm

for d in range(2):
    if d == 0:  # finding values in positive direction
        x, y, z = x0, y0, z0
        N = np
    else:  # finding values in negative direction
        x, y, z = x0, y0, z0
        h = -h
        N = nm
    for i in range(N):  # get values at all x in range
        if d == 0:
            xp[i] = x
            yp[i] = y
        else:
            xm[i] = x
            ym[i] = y
            
        # rk2 formula for f and g
        k1 = h * f(x, y, z)
        j1 = h * g(x, y, z)
        x1, y1, z1 = x + h, y + k1, z + j1
        k2 = h * f(x1, y1, z1)
        j2 = h * g(x1, y1, z1)
        y = y + (k1 + k2) / 2
        z = z + (j1 + j2) / 2
        x = x + h
# 		print i,x,k1,j1,k2,j2,y,z;print

# plotting the solution curve
plt.plot(xp, yp, ".-", xm, ym, ".-")
plt.xlabel("X ------>")
plt.ylabel("Y  ------>")
plt.grid()
plt.savefig("2nd order ode by rk2.png", dpi=400)

# get value at specific x
print "X must be in between %r and %r \
\n\nto stop press 'exit'\n" % (
    xmin,
    xmax,
)
while 1 == 1:
    h = abs(h)
    xneed = input("value at point x=")
    if xneed == exit:
        break
    i = int(float(str(abs(xneed - x0) / h)))
    if xneed < x0:
        print ym[i]
    else:
        print yp[i]
