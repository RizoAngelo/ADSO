#1. pedir numeros, imprimirlo con el opuesto (ejemplo 5 opuesto -5, -10 opuesto 10),
n=1
cont=0

while n !=0:
    n=int(input("digite un numero "))
    if n !=0:
        print('el opuesto de ',n,"es",-(n))
        cont+=1
    if n==0:
        print("el programa finalizo con exito")
print("numeros de intento",(cont))

