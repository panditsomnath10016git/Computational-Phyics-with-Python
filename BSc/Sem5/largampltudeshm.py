# pylint:disable=W0312
import math as m
import matplotlib.pyplot as plt


def f(t, x, z):  # defining the function
    ftxz = z
    return ftxz


def g(t, x, z):  # g=f '
    gtxz = -m.sin(x)
    return gtxz


t0, x0, z0 = 0.0, m.pi / 2, 0.0  # initial values
tmin, tmax = 0.0, 10.0  # range of solution
h = 0.0025  # step size

np = int(abs(tmax - t0) / h)  # points in + direction
nm = int(abs(tmin - t0) / h)  # points in -  direction
tp = [0.0] * np
xp = [0.0] * np
tm = [0.0] * nm
xm = [0.0] * nm

for d in range(2):
    if d == 0:  # finding values in positive direction
        t, x, z = t0, x0, z0
        N = np
    else:  # finding values in negative direction
        t, x, z = t0, x0, z0
        h = -h
        N = nm
    for i in range(N):  # get values at all t in range
        if d == 0:
            tp[i] = t
            xp[i] = x
        else:
            tm[i] = t
            xm[i] = x
            
        # rk2 formula for f and g
        k1 = h * f(t, x, z)
        j1 = h * g(t, x, z)
        t1, x1, z1 = t + h, x + k1, z + j1
        k2 = h * f(t1, x1, z1)
        j2 = h * g(t1, x1, z1)
        x = x + (k1 + k2) / 2
        z = z + (j1 + j2) / 2
        t = t + h
# 		print i,t,k1,j1,k2,j2,x,z;print

# plotting the solution curve
plt.plot(
    tp,
    xp,
    tm,
    xm,
)
plt.xlabel("X ------>")
plt.ylabel("Y  ------>")
plt.grid()
plt.savefig("largampltudeshm.png", dpi=400)
"""
#get value at specific t

print "X must be in between %r and %r \
\n\nto stop press 'exit'\n" %(tmin,tmax)
while 1==1:
	h=abs(h)
	tneed=input('value at point t=')	
	if tneed==exit:
		break
	i=int(float(str(abs(tneed-t0)/h)))
	if tneed<t0:
		print xm[i]
	else:
		print xp[i]
"""
