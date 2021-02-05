# pylint:disable=W0312
from math import *
import numpy as np
import matplotlib.pyplot as plt

print "t, T , p , 1/T , ln(p)"
k = 0
x = []
y = []
t = np.arange(70, 35, -2.5)
t[-1] = 39.5
print t

while k < 23:
    i = 5.0
    try:
        v = input("V = ")
    except:
        break
    T = t[k] + 273
    t1 = 1000.0 / T
    p = 0.1 * v / i
    lr = log(p)
    print t[k], T, p, t1, lr
    x.append(t1)
    y.append(lr)
    k = k + 1
    print

plt.plot(x, y, ".")
plt.savefig("aaasgh.png")
