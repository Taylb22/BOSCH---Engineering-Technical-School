import numpy as np

a = np.random.randint(0,10,5)
b = np.random.randint(0,10,5)
print(f"\nOriginal a -> {a}\nOriginal b -> {b}\n")
print(f"União: {np.union1d(a, b)}\n") # Une os dois vetores desconsiderando repetições
print(f"Intersecção: {np.intersect1d(a, b)}\n") # Apenas os elementos em comum sem repetições
print(f"Únicos de \"A\": {np.unique(a)}") # Valores Únicos de "A"
print(f"Únicos de \"B\": {np.unique(b)}\n") # Valores Únicos de "B"
print(f"Diferença de \"A\" com \"B\": {np.setdiff1d(a, b)}") # Remove de "A" todos os itens coincidentes em "B" eliminando repetições
print(f"Diferença de \"B\" com \"A\": {np.setdiff1d(b, a)}\n") # Remove de "B" todos os itens coincidentes em "A" eliminando repetições