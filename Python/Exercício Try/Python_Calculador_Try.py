print(f"{'=' * 10} Calculadora {'=' * 10}")

while True:
    try:
        resultado = eval(input("Digite a sua equação matemática: "))
        print(f"Resultado = {resultado}")
        
        continuar = input("Deseja continuar? (S = sim / N = não)").upper().strip()
        continuar = continuar[0]
        
        if continuar == "N":
            print("Obrigado por utilizar o programa :)")
            break
        
    except ValueError:
        print("O valores digitados não são aceitos, por favor, tente novamente.")
    except ZeroDivisionError:
        print("Impossível dividir por zero, por favor, tente novamente.")
    except NameError:
        print("Por favor, digite um valor válido.")
    except Exception as erro:
        print(f"ERRO: {erro}")