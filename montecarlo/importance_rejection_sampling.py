import numpy as np
import matplotlib.pyplot as plt

def analytical(n):  # Analytical sampling for comparison
    x = []  # Make list
    while len(x) < n:
        x.append(2 * np.tan(np.pi * (mt.rand() - 0.5))) # Add inverse CDF variable to list
    x_np = np.array(x)  # Convert to np array for filtering
    return x_np[np.abs(x_np) <= 10.0] # Return only values closer to zero than 10

def box_muller(mean=0, sd=2):   # Generate Gaussian point
    u1, u2 = mt.rand(), mt.rand()   # Box-Muller random variables
    z = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2) # Calculate Z
    return mean + sd * z    # Return Z

def rejection(n, mean=0, sd=2, c=1):
    samples = []    # Make List
    while len(samples) < n: # Loop until n datapoints
        x = box_muller(mean, sd)    # Get a Gaussian point for comparison
        ceil = (4 / (x**2 + 4)) / (c * (1 / (np.sqrt(2 * np.pi) * sd) * np.exp(-0.5 * ((x - mean) / sd)**2)))   # Calculate max allowed value
        if mt.rand() < ceil:    # If value lower than max allowed:
            samples.append(x)   # Append to list
    return np.array(samples)    # Return samples

mt = np.random.RandomState() # Mersenne twister

points = 100000 # Amount of generated points
sample_analytical = analytical(points) # Analytical distribution
sample_rejection = rejection(points) # Analytical + rejection distribution

plt.hist(sample_analytical, bins=100, density=True, alpha=0.5, label="Analytical")
plt.hist(sample_rejection, bins=100, density=True, alpha=0.5, label="Analytical + rejection")
plt.xlabel('x')
plt.ylabel('Probability density')
plt.legend()
plt.show()