import numpy as np
from scipy.special import legendre
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

p1 = legendre(5)
print p1(0.5)


plt.plot(x, p1(x))
plt.show()
