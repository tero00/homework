import numpy as np

seeds = np.random.randint(0, 10000, size=100)
errors = []

# Calculate error in estimation of pi
# Pi is estimated using Buffon's needle method
for s in seeds:
    np.random.seed(s)
    angles = np.random.rand(100) * 2 * np.pi
    lengths = np.cos(angles) * 2
    positions = np.random.rand(100) * 5
    hits = positions + lengths >= 5
    hit_count = np.sum(hits)
    if hit_count == 0:
        continue  # Skip zero hits to avoid division by zero
    pi_estimate = 0.4 / (hit_count / 100)
    errors.append(abs(pi_estimate - np.pi))

if errors:
    print("Average error in Pi estimation:", np.mean(errors))
else:
    print("No hits recorded, increase sample size.")
