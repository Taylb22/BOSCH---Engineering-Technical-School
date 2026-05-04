import numpy as np
from math import pi, sqrt, exp
from random import uniform

rng = np.random.default_rng()

def X() -> np.float64:
    L1 = rng.uniform(0, 4)
    L2 = rng.uniform(5, 60)
    if rng.uniform(0, 1) < 0.15:
        delta = rng.uniform(0, 3)
        return rng.uniform(40 - delta, 60 + delta)
    return rng.uniform(0, L1 * L1) + rng.uniform(0, L2)

def gen_vals(n : int) -> np.array:
    arr = np.array([]);
    for _ in range(n):
        arr = np.append(arr, X())
    return arr

def Y(n : int) -> np.array:
    return np.mean(gen_vals(n))

def gen_valsY(n : int, bin : int) -> np.array:
    arr = np.array([]);
    for _ in range(n):
        arr = np.append(arr, Y(bin))
    return arr

def gauss(x, mu, sigma):
    return 1 / sqrt(2 * pi * sigma * sigma) * exp(-(x - mu) ** 2 / (2 * sigma * sigma))
vGauss = np.vectorize(gauss)

def gaussData(arr : np.array, size=(0, 100), bin=1):
    return vGauss(np.arange(size[0], size[1]), arr.mean(), arr.std() / sqrt(bin))