# pylint:disable=W0312
import math as m
import matplotlib.pyplot as plt

xg = [-2.0, 0.0, 2.0, 3.0]  # input data set
yg = [-8.0, 0.0, 8.0, 27.0]
npg = len(xg)  # number of points
xmin, xmax = -4.0, 4.0  # solution range
h = 0.001  # step size
N = int(abs(xmax - xmin) / h)  # number of points
xp = [0.0] * N
yp = [0.0] * N

for i in range(N):
    x = xp[i] = xmin + i * h
    y = 0.0

    for j in range(npg):  # sum the terms
        k = 0
        m = 1.0
        while k < npg:  # generate the terms to sum
            if j != k:  # exclude the releted given point
                # multiply to generate each term
                m = m * (x - xg[k]) / (xg[j] - xg[k])
            k = k + 1
        y = yp[i] = y + m * yg[j]
        
# fitting the curve
plt.plot(xp, yp, xg, yg, "o")
plt.grid()
plt.xlabel("X ------>")
plt.ylabel("Y ------>")
plt.savefig("lagrange interpolation.png")

# get value at specific point
print (
    "X must be in between %r and %r \
\n\nto stop press 'exit'\n"
    % (xmin, xmax)
)
while 1 == 1:
    xneed = input("value at point x=")
    if xneed == exit:
        break
    w = int(float(str((xneed - xmin) / h)))
    print "is=%r" % (yp[abs(w)])
    print
