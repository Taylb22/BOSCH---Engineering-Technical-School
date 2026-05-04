b=[]
jog = True
lista = [7,5,10,1,9]
lista1 = lista[:]
while jog:
    for i in lista:
        for e in lista1: 
            if i > e:
                i = e
                next        
        b.append(i)
        lista.remove(i)
        lista1.remove(i)
        if not lista:
            print(b)
            jog = False