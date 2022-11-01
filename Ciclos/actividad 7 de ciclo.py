num = int(input("Ingrese el número máximo   "))
cont=0
while cont*(cont+1)<=2*num:
    cont+=1
print("El número natural mas pequeño que excede al dato es:",cont)