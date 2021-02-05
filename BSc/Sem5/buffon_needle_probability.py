from math import *
import numpy as np

n = 100000

x = np.random.rand(n)
angl = (pi / 2) * np.random.rand(n)

anglmax = np.arccos(x)
# print anglmax,angl
cross = 0.0
for i in range(n):
    if angl[i] < anglmax[i]:
        cross += 1
print cross / n
