import numpy as np
import matplotlib.pyplot as plt
import typing

def factorial(n : int):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

def dist_binomial(n : int, k : int, p : float):
    return (factorial(n) / (factorial(k) * factorial(n - k))) * p**k * (1-p)**(n-k)

x = np.arange(0, 21, 1)
vfunc = np.vectorize(dist_binomial)
y = np.round(vfunc(20, x, 0.2), 4)

print(f"Probabilidade de acertar todas -> {round(dist_binomial(20, 20, 0.2) * 100, 2)} %")
print(f"Probabilidade de passar -> {np.sum(y[9::]) * 100} %")
print(f"A quantidade de acertos mais provável é {np.argmax(y)} com uma probabilidade de {round(np.max(y) * 100, 2)} %")
print(f"A nova probabilidade dele ser aprovado é de -> {np.round(np.sum(vfunc(17, x[6:18], 0.2)) * 100, 2)} %")

plt.plot(x, y, marker="o")
plt.title("Distribuição Binomial (n = 20, p = 0.2)")
plt.xlabel("Número de Acertos")
plt.ylabel("Probabilidade")
plt.grid()
plt.xticks(x)

for i in range(len(x)):
    plt.text(x[i], y[i], str(y[i]))

plt.show()