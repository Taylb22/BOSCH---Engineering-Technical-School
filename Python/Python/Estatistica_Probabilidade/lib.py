import numpy as np
import math as m

vComb = np.vectorize(m.comb)
conditional_prob = lambda a, b : np.intersect1d(a, b) / np.sum(b)

dist_binomial =  lambda n, k, p : m.comb(n, k) * p**k * ((1-p)**(n-k))
vdist_binomial = np.vectorize(dist_binomial)

# def dist_binomial(n : int, k : int, p : float):
    # return m.comb(n, k) * p**k * ((1-p)**(n-k))

def dist_poisson():
    pass