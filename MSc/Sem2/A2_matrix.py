""" COMPUTATIONAL PHYSICS LAB 
     SPRING SEM ,2021
     ASSIGNMENT 2
        
     Author : Somnath Pandit , Date : 20.01.2021
    
This program creates two matrices A & B of a given dimension such that A_ij=(i+1)x(j+1), B_ij=(i+j) and multiply them
 
"""
import numpy as np

# defining the matrix multiplication
def matmul(A, B):
    n = len(A)
    M = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += A[i][k] * B[k][j]
    return M


n = int(input("Dimension of matrix= "))  # Taking the dimension as input

A = np.zeros((n, n))  # creating matrices..
B = np.zeros((n, n))  # ..filled with zero

# Building the required matrices A & B
for i in range(n):
    for j in range(n):
        A[i][j] = (i + 1) * (j + 1)
        B[i][j] = i + j


M = matmul(A, B)  # result of multiplication

print("A =\n", A, "\n \n B =\n", B, "\n \n AxB =\n", M)
