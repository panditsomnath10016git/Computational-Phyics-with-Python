import numpy as np
import matplotlib.pyplot as plt

""" From semi empirical mass formula find the mass no ar proton drip line"""


Ai, Af = 10, 200  # min and max A values for plot
n = 10000
A = np.linspace(Ai, Af, n)
N = 68  # N value --constant

# Binding energy terms diiferentiated with respect to A at const N
vol = 15.56
sur = -17.23 * (2.0 / 3) * A ** (-1.0 / 3)
col = -0.72 * A ** (-4.0 / 3) * (5 * A ** 2 - 2 * A * (2 * N + 1) - N * (N + 1)) / 3
asym = -23.28 * (1 - 4 * (N ** 2 / A ** 2))

db_da_N = vol + sur + col + asym

# Value of A at db_da_N=0
A_at_dbda0 = A[np.argmin(np.abs(db_da_N))]

# plotting the graph
plt.plot(A, db_da_N, A_at_dbda0, 0, "o")
plt.annotate("(%d,0)" % A_at_dbda0, xy=(A_at_dbda0, 0), xycoords="data")
plt.xlabel("A $\longrightarrow$")
plt.ylabel(
    "$\left(\\frac{\partial (BE)}{\partial A}\\right)_{N=const} \longrightarrow$",
    fontsize=15,
)
plt.ylim(-50, 50)
plt.grid()
plt.tight_layout()
plt.savefig("proton drip line.png")
plt.show()
