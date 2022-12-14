def moda(lista):
    lista2=[]
    cont=0
    mayor=0
    pos=0
    moda=0
    for i in range(len(lista)): 
        cont=0
        for j in lista:    
            if lista[i] == j:
                cont+=1 
        if cont!=0:
            lista2.append(cont)
        else:
            lista2.append(0)
    for i in range(len(a)):
        if mayor<lista2[i]:
            mayor=lista2[i]
        for j in range(len(lista2)):
            if mayor==lista2[j]:
                moda=lista[j]
    return moda
"""NO LA HICE YO LA HIZO Yian"""""