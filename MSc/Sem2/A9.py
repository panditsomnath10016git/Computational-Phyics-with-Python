"""COMPUTATIONAL PHYSICS LAB 
    ASSIGNMENT 9
    
 Author : Somnath Pandit ; Date: 15.03.2021
 
"""

import numpy as np


print(50 * "-")
HOLD = input(
    ">>Q1- Find solution of system of equations by Gauss elimination method.\n>> Press enter..."
)

# If the system of equation represented as Ax=B then we can find
# a T by gauss elimination method such that TA = I i.e T = Inv(A)
# Then the solution of equations are x=Inv(A)*B.
# Here instead of finding the inverse explicitly we apply same
# operations simulteneous to A and B  to get TAx = TB >> x= TB
# for this simultatneous opetation we create the augmented matrix.

# The equations are --
# 4*V1 -   V2 -   V3 -   V4 = 5
# -V1  + 3*V2 -   V3 + 0*V4 = 0
# -V1  + 0*V2 + 3*V3 -   V4 = 5
# -V1  -   V2 -   V3  +  V4 = 0

# The Augmented matrix
A = np.array(
    [
        [4, -1, -1, -1, 5],
        [-1, 3, 0, -1, 0],
        [-1, 0, 3, -1, 5],
        [-1, -1, -1, 4, 0],
    ],
    dtype="float",
)

n = len(A[:, 0])  # number of equations

for i in range(n):
    # if the leading element in i-th row is 0, swap rows
    l = i + 1
    while A[i, i] == 0 and l < n:
        A[[i, l], :] = A[[l, i], :]
        l = l + 1
    if A[i, i] == 0:
        print(A)
        raise ValueError("Can't solve, insufficient equations")

    # pick the row and make the leading element 1
    A[i, :] /= A[i, i]
    # substract the picked row from other rows
    for j in range(n):
        if i != j:
            A[j, :] -= A[j, i] * A[i, :]

print("Solutions = ", A[:, -1])

# OUTPUT:
# Solutions =  [3.         1.66666667 3.33333333 2.        ]


print(50 * "-")  # --------------------------------------------------
HOLD = input(
    ">>Q2 - Solve system of equations by Gauss elimination backsubstitution method.\n>> Press enter..."
)

# The Augmented matrix
A = np.array(
    [
        [2, 1, 4, 1, -4],
        [3, 4, -1, -1, 3],
        [1, -4, 1, 5, 9],
        [2, -2, 1, 3, 7],
    ],
    dtype="float",
)

n = len(A[:, 0])  # number of equations

# Convert to upper triangular matrix
for i in range(n):
    # if the leading element in i-th row is 0, swap rows
    l = i + 1
    while A[i, i] == 0 and l < n:
        A[[i, l], :] = A[[l, i], :]
        l = l + 1
    if A[i, i] == 0:
        print(A)
        raise ValueError("Can't solve, insufficient equations")

    # pick the row and make the leading element 1
    A[i, :] /= A[i, i]
    # substract the picked row from bottom rows
    for j in range(i + 1, n):
        A[j, :] -= A[j, i] * A[i, :]
    # print(A)

# Find solutions by back-substitution
sol = np.zeros(n)
for r in range(1, n + 1):
    sol[-r] = A[-r, -1] - np.sum(sol * A[-r, :-1])

print("Upper triangular matrix = \n", A)
print("Solutions = ", sol)

# OUTPUT:
# Upper triangular matrix =
# [[ 1.   0.5  2.   0.5 -2. ]
# [ 0.   1.  -2.8 -1.   3.6]
# [-0.  -0.   1.  -0.  -2. ]
# [-0.  -0.  -0.   1.   1. ]]
# Solutions =  [ 2. -1. -2.  1.]


print(50 * "-")  # --------------------------------------------------
##Q3- statement of the question.
HOLD = input(
    ">>Q3- Find solution of system of equations by Gauss-Jordan method.\n>> Press enter..."
)

# The Augmented matrix
A = np.array(
    [
        [0, 2, 0, 1, 0],
        [2, 2, 3, 2, -2],
        [4, -3, 0, 1, -7],
        [6, 1, -6, -5, 6],
    ],
    dtype="float",
)

n = len(A[:, 0])  # number of equations

for i in range(n):
    # if the leading element in i-th row is 0, swap rows
    l = i + 1
    while A[i, i] == 0 and l < n:
        A[[i, l], :] = A[[l, i], :]
        l = l + 1
    if A[i, i] == 0:
        print(A)
        raise ValueError("Can't solve, insufficient equations")

    # pick the row and make the leading element 1
    A[i, :] /= A[i, i]
    # substract the picked row from other rows
    for j in range(n):
        if i != j:
            A[j, :] -= A[j, i] * A[i, :]

print("Solutions = ", A[:, -1])


# OUTPUT:
# Solutions =  [-0.5         1.          0.33333333 -2.        ]
