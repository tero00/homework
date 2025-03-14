import numpy as np

def adaptive_simpsons(func, a, b, tol=10e-6): 
    integral = simpsons(func, a, b)         # Compute initial Simpson's rule approximation
    error = 1
    subdivisions = 2                        # Start with 2 subdivisions
    while abs(error) > tol:                 # Loop until error < tolerance 
        intervals = np.linspace(a, b, 2**subdivisions)  # Generate equally spaced interval endpoints
        finer_integral = sum([simpsons(func, intervals[i], intervals[i+1]) for i in range(2**subdivisions-1)])  # Sum Simpson's approximations over each subinterval
        error = finer_integral - integral   # Calculate error
        integral = finer_integral           # Update the integral approximation with the refined value
        subdivisions += 1                   # Increase the number of subdivisions for the next iteration
    return integral                         # Return the final, refined integral approximation

def simpsons(func, a, b):  # Simpson's rule
    return ((b-a)/6)*(func(a)+4*func((a+b)/2)+func(b))  

def f(x): 
    return np.exp(-x)*np.cos(x)**2 

def f_t(t): 
    return (np.exp(-(t/(1-t)))*np.cos(t/(1-t))**2)/(1-t)**2  # x = t/(1-t)

def gauss_laguerre(g, n): 
    nodes, weights = np.polynomial.laguerre.laggauss(n) # Get Gauss-Laguerre nodes and weights for integration
    return np.sum(weights * g(nodes))                   # Calculate the weighted sum approximation using the nodes

def g(x):  # Define function g(x) for Gauss-Laguerre quadrature
    return np.cos(x)**2  

print("f(x):   "+str(adaptive_simpsons(f, 0, 1000)))  
print("f_t(x): "+str(adaptive_simpsons(f_t, 0, 0.999))) 
print("Gauss-Laguerre, n=2:  "+str(gauss_laguerre(g, 2)))
print("Gauss-Laguerre, n=4:  "+str(gauss_laguerre(g, 4)))
print("Gauss-Laguerre, n=8:  "+str(gauss_laguerre(g, 8)))
