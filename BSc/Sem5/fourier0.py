# Fourier expansion of any function in any range

from pylab import *
from scipy.integrate import quad


def f(x):
    if x < 0:
        y = 0.0
    else:
        y = 1.0
    return y


N = 20  # number of fourier terms
xi = -1.0
xf = 1.0  # function range
l = 2.0  # periodicity


ri = -2.0  # range of graph
rf = 2.0

h = 0.005  # stepsize
xx = arange(ri, rf + h, h)
yy = []

# first fourier coefficient
s0, e1 = quad(lambda x: f(x), xi, xf)
a0 = s0 / l
#print s0

for x in xx:
    s = a0
    # 	print x
    for n in range(1, N + 1):

        arg = 2 * n * pi / l
        
        # find the coefficient value
        an, e2 = quad(lambda x: f(x) * cos(arg * x), xi, xf)
        bn, e2 = quad(lambda x: f(x) * sin(arg * x), xi, xf)
        
        # sum of the fourier series
        s = s + (2 / l) * (an * cos(arg * x) + bn * sin(arg * x))
 		#print an,bn,s
    yy = append(yy, s)

# plot the function of fourier expansion
plot(xx, yy)
grid()
savefig("fourier series.png")
