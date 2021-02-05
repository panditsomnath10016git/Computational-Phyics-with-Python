import numpy as np
import matplotlib.pyplot as plt

Na = 6.022e23  # Avogadro number
Kb = 8.314 / Na  # Boltzmann constant

n = 1000  # no of points in graph
T = np.array([400, 300, 100])  # temp for distribution
t = np.max(T)
kt = Kb * t
E0, Ef = 0, 2 * kt  # range of energy in plot

E = np.linspace(E0, Ef, n).reshape(n, 1)
kT = Kb * T

# Maxwell-Boltzman energy distribution function
MB = 2 * ((E / np.pi) ** 0.5) * (kT ** -1.5) * np.exp(-E / kT)

# rescaling values for graph
E = E / kt
P = MB / np.max(MB)

# plotting the graph
plt.plot(E, P)
plt.title("M-B energy distribution")
plt.xlabel("E/kT $\longrightarrow$")
plt.ylabel("P(E) $\longrightarrow$")
ref = ["%r K" % t for t in T]
plt.legend(ref)
plt.grid()
plt.savefig("MB energy distribution.png")
