""" From semi empirical mass formula find the mass number at neutron & proton drip line"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
A_v = 15.56
A_s = 17.23
A_c = 0.72
A_a = 23.28
A_p = 12

Ai, Af = 10, 200  # min and max A values for graph
n = 10000  # No of points for graph
A = np.linspace(Ai, Af, n)
Z = 50.0  # Z value --constant
N = 68.0  # N value --constant


### Neutron drip line
# Binding energy terms diiferentiated with respect to A at const Z
vol = A_v
sur = -A_s * (2.0 / 3) * A ** (-1.0 / 3)
col = A_c * Z * (Z - 1) * A ** (-4.0 / 3) / 3
asym = -A_a * (1 - 4 * (Z ** 2 / A ** 2))

db_da_Z = vol + sur + col + asym

# Value of A at db_da_Z=0
A_at_dbdaZ0 = A[np.argmin(np.abs(db_da_Z))]


### Proton drip line
# Binding energy terms diiferentiated with respect to A at const N
vol = A_v
sur = -A_s * (2.0 / 3) * A ** (-1.0 / 3)
col = -A_c * A ** (-4.0 / 3) * (5 * A ** 2 - 2 * A * (2 * N + 1) - N * (N + 1)) / 3
asym = -A_a * (1 - 4 * (N ** 2 / A ** 2))

db_da_N = vol + sur + col + asym

# Value of A at db_da_N=0
A_at_dbdaN0 = A[np.argmin(np.abs(db_da_N))]


# Plotting the graph for neutron dripline
plt.plot(A, db_da_Z, A_at_dbdaZ0, 0, "o")
plt.annotate("(%d,0)" % A_at_dbdaZ0, xy=(A_at_dbdaZ0, 0), xycoords="data")
plt.xlabel("A $\longrightarrow$")
plt.ylabel(
    "$\left(\\frac{\partial (BE)}{\partial A}\\right)_{Z=const} \longrightarrow$",
    fontsize=15,
)
plt.ylim(-50, 50)
plt.grid()
plt.tight_layout()
# plt.savefig("neutron_dripline.png")
plt.show()

# Plotting the graph for proton dripline
plt.plot(A, db_da_N, A_at_dbdaN0, 0, "o")
plt.annotate("(%d,0)" % A_at_dbdaN0, xy=(A_at_dbdaN0, 0), xycoords="data")
plt.xlabel("A $\longrightarrow$")
plt.ylabel(
    "$\left(\\frac{\partial (BE)}{\partial A}\\right)_{N=const} \longrightarrow$",
    fontsize=15,
)
plt.ylim(-50, 50)
plt.grid()
plt.tight_layout()
# plt.savefig("proton_dripline.png")
plt.show()
