def numero(num):
    cont = 0
    for i in range (2,num,1):
        if num%i==0:
            cont +=1
    if cont>0:
        return ("el número es primo")
    else:
        return ("el número no es primo")
num = int(input("ingrese un número= "))
print(numero(num))