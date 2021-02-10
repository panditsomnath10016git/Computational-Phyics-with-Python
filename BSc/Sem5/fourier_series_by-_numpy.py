from pylab import *

# from scipy.integrate import simps,trapz

#######**** INPUT ****########==================================

ri, rf = -1.0, 1.0  # function range


def f(x):  # define the function such that argument is a numpy array
    np = len(x)
    y = zeros(np)

    for i in range(np):
        if x[i] < 0.0:
            y[i] = -1.0
        else:
            y[i] = 1.0
    return y


N = 5  # number of fourier series terms

nint = 10001  # number of points in integration (odd for simpson1_3 ,even for trapizoidal integration)

xi, xf = -1.0, 1.0  # range of graph
np = 1000  # number of points in graph

ignr = [0]  # to ignore  coefft.s [n's'], otherwise [0]

#===============================================================

# simpson 1/3 integration module
def simps1_3(ya, xa):
    h = (xa[-1] - xa[0]) / (len(xa) - 1)
    s = ya[0] + 4 * sum(ya[1:-1:2]) + 2 * sum(ya[2:-2:2]) + ya[-1]
    return (h / 3) * s


# trapizoidal integration module
def trpzd(ya, xa):
    h = (xa[-1] - xa[0]) / (len(xa) - 1)
    s = ya[0] + 2 * sum(ya[1:-1]) + ya[-1]
    return (h / 2) * s


l = rf - ri  # periodicity
arg = 2 * pi / l
h = (xf - xi) / np  # stepsize of graph
xx = linspace(xi, xf, np)  # x value array for graph
xint = linspace(ri, rf, nint)  # x value for integration
yy = []  # y=f(x) array
A = zeros(N)
B = zeros(N)  # coefft. array

print "stepsize = ", h

# first fourier coefficient
a0 = simps1_3(f(xint), xint) / l
print "a0 = ", a0
nn = arange(1, N + 1)

# print nn
for n in nn:
    if n in ignr:  # skipping the ignored coefft.s
        continue
    yc = f(xint) * cos(arg * n * xint)
    ys = f(xint) * sin(arg * n * xint)
    A[n - 1] = (2 / l) * simps1_3(yc, xint)  # integration for..
    B[n - 1] = (2 / l) * simps1_3(ys, xint)  # ..coefficients

# print "an=", A ,"\n bn=",B
# summing the series for each x point
for x in xx:
    s = 0.0
    argn = 2 * pi * nn * x / l
    Cosn = cos(argn)
    Sinn = sin(argn)
    s = a0 + sum(A * Cosn + B * Sinn)
    yy.append(s)
# print len(A),len(Cosn),len(yy),  s

# plotting the function graph
# plot(xx,yy)
# grid()

# plotting the coefficents
bar(nn, B, width=0.2)
xticks(nn, size=6)
yticks(B, size=4)
savefig("fourier_numpy.png")
