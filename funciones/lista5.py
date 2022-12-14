def finabonacci(num):
    lista=[0,1]
    if num>5 and num<20:
        for i in range(num):
            lista.append(lista[-1]+lista[-2])
    return lista
"""NO LA HICE YO LA HIZO Yian"""""