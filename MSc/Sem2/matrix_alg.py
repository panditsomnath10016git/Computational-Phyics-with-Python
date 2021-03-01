import numpy as np


def Inv(M):
    """
    Calculate inverse of matrix by Gauss elimination method.

    Parameters
    ------------
    M : numpy array
        Marix to be inverted.

    Returns
    ---------
    matrix : numpy array
        inverse of matrix M.
    """

    n = len(M[0, :])
    I = np.eye(n)
    # The Augmented matrix
    A = np.concatenate((M, I), axis=1)

    for i in range(n):
        # if the leading element in i-th row is 0, swap rows
        l = i + 1
        while A[i, i] == 0 and l < n:
            A[[i, l], :] = A[[l, i], :]
            l = l + 1
        if A[i, i] == 0:
            print(A)
            raise ValueError("Can't find Inverse, Det(A)=0")

        # pick the row and make the leading element 1
        A[i, :] /= A[i, i]
        # substract the picked row from other rows
        for j in range(n):
            if i != j:
                A[j, :] -= A[j, i] * A[i, :]
    return A[:, n::]


# m=np.array([[1,2],[3,7]])
# n=Inv(m)
# print(n,np.matmul(m,n))
