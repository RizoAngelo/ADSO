numeros = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("original",numeros)
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.

numeros[2] = int (input("ingrese un numero "))
print("modificacio de la lista",numeros)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del numeros[4]
print("lista nueva",numeros)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("longitud de la lista",len (numeros))
