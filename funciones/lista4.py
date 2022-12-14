def desviacion(lista):
    lista2=[]
    prom=prom_listas(lista)
    suma=0
    for i in range(len(lista)):
        lista2.append(lista[i]-prom)
        lista2[i]=lista2[i]**2
        suma+=lista2[i]
    desviacion=((suma**0.5)/len(lista)-1)**0.5
    return desviacion

"""NO LA HICE YO LA HIZO Yian"""""