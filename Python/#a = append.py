#a = append
#w = write
#r = read

with open('./ola.txt', 'r') as anotacoes:
    for line in anotacoes.readlines(): #.readlines()
        print(line)