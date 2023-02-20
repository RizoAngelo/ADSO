def palabras(ejercicio,ultima_silaba,penultima_silaba,antepenultima_silaba):
    ultima_silaba = ejercicio[-3:].lower()
    penultima_silaba = ejercicio[-4:-2].lower()
    antepenultima_silaba = ejercicio[-5:-3].lower()
    if ultima_silaba[-1] in "aeiouáéíóú":
        if len(palabra) <= 3 or (ultima_silaba[-2] not in "aeiouáéíóú" and ultima_silaba[-1] == "n"):
            print("La palabra es aguda.")
        else:
            print("La palabra no es aguda.")
    elif penultima_silaba[-1] in "aeiouáéíóú":
    
        if len(palabra) <= 3 or (ultima_silaba[-2] not in "aeiouáéíóú" and ultima_silaba[-1] == "n"):
            print("La palabra es grave.")
        else:
            print("La palabra no es grave.")
    elif antepenultima_silaba[-1] in "aeiouáéíóú":
    
        print("La palabra es esdrújula.")
    else:
        print("La palabra es sobresdrújula.")
palabra = input("Ingrese una palabra: ")
ultima_silaba = palabra[-3:].lower()
penultima_silaba = palabra[-4:-2].lower()
antepenultima_silaba = palabra[-5:-3].lower()
print(palabras(palabra,ultima_silaba,penultima_silaba,antepenultima_silaba))