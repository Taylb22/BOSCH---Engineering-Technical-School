import random

def validate_bet(balance: float, bet: float) -> bool:
    if bet > balance:
        raise ValueError("Aposta maior que o saldo")
    elif bet < 0:
        raise ValueError("Aposta negativa")
    return True

def get_card():
    global pack
    while True:
        name = random.choice(list(pack.keys()))
        
        if not(pack[name][1] == 0):
            break
    
    value = pack[name][0]
    pack[name][1] = pack[name][1] - 1
    
    return name, value

def hit() -> None:
    global player_score
    global computer_score
    
    card, player_score_temp = get_card()
    player_score += player_score_temp

    card_comp, computer_score_temp = get_card()
    computer_score += computer_score_temp
    
    print(f"\nVocê pegou {card}. {player_score_temp} adicionado à sua pontuação.\nSua pontuação = {player_score}")
    print(f"A banca pegou {card_comp}. {computer_score_temp} adicionado à pontuação da banca.\nPontuação da Banca = {computer_score}") 

def validate_victory(player_score: int, computer_score: int) -> bool:
    if (player_score > computer_score and not(player_score > 21))\
        or (computer_score > 21 and player_score <= 21):
        return True
    
    return False

balance = 500

print(f"{'-' * 10} Bem vindo ao jogo de BlackJack {'-' * 10}")

pack = {
    'Às': [1, 4],
    '2': [2, 4],
    '3': [3, 4],
    '4': [4, 4],
    '5': [5, 4],
    '6': [6, 4],
    '7': [7, 4],
    '8': [8, 4],
    '9': [9, 4],
    '10': [10, 4],
    'Valete': [10, 4],
    'Dama': [10, 4],
    'Rei': [10, 4]
}

while True:
    for key in pack.keys():
        pack[key][1] = 4
    
    player_score = 0
    computer_score = 0
    
    print(f"Seu saldo atual: {balance:.2f}")
    
    while True:
        try: 
            bet = float(input("Quanto deseja apostar? "))
            validation = validate_bet(balance, bet)
        except ValueError:
            print("Aposta inválida, por favor, digite um novo valor.")
        else:
            break

    
    for i in range(2):
        hit()
    
    print()
    while True:
        answer = input("Deseja pegar uma nova carta? (HIT / STOP)").upper().strip()
        answer = answer[0]
        
        if not(answer == "H"):
            break
        
        hit()
    
    victory = validate_victory(player_score, computer_score)   

    if victory:
        print("Você venceu!!!")
        balance += bet
    else:
        print("Você perdeu")
        balance -= bet
    
    if balance == 0:
        print("Seu saldo acabou...")
        break
    
    answer_continue = input("Deseja continuar? (S = sim / N = não) ").upper().strip()
    answer_continue = answer_continue[0]
    
    if answer == "N":
        print("Obrigado por jogar :)")
        break