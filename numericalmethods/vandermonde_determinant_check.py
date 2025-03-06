import sympy as sp

N = 3
x = sp.symbols(f'x_0:{N+1}')  # Declare x's as symbols

M = sp.Matrix([[sp.exp(j * x[i]) for j in range(N+1)] for i in range(N+1)]) # Make matrix

det = M.det() # Calculate determinant
if (sp.simplify(det) != 0): # Check if determinant isn't zero
    print("Determinant isn't zero")
