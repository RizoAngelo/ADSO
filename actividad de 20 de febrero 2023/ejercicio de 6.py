def palabras(pepe):
    if pepe == "ar":
        print("El verbo está conjugado en presente de indicativo.")
    elif pepe == "er":
        print("El verbo está conjugado en pretérito perfecto simple de indicativo.")
    elif  pepe == "ir":
        print("El verbo está conjugado en futuro simple de indicativo.")
    else:
        print("El verbo no está conjugado")

verbo = input("Ingrese palabras\nR:")
pepe = verbo[-2:].lower()
print(palabras(pepe))
