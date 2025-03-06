import numpy as np
from scipy.linalg import eigvals

def myroots(N, p):
    p = np.array(p, dtype=float) # Make into a numpy array
    A = np.eye(N-1, k=1)         # Make identity matrix but shifted right
    A[-1, :] = -p[:-1] / p[-1]   # Make bottom row of matrix the coefficients of the polynomial
    return eigvals(A)            # return eigenvalues

p = [-6, 11, -6, 1] # Third degree polynomial
N = len(p)

roots_eigenvalues = myroots(N, p)
print("myroots: ", np.sort(roots_eigenvalues))

roots_np = np.roots(p[::-1])  # Need to reverse p because np.roots wants highest degree first
print("np.roots:", np.sort(roots_np))