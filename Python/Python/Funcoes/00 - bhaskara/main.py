# Crie uma função "bhaskara()", que recebe a,b,c, e 
# retorna os dois resultados possíveis da equação de 
# bhasakara (retorna "i", caso dê um número imaginário)

def b(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 'i'
    
    
    delta = delta ** 0.5
    res1 = (-b + (delta))/(2*a)
    res2 = (-b - (delta))/(2*a)
    
    return (res1,res2)

# --------EXEMPLO--------
def f(x):
    return 2 * x + 7

r = b(2,4,-6)

print(r) # esperado -> (1.0, -3.0)
