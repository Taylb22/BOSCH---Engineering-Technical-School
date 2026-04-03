from time import time
from random import choice

def read_txt():
    phrases = []
    with open("frases.txt", "r") as arq:
        for line in arq.readlines():
            phrases.append(line.replace('\n', ''))
    
    return phrases

phrases = read_txt()

print("Digite a frase abaixo o mais rápido possível: ")
print()
P = choice(phrases).strip()
print(P)
print()
print("Pressione ENTER para começar...")
input()
sec = time()

while True:
    print("Digite aqui\n>> ", end='')
    answer = input().strip()
    
    if answer == P:
        sec = time() - sec
        break
    else:
        print("As frases não coincidem, tente novamente.\n")

print("\nRESULTADO")
print(f"Tempo Total: {sec:.2f}")
print(f"Velodidade: {(len(P) / sec):.2f} caracteres por segundo")
        
