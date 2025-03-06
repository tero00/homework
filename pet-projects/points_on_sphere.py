import numpy as np
import matplotlib.pyplot as plt

N = 2000
theta = np.random.rand(N)*np.pi*2
phi = np.random.rand(N)*np.pi-np.pi/2
x = np.sin(theta)*np.cos(phi)
y = np.cos(theta)*np.cos(phi)
z = np.sin(phi)

# Visualize how density is higher around the poles
ax1 = plt.figure().add_subplot(projection='3d')
ax1.scatter(x, y, z, s=1, c='blue', alpha=0.6)
ax1.set_box_aspect([1, 1, 1])
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

plt.show()
