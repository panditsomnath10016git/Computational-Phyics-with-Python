# This programme calculates the 1st order energy and wavefunction
#  correction given the wavefunction and energy expression for
#  quantum states.
# It is done for infinte potential box change the parameters
#  accordingly for different problems.
###############################################################

import numpy as np
import matplotlib.pyplot as plt

# ===============================================================
# simpson 1/3 integration module
def simps1_3(ya, xa):
    h = (xa[-1] - xa[0]) / (len(xa) - 1)
    s = ya[0] + 4 * sum(ya[1:-1:2]) + 2 * sum(ya[2:-2:2]) + ya[-1]
    return (h / 3) * s


# ===============================================================


def psi(x, n, L=1):
    # wavefuntion for n-th quantum state
    # L=length of infinte potential well
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)


def H_p(x, L=1):
    # perturbation to the hamiltonian
    g = 10
    return g * (x - L / 2) ** 2  # harmonic oscillator perturbation


def E_(n):
    E_0 = 1.0  # ground state energy
    return n ** 2 * E_0


def H_mn(m, n, x):
    # matrix element of the perturbating potential
    H_mn = simps1_3(psi(x, m) * H_p(x) * psi(x, n), x)
    return H_mn


def psi_p1(x, n):
    # 1st order correction in psi
    n_max = 20  # accuracy of correction upto quantum number
    psi_corr1 = np.zeros(len(x))

    for l in range(1, n_max + 1):
        if l != n:
            a_nl = H_mn(n, l, x) / (E_(n) - E_(l))
            if a_nl > 1e-3:
                print("perptrbation condition failed for n,l=%d,%d" % (n, l))
            psi_corr1 += a_nl * psi(x, l)

    return psi_corr1


L = 1.0
x = np.arange(0, L, 0.00005)  # 0<x<L is the potental region

nn = [1, 2, 3]  # quantum states for calculating perturbation

for n in nn:
    # energy correction
    E_corr1 = H_mn(n, n, x)
    print(
        "Energy upto 1st order corrction = %r+%.4f = %.4f"
        % (E_(n), E_corr1, E_(n) + E_corr1)
    )

    # wavefuntion correction
    psi_n = psi(x, n)
    psi_n_pert = psi_n + psi_p1(x, n)

    plt.plot(x, psi_n, label="original $\psi_%d$" % n)
    plt.plot(x, psi_n_pert, label="perturbed $\psi_%d$" % n)
    plt.title("Perturbation of wavefunction($\psi_%d$) upto 1st order" % n)
    plt.xlabel("x $\longrightarrow$")
    plt.legend(loc="best")
    plt.grid()
    plt.savefig("psi%d_pert.pdf" % n)
    plt.show()
