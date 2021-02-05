import random as rnd
import matplotlib.pyplot as plt

np = 10000  #no. of random numbers
r = [0.0] * np
xi = -1
xf = 2
h = 0.1
x = []
p = []

for i in range(np):
    r[i] = rnd.uniform(xi, xf)

i = xi
k = 0

while i < xf:
    n = 0.0
    for j in range(np):
        if i < r[j] < (i + h):
            n = n + 1
    p.append(n / np)
    x.append(i)
    print("no. between %r and %r= %r\n" % (i, i + h, n))
    i = i + h
    k = k + 1

plt.ylim(ymax=2 * p[0])
plt.plot(x, p)
plt.savefig("random float distribution.png")
