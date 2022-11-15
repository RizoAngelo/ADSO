#4.Generar numero (generarlo random) y adivinarlo diciendo si cada intento es mayor o menor que el numero. Decir cuantos numeros ingreso antes de adivinarlo


import random


x=random.randint(1,20)
n=0
cont=0
while n != x:
    n=int(input("digite numero "))
    cont+=1
    if n>x:
        print(n,"es muy grande")
    else:
        print(n,"es muy pequeño")
    print("numero de intentos=", cont)
