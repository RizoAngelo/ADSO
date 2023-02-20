def palabras(cadena):
    vocales = 0
    consonantes = 0
    vocales_tilde = 0
    especiales = 0
    for caracter in cadena:
        if caracter.isalpha():
            if caracter in "aeiouAEIOU":
                vocales += 1
                if caracter in "áéíóúÁÉÍÓÚ":
                    vocales_tilde += 1
            else:
                consonantes += 1
        else:
            especiales += 1
    print("La cadena ingresada tiene:\n",vocales, "vocales,\n",consonantes, "consonantes,\n",vocales_tilde,"vocales con tilde y\n",especiales,"caracteres especiales.")
    exit()
cadena = input("Ingrese una cadena: ")
print(palabras(cadena))