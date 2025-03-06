import numpy as np

mt = np.random.RandomState() # Mersenne twister

def volume(d, n=1000000):
    hits = 0 # How many points land in designated volume
    for _ in range(n):
        rand_point = np.array([mt.rand() for _ in range(d)])    # Generate point
        if np.sqrt(np.sum(rand_point**2)) < 1:  # If point in one symmetric part of hypersphere
            hits += 1   # Increment
    p = hits/n  # Probability of landing in area
    sigma = p*2**d*np.sqrt((p*(1-p))/n) # Uncertainty
    return (p*2**d, sigma, n)  # Return area and uncertainty

dimensions = 10

vol = volume(dimensions)
print(f"Approximate volume of hypersphere in {dimensions} dimensions ({vol[2]} points): {vol[0]} ± {vol[1]}")