from math import trunc

num = int(input("Ingrese un número   "))
suma= 1
if num>1:
    for i in range (2,num,1):
        if num%i==0:
            suma=suma+(trunc(num/i))
if suma>1:
    print ("El número ",num," es perfecto")
else:
    print ("El número ",num," no es perfecto")