def cifra(num):
    if (num<10):
        return ("su numero es de una cifra")
    elif num < 100 :
        return ("el numero es de dos cifras")
    elif num < 1000:
        return ("el numero es de tres cifras")
    elif num < 10000: 
        return ("el numeo es de cuatro cifras")
    elif num > 100000:
        return ('superaste el limite de numeros')
num = int(input("digite su numero de 0 a 9999 "))
print(cifra(num))