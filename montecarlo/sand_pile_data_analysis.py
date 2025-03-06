import matplotlib.pyplot as plt
import numpy as np
# Sand pile data analysis

data = np.loadtxt("statistics.dat", skiprows=1) # Load data
grain, ntopple, hsum, hmax = data.T

ntopple = ntopple.astype(int)
topple_max = np.max(ntopple)    # Get biggest topple
Ns = np.zeros(topple_max + 1)   # Initiate arrays
s = list(range(topple_max + 1))

# Count topples
for i in ntopple:
    Ns[i] += 1

# Choose interval between 50 and 150
s_interval = np.array(s[50:150])
Ns_interval = np.array(Ns[50:150]) 

k, b = np.polyfit(np.log(s_interval), np.log(Ns_interval), 1)   # Fit curve

print("alpha =", -k)
plt.scatter(s, Ns, s=20)
plt.xlabel("s")
plt.ylabel("N(s)")
plt.grid(True)
plt.loglog()
plt.show()