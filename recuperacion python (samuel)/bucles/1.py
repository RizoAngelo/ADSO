def funcion(num):
    while num>0:
        if num%a==0:
            print(num,"son multiplo de",a)
        else:
            print(num,"no es multiplo de",a)
        num-=1
a=int(input("introduce un numero: "))
funcion(50)