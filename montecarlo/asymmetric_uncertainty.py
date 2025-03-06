import numpy as np
import matplotlib.pyplot as plt
import math

mt = np.random.RandomState() # Mersenne twister

def first_distribution():
    data = np.loadtxt("distr1.dat")     # Load data
    x = data[:,0]   # Extract values for x and y
    y = data[:,1]
    means = []
    for _ in range(1000):   # 1000 means
        samples = []
        while len(samples) < 100:           # 100 samples
            rand_x = mt.rand()*np.max(x)    # Random x
            rand_y = mt.rand()*np.max(y)    # Random y
            rand = np.interp(rand_x, x, y)  # Interpolate to get y of rand_x
            if rand_y < rand:               # If under the curve...
                samples.append(rand_x)      # ...append
        means.append(np.mean(samples))      # Add mean of samples to array     
    return np.array(means)    # Return array

def poisson_distribution(x_max=10,y_max=0.25):  # Mostly identical to first_distribution()
    means = []
    for _ in range(1000):
        samples = []
        while len(samples) < 100:       
            rand_k = int(mt.rand()*x_max)   
            rand_y = mt.rand()*y_max        
            if rand_y < (3**rand_k*np.exp(-3))/math.factorial(rand_k):  # Check if under curve of Poisson function
                samples.append(rand_k)      
        means.append(np.mean(samples))
    return np.array(means)

def asymmetric_uncertainty(means):      
    middle = np.median(means)   # Find median value
    lower_bound = np.percentile(means, 16)      # Find lower bound of 1sigma
    upper_bound = np.percentile(means, 84)      # And upper bound
    uncertainty_lower = middle - lower_bound    # Uncertainty down
    uncertainty_upper = upper_bound - middle    # Uncertainty up
    return (uncertainty_lower+uncertainty_upper)/2  # Return average uncertainty for comparison

def symmetric_uncertainty(means):
    mean = np.mean(means)
    means = np.array(means)
    return np.sqrt((1/len(means))*sum((means-mean)**2)) # Return uncertainty


means = first_distribution()
print("Asymmetric uncertainty of first distribution: "+str(asymmetric_uncertainty(means)))
print("Gaussian uncertainty of first distribution: "+str(symmetric_uncertainty(means)))
means = poisson_distribution()
print("Asymmetric uncertainty of poisson distribution: "+str(asymmetric_uncertainty(means)))
print("Gaussian uncertainty of poisson distribution: "+str(symmetric_uncertainty(means)))

