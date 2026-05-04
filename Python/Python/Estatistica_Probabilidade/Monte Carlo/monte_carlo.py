import matplotlib.pyplot as plt
import lib
import numpy as np
from scipy.stats import norm

n = 10000
x = lib.gen_vals(n)
y = lib.gen_valsY(n, 24)

z = (25 - np.mean(y)) / np.std(y)
prob = 1 - norm.cdf(z)
print(f"{prob:.2%}")

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].hist(x, density=True, bins=100)
ax[0].plot(lib.gaussData(x, size=(0, 70)))
ax[1].hist(y, density=True, bins=100)
ax[1].plot(lib.gaussData(y, size=(0, 40)))
plt.show()