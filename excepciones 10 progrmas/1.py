def sumadenumeros(a,b):
    try:
        restados_de_suma = int(a) + int(b)
        return restados_de_suma
        
    except ValueError:
        print("Tiene que ser numeros enteros ")
        exit()
numero=input("introduce un numero")
numero1=input("introduce el sengundo numumero")
print(sumadenumeros(numero,numero1))
