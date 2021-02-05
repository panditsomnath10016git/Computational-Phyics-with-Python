import math as m
import matplotlib.pyplot as plt


def f(x, y):
    fx = 1 / y ** 2  # define the function
    return fx


np = 2  # number of points
N = 5  # number of recursion for improvement
xp = [0.0] * np
yp = [0.0] * np

# xmax=0.0		#range
x = x0 = 0.0  # initial values
y = y0 = 1.0
# h=(xmax-x0)/(np-1)		#step size
h = 0.1

for i in range(np):
    y1 = 0.0
    x = xi = x0 + i * h
    xp[i] = x
    yp[i] = y
    # 	print "hi"
    for j in range(N):
        if j == 0:
            y10 = f(x, y)  # tangent at xn
            # 			print x,y,y10
            y = yp[i] + y10 * h  # yn+1 based on y10
            x = x + h  # xn+1
        y1N = f(x, y)  # tangent at xn+1
        # print x,y,y1N
        y1 = (y10 + y1N) / 2  # avg. of tangents at xn and xn+1
        y = yp[i] + y1 * h  # yn+1 based on the improved tangent
# 	print y

print xp
print
print yp
plt.plot(xp,yp)
plt.savefig("1st order diff by IEM .png")
