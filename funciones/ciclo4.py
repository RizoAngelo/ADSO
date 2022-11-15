def numero(num):
    cont=0
    while cont*(cont+1)<=2*num:
        cont+=1
    return("El número natural mas pequeño que excede al dato es:",cont)
num = int(input("Ingrese el número máximo= "))
print(numero(num))