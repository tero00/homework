import numpy as np

def broyden(x_init, i_max=100, tol=1e-8): # Arbitrary i_max and tolerance
    x = np.array(x_init)    # Make x into a numpy array
    B = np.eye(len(x))      # Identity matrix as initial guess for inverted Jacobian
    for _ in range(i_max):  # Iterate
        f = np.array([f1(x), f2(x)])    # Current correction values
        x_last = x.copy()   # Make copy
        x = x - B @ f       # Update x
        s = x - x_last      # How much x changed
        y = np.array([f1(x), f2(x)]) - np.array([f1(x_last), f2(x_last)]) # y for next step
        B = B + np.outer((s - B @ y), s) / (s.T @ B @ y)    # Update inverted Jacobian
        if np.linalg.norm(f) < tol:  # If below tolerance, stop
            break
    return x  

def f1(x):  # Function 1
    return np.exp(-(x[0]**2 + x[1]**2)) - 1/8

def f2(x):  # Function 2
    return np.sin(x[0]) - np.cos(x[1])

print("Broyden:", broyden([1.0, 1.0])) # Call function with initial guesses