from math import trunc
def numero(num):
    suma= 1
    if num>1:
        for i in range (2,num,1):
            if num%i==0:
                suma=suma+(trunc(num/i))
    if suma>1:
        return ("El número ",num," es perfecto")
    else:
        return ("El número ",num," no es perfecto")
num = int(input("Ingrese un número= "))
print(numero(num))