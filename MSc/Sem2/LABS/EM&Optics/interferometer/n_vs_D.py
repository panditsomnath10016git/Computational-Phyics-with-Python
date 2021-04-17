import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt

# import data from file
data = np.loadtxt("D_n.txt")
n_data = data[:,0]
D_data = data[:,1]

n_fit = np.arange(min(n_data), max(n_data)+ .1, .1)
D_fit = poly.polyval(n_fit, poly.polyfit(n_data,D_data, 1))

slope= 1e-3*(D_fit[0]-D_fit[1])/(n_fit[0]-n_fit[1])

plt.plot(n_data, D_data, ".")
plt.plot(n_fit, D_fit)
plt.title("Plot of n vs. D")
plt.xlabel("n $\longrightarrow$")
plt.ylabel("D$(\\times 10^{-3} mm)\ \longrightarrow$")
plt.text(25, 4, "slope = %f "%slope)
plt.grid()
plt.savefig("D_n.pdf")
plt.show()

