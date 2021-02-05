# Fourier expansion of any function in any range

from pylab import *
from scipy.integrate import quad

######### INPUT ##########
xi, xf = -pi, pi  # function range


def f(x):  # define the function
    if x > 0:
        y = 1.0
    else:
        y = 0.0
    return y


N = 10  # number of fourier series terms

ri, rf = -pi, pi  # range of graph
np = 100  # number of points in graph

ignr = []  # to ignore some  coefft. set n(an,bn)
#########################

l = xf - xi  # periodicity

# defining the kernels
arg = 2 * pi / l


def fnc(x, n):
    return cos(arg * n * x)


def fns(x, n):
    return sin(arg * n * x)


h = (xf - xi) / np  # stepsize of graph
xx = linspace(ri, rf, np)  # x value array
yy = []  # y=f(x) array
A = []
B = []  # coefft. array

print "stepsize = ", h
# first fourier coefficient
s0, err = quad(f, xi, xf)
a0 = s0 / l
# print "a0 = ",a0

for x in xx:
    s = a0

    for n in range(1, N + 1):

        if n in ignr:  # ignore  coefficients
            continue

        # find the coefficient values
        an, err = quad(lambda x: f(x) * fnc(x, n), xi, xf)
        bn, err = quad(lambda x: f(x) * fns(x, n), xi, xf)

        # store the coefficients
        A.append(an * 2 / l)
        B.append(bn * 2 / l)
        
        # sum of the fourier series
        s = s + (2 / l) * (an * fnc(x, n) + bn * fns(x, n))

    yy.append(s)  # value of the function for the x

# plot the function of fourier expansion
plot(xx, yy)
grid()
savefig("fourier series.png")
