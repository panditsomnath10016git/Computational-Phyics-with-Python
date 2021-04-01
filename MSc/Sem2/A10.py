"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 10
    
 Author : Somnath Pandit ; Date: 23.03.2021
 
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


print(50 * "-")
HOLD = input(
    ">>Q1- Solving laplace equation with Jacobi relaxation method.\n>> Press enter..."
)


def set_boundary_cond1(V):
    n = len(V[0, :])
    for i in [0, n - 1]:  # Potential at all boundaries is 0 except..
        V[i, 0:n] = 0
        V[1 : n - 1, i] = 0
    V[-1, :] = 1.0  #  at top wall potential is 1.0

    return V


def solve_laplace_by_J_rlx(potential):
    V = potential.copy()
    V[1:-1, 1:-1] = (1.0 / 4) * (
        V[0:-2, 1:-1] + V[2:, 1:-1] + V[1:-1, 0:-2] + V[1:-1, 2:]
    )
    return V


n = 10  # Grid division along one direcion
eps = 1e-6  # Accuracy of solution
V = 0.5 * np.ones((n, n), float)  # Inital guess..
V = set_boundary_cond1(V)  # ..with boundary conditions
# print(V)

err = 1.0  # Loop initiator
while err > eps:
    V_p = solve_laplace_by_J_rlx(V)
    err = np.max(abs(V_p - V))
    V = V_p


# Pseudo-color Plot
plt.imshow(V, cmap="bone")
plt.title(
    "Electrostatic potential(V) in an empty box with all walls grounded\nexcept the top one with V = 1.0"
)
plt.xlim(0, n - 1)
plt.ylim( 0,n-1)
plt.xlabel("<-- width -->")
plt.ylabel("height -->")
plt.savefig("A10_Q1.png")
plt.show()



print(50 * "-")#--------------------------------------------------
HOLD = input(
    ">>Q2- Solving poission equation with Jacobi relaxation method.\n>> Press enter..."
)
def set_boundary_cond2(V):
    n = len(V[0, :])
    for i in [0, n - 1]:  # Potential at all boundaries is 0
        V[i, 0:n] = 0
        V[1 : n - 1, i] = 0

    return V


def solve_poission_by_J_rlx(potential, rho, a):
    V = potential.copy()
    epsilon = 1.0
    V[1:-1, 1:-1] = (1.0 / 4) * (
        V[0:-2, 1:-1]
        + V[2:, 1:-1]
        + V[1:-1, 0:-2]
        + V[1:-1, 2:]
        + a ** 2 * rho[1:-1, 1:-1] / epsilon
    )

    return V


f = 1  # inverse of grid unit
n = 100 * f + 1  # Grid points along one direction
eps = 1e-5  # Accuracy of solution

# Potential
V = np.zeros((n, n), float)
V = set_boundary_cond2(V)  # Initial guess with boundary conditions

# Charge density
Rho = np.zeros((n, n), float)
Rho[20 * f, 20 * f] = 1.0
Rho[80 * f, 80 * f] = -1.0


err = 1.0  # Loop initiator
while err > eps:
    V_p = solve_poission_by_J_rlx(V, Rho, 1.0 / f)
    err = np.max(abs(V_p - V))
    V = V_p


# Pseudo-color plot
plt.imshow(V, cmap="bone", origin="lower")
plt.title(
    "Electristatic potential in a box with all walls grounded\n and +1,-1 charges at (20,20),(80,80)"
)
plt.xlabel("$x \longrightarrow$")
plt.ylabel("$y \longrightarrow$")
plt.savefig("A10_Q2.png")
plt.show()



print(50 * "-")#--------------------------------------------------
HOLD = input(
    ">>Q3- Solve laplace equation using Gauss-Seidal relaxation method.\n>> Press enter..."
)
def set_boundary_cond3(V, f):
    n = len(V[0, :])
    for i in [0, n - 1]:
        V[i, 0:n] = 0
        V[1 : n - 1, i] = 0
        
    V[20 * f : 80 * f, 20 * f] = 1.0
    V[20 * f : 80 * f, 80 * f] = -1.0

    return V


def solve_laplace_by_GS_rlx(potential, f):
    V = potential.copy()
    
    for i in [1, 2]:  # calculate on odd grid-points
        V[i:-1:2, i:-1:2] = (
            V[i - 1 : -2 : 2, i:-1:2]
            + V[i + 1 :: 2, i:-1:2]
            + V[i:-1:2, i - 1 : -2 : 2]
            + V[i:-1:2, i + 1 :: 2]
        ) / 4
    for i, j in zip([1, 2], [2, 1]):  # calculate on even grid-points
        V[i:-1:2, j:-1:2] = (
            V[i - 1 : -2 : 2, j:-1:2]
            + V[i + 1 :: 2, j:-1:2]
            + V[i:-1:2, j - 1 : -2 : 2]
            + V[i:-1:2, j + 1 :: 2]
        ) / 4

    V = set_boundary_cond3(V, f)

    return V


f = 1  # grid multiplier(integer)
n = 100 * f + 1  # Grid points along one direcion
eps = 1e-6  # Accuracy of solution

# Potential
V = np.ones((n, n), float)  # Inital guess with..
V = set_boundary_cond3(V, f)  # ..boundary conditions


err = 1.0  # Loop initiator
while err > eps:
    V_p = solve_laplace_by_GS_rlx(V, f)
    err = np.max(np.abs(V_p - V))
    V = V_p


# Pseudo-color plot
plt.imshow(V, cmap="bone", origin="lower")
plt.title(
    "Electrostatic potential in a box with all walls grounded\n and capacitor plates with potential +1,-1 V "
)
plt.tight_layout()
plt.savefig("A10_Q3.png")
plt.show()

##3D plot
g = np.linspace(0, 100, n)
X, Y = np.meshgrid(g, g)

fig = plt.figure()
ax = fig.gca(projection="3d")
# ax.view_init(20)
ax.set_title(
    "Electrostatic potential in a box with all walls grounded\n and capacitor plates with potential +1,-1 V "
)
plot = ax.plot_surface(
    X,
    Y,
    V,
    rstride=2,
    cstride=2,
    cmap="coolwarm",
    linewidth=0.4,
)
ax.set_xlabel("$x \\rightarrow$")
ax.set_ylabel("$y \\rightarrow$")
ax.set_zlabel("$V(x,y) \\rightarrow$")
fig.tight_layout()
plt.savefig("A10_Q3_3d.svg")
plt.show()




print(50 * "-")#--------------------------------------------------
HOLD = input(
    ">>Q3- Solve heat equation by FTCS method.\n>> Press enter..."
)


def set_initial_cond(T, Tl, Tm, Tr):
    T[0] = Tl
    T[1:-1] = Tm
    T[-1] = Tr

    return T


def FTCS(Temp, k):
    T = np.copy(Temp)
    T[1:-1] = T[1:-1] + k * (T[0:-2] + T[2:] - 2 * T[1:-1])

    return T


w = 1.0e-2  # Thickness of container(m)
Tl, Tm, Tr = 50.0, 20.0, 0.0  # left, middle, right temperatures
D = 4.25e-6  # diffusion coefficient(m^2.s^-1)

dt = 1e-5  # time step
t_need = np.array([0.01, 0.1, 0.4, 1.0])  # plot solution at time(s)

N = 101  # no of grid points
a = w / N  # grid unit

T = np.empty(N, float)
T = set_initial_cond(T, Tl, Tm, Tr)  # initial temp profile
X = np.linspace(0, w * 100, N)

t = 0.0
k = dt * D / a ** 2

while t < max(t_need):
    T_p = FTCS(T, k)
    T = T_p

    # plot the solution at needed time
    if min(abs(t_need - t)) < dt / 2:
        plt.plot(X, T, label="t = %.2f s" % t)

    t += dt


plt.title("Temperature profile at different times, solved by FTCS method")
plt.xlabel("$x(cm) \longrightarrow$")
plt.ylabel("$Temperature \longrightarrow$")
plt.grid()
plt.legend()
plt.savefig("A10_Q4.svg")
plt.show()

