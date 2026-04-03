n = 5
mask = 0
mask = mask >> n - 1
mask = mask | 1 << 3

print(2**n-1)

print(mask)

# if mask == mask1:
#     print("Iguais")