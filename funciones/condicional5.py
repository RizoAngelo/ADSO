def numeros(minutos):
    if minutos <= 3:
        return (" en total son ",minutos_1)
    else:
        return ("en total son ", minutos_3 * 50 + 200)
minutos = int(input("cuantos minutos?"))
minutos_1 = minutos * 67 - 1
minutos_3 = (minutos - 3)
print(numeros(minutos))