# Crie uma função "toLow()" que recebe uma string e retorna uma 
# versão dessa string com todos os caracteres 
# minusculos (caracteres especiais devem ser mantidos)

def toLow(text: str) -> str:
    new_text = []
    for char in text:
        if 65 <= ord(char) <= 90:
            new_char = chr(ord(char) + 32)
        else:
            new_char = char
        new_text.append(new_char)
        
    return "".join(new_text)

a = toLow('HaHA PaPOi? HAHA PAPOI! UaaaaA')
print(a)