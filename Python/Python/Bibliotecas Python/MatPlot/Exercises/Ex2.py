import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-20, 21, 1)
y1 = x ** 2
y2 = x ** 3

print(x)
print(y1)
print(y2)


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,20))

ax[0].plot(x, y1)
ax[1].plot(x, y2)

plt.show()