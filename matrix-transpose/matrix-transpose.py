import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)

    A_t = []

    for j in range(A.shape[1]):
        A_t.append(
            [A[i][j] for i in range(A.shape[0])]
        )

    return np.array(A_t)
