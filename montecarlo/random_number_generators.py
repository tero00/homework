import numpy as np
import random

def LCG(seed, n): # Linear congruent generator
    numbers = []
    num = seed
    for i in range(n):
        num = (113829761 * num + 48582261) % 113829760
        yield num/113829760

def ParkMillerSchrage(seed, n):     # LCG using Park-Miller parameters and Schrage algorithm
    numbers = []
    num = seed
    m = 2**31-1
    q = (m//16807)
    r = m%16807
    for i in range(n):
        k = num//q
        num = 16807 * (num - k * q) - r * k
        if num < 0:
            num += m
        yield num/m

def MT(seed, n):    # Mersenne Twister for comparison
    random.seed(seed)
    for i in range(n):
        yield random.random()

def period(gen):
    try:
        first = next(gen)
    except StopIteration:
        return 0
    count = 1
    for num in gen:
        if num == first:
            return count
        count += 1
    return "No period found in given range"

if __name__ == "__main__":
    pass

