"""Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto"""
def valor(letra):
    suma=0
    for i in letra:
        suma+=ord(i)
    return(suma)
        
letra=input("ingrese letras\nR:")
print(list(letra))
print(valor(letra))