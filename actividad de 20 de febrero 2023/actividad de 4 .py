def palabras(cadenas):
    for p in range(1*len(cadenas)):
        combinar=""
        for i in range(len(cadenas)):
            if p & (1<<i):
                combinar+=cadenas[i].upper()
            else:
                combinar+=cadenas[i].lower()
        print(combinar)
            
cadenas= input("Ingresa la cadena que quiere convertir\nR:")
print(palabras(cadenas))