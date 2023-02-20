def nuemro(n):
    cont=0
    while n !=0:
        n=int(input("digite un numero "))
        if n !=0:
            print('el opuesto de ',n,"es",-(n))
            cont+=1
        if n==0:
            print("el programa finalizo con exito")
    print("numeros de intento",(cont))
n=1
nuemro(n) 