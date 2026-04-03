import random
import unicodedata

def strip_accent(word:str) -> str:
    normalized = unicodedata.normalize('NFD', word)
    text = "".join([c for c in normalized if not unicodedata.combining(c)])
    
    return text

def read_txt(dif: int) -> list:
    words = []
    with open("Words_Anagram.txt", 'r', encoding='utf-8') as archive:
        for line in archive.readlines():
            split_line = line.strip().split(';')
            
            if not(int(split_line[0]) == dif):
                continue
            
            split_line.pop(0)
            
            for word in split_line:
                word = word.encode('utf8', "strict").decode('utf8')
                words.append(word)
        archive.close()
        
    while '' in words:
        words.remove('')
    return words

def validate_int_input(input_value: int, inferior_limit: int, superior_limit: int) -> bool:
    if not(inferior_limit <= input_value <= superior_limit):
        return False
    return True

def shuffle_choice(word: list) -> str:
    
    amount = 0
    for char in word:
        if char in vogals:
            amount += 1
    
    vogals_index = [[0, 0]] * amount
    consonants_index = [[0, 0]] * (len(word) - amount)
    
    i = 0
    j = 0
    z = 0
    for char in word:
        if char in vogals:
            vogals_index[j - 1][1] = i
            vogals_index[j - 1][0] = char
            j += 1
        else:
            consonants_index[z - 1][1] = i
            consonants_index[z - 1][0] = char
            z += 1
        word.remove(char)
        i += 1
    
    print(vogals_index)

    return word
            

vogals = ['a', 'e', 'i', 'o', 'u']

while True:
    while True:
        try:
            score_minus = int(input("Quantos pontos deseja perder se você errar(20 a 100)? "))
            score_validation = validate_int_input(score_minus, 20, 100)
            
            if not(score_validation):
                print("\nA pontuação a perder está fora dos limites (20 até 100), por favor, digite um valor válido.\n")
                continue
            
            dif = int(input("Qual a dificuldade de palavra que você deseja(1, 2 ou 3)? "))
            dif_validation = validate_int_input(dif, 1, 3)
            
            if not(dif_validation):
                print("\nA dificuldade escolhida não é válida, por favor, tente novamente com um valor válido.\n")
                continue
            break
        except ValueError:
            print(f"Um dos valores digitados não é valido, tente novamente.\n")
    
    total_score = 100
    
    words = read_txt(dif)
    
    anagram = random.choice(words)
    answer = anagram
    anagram = strip_accent(anagram).lower()
    anagram = list(anagram)
    anagram = shuffle_choice(anagram)
    anagram = "".join(anagram)
    
    while True:
        print(f"\nPalavra sorteada:\n{anagram}\n")
        print(anagram)
        
        guess = input("R: ").lower().strip()
        
        if strip_accent(guess).lower() == strip_accent(answer).lower():
            print(f"\nParabéns!! Você acertou a palavra {answer}\n")
            break
        else:
            total_score = total_score - score_minus
            if total_score <= 0:
                print("\nVocê Perdeu :(\n")
                break
            else:
                print(f"\nVocê errou... Tente novamente.\nPontuação Restante: {total_score}\n")
    
    again = input("Você deseja jogar novamente? (S = sim/ N = não): ").upper().strip()
    again = again[0]
    
    if again == 'N':
        print("Obrigado por Jogar :)")
        break