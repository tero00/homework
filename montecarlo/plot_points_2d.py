import random_number_generators as rng
import matplotlib.pyplot as plt

# Helper function to generate points
def create_points(gen, total_points):
    points = []
    try:
        for _ in range(total_points):
            points.append((next(gen), next(gen)))
    except StopIteration:
        pass
    return points

# Generate points using each RNG method
num_points = 20000
LCG_points = create_points(rng.LCG(123, num_points * 2), num_points)
PMS_points = create_points(rng.ParkMillerSchrage(123, num_points * 2), num_points)
MT_points = create_points(rng.MT(123, num_points * 2), num_points)

# Plotting
fig, axs = plt.subplots(1, 3, figsize=(12, 3.5))
methods = ['LCG', 'Park-Miller Schrage', 'Mersenne Twister']
data = [LCG_points, PMS_points, MT_points]

for ax, points, method in zip(axs, data, methods):
    x, y = zip(*points)
    ax.scatter(x, y, s=2, alpha=0.5)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(method)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.show()
