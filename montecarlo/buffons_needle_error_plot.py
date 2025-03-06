import matplotlib.pyplot as plt
import numpy as np

def needles(n):
    angles = np.random.uniform(0, 2*np.pi, n)
    positions = np.random.uniform(0, 5, n)
    lengths = np.cos(angles)*2
    hits = positions + lengths >= 5
    hit_count = np.sum(hits)
    if hit_count == 0:
        pi = 0
    else: pi = 0.4/(hit_count/n)
    return abs(pi - np.pi)

def error(n):
    errors = [needles(n) for i in range(100)]
    return np.mean(errors)

samples = [10, 100, 1000, 10000, 100000, 1000000]
results = [error(n) for n in samples]

plt.plot(samples, results)
plt.xlabel("Number of Needles")
plt.ylabel("Average Error")
plt.xscale('log')
plt.yscale('log')
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%0.4f'))
plt.grid(True)

plt.show()