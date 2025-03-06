from math import floor

def vdc(index, b):  # Simple van der corput pseudo random sequence
    result = 0
    f = 1
    i = index
    while i > 0:
        f = f / b
        result = result + f * (i % b)
        i = floor(i/b)
    return result



if __name__ == "__main__":
    for n in range(10):
        print(vdc(n,7))

