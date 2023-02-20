def plabra(cadena):
    for i in range(2, len(cadena)+1):
        for j in range(len(cadena)-i+1):
            print(cadena[j:j+i])
cadena = input("Introduce la cadena: ")
print(plabra(cadena))