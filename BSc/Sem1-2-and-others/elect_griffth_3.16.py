# Electromagnetism Griffith problem3.16
from math import *
import matplotlib.pyplot as plt

l = 2.0  # specify the box
x = l / 2
y = l / 2
z = l / 2

N = 50
s = 0.0
for n in range(1, N, 2):
    for m in range(1, N, 2):
        k1 = n * pi / l
        k2 = m * pi / l
        p = (k1 ** 2 + k2 ** 2) ** 0.5
        s = (
            s 
            + (1.0 / n * m) 
            * (sinh(p * z)) 
            * sin(k1 * x) 
            * sin(k2 * y) 
            / (sinh(p * l))
        )

v = 16 * s / pi ** 2
print (v, 1.0 / 6)
