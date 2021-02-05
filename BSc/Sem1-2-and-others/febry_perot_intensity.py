import math as m
import matplotlib.pyplot as plt

f = 80
xmax = 25.28
np = 1000
h = xmax / np
yt = [0.0] * np
yr = [0.0] * np
x = [0.0] * np

for i in range(np):
    delt = x[i] = 0.0 + i * h
    yt[i] = 1 / (1 + f * m.sin(delt / 2) ** 2)
    yr[i] = f * m.sin(delt / 2) ** 2 / (1 + f * m.sin(delt / 2) ** 2)

plt.plot(x, yr)
plt.savefig("intensity distribution.png")
