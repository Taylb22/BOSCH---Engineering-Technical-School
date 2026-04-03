import math 
# Crie uma função "bhaskara()", que recebe a,b,c, e 
# retorna os dois resultados possíveis da equação de 
# bhasakara (retorna "i", caso dê um número imaginário)

calculate_delta = lambda a, b, c: (b * b) - (4 * a * c)

def bhaskara(a: float, b: float, c: float) -> float:
    delta = calculate_delta(a, b, c)
    
    if delta < 0:
        raise ValueError ("Valor de Delta menor que 0")
    
    delta = delta ** 0.5
    
    result1 = ((-b) + delta) / (2 * a)
    result2 = ((-b) - delta) / (2 * a)
    
    return (result1, result2)

try:
    r = bhaskara(2,4,-6)
except ValueError as erro:
    print("O resultado de Delta não pode ser menor do que 0")
print(r) # esperado -> (1.0, -3.0)