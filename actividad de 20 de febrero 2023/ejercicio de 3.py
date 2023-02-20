""" cuantas veces se repite un caracter dado"""
def pepe(cadena,palabras):
    cont=0
    for palabras in palabras:
        if cadena==palabras:
            cont+=1
    print("se repite la letra",cadena,"=",cont)
    
cadena="a"
palabras="bueno dia mi nombre es angelo"
print("longitud",len(palabras),"lo que hay:",palabras)
print(list(cadena))
print(len(cadena))
print(pepe(cadena,palabras))


