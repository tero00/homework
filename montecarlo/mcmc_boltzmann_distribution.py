import matplotlib.pyplot as plt
import numpy as np
import time
import numba # numba for a reasonable execution time


@numba.njit 
def mbd(E, k=8.6173324e-5, T=300):
    return np.exp(-E/(k*T))*(2/np.sqrt(np.pi))*((np.sqrt(E))/(k*T)**(3/2)) # Maxwell-Boltzmann distribution

@numba.njit
def markovchain(N, dE_max, x_init=0.1): # Markov chain algorithm
    burn_in = int(N*0.1)
    N = N + burn_in
    chain = np.empty(N)
    x = x_init
    i = 0
    while N > 0:    
        r = mbd(x)
        u = np.random.rand()*2 - 1
        x_new = x + u*dE_max
        r_new = mbd(x_new)
        if r_new > r or r_new > np.random.rand()*r:
            x = x_new
            chain[i] = x
            N -= 1
            i += 1
    return chain[burn_in:]

def rms(markovchain, dE_max_array, N):
    errors = []
    for i in dE_max_array:  # Loop through dE_max values
        means = []
        for _ in range(10): # Get 10 means
            means.append(np.mean(markovchain(N,i)))
        means = np.array(means)     # Make into a numpy array
        errors.append(np.sqrt(sum((means-0.0387779958)**2)/len(dE_max_array)))  # Assemble error array
    return errors

def find_dE_max(interval, num, N):  # Find optimal dE_max
    dE_max_array = [i*interval for i in range(num)]     # Make array for test dE_maxes
    plt.scatter([i*interval for i in range(num)], rms(markovchain, dE_max_array, N))
    plt.title("stepsize: "+str(interval)+" steps: "+str(num)+" samples for one mean: "+str(N))
    plt.grid()
    plt.show()

def plot_N():   # Plot errors for different values of N 
    errors_for_N = []
    for i in range(2,9):
        errors_for_N.append(rms(markovchain, [0.03], 10**i))
    plt.figure(figsize=(8,6))
    plt.scatter([10**i for i in range(2,9)], errors_for_N)
    plt.ylabel("Error")
    plt.xlabel("N")
    plt.loglog()
    plt.grid()
    plt.show()

start = time.time()

find_dE_max(0.001, 100, 500)
plot_N()

stop = time.time()
print(stop - start)