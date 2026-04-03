def validate():
    global compared
    if not(compared.isalpha()):
        raise ValueError

print(f"{'-' * 10} Verificação de Palíndromos {'-' * 10}")

while True:
    while True:
        compared = input("Digite a palavra a ser verificada: ").lower().strip()
        lista = compared.split()
        compared = ''.join(lista)
        
        try:
            validate()
        except ValueError:
            print("O texto não deve possuir números.")
        else:
            break
    
    if compared == compared[::-1]:
        print(f"{compared} é palíndromo")
    else:
        print(f"{compared} não é palíndromo")
    
    answer = input("Deseja tentar uma nova palavra? (S = sim / N = não)").upper().strip()
    answer = answer[0]
    
    if answer == "N":
        print("Obrigado por utilizar o programa :)")
    