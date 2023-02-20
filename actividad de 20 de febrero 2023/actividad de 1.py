"""Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez"""
def pepe(cadena):
    abecedario="bueno dia mi nombre es angelo"
    print("longitud",len(abecedario),"lo que hay:",abecedario)
    cont=0
    for abecedario in abecedario:
        if cadena==abecedario:
            cont+=1
    print (cont)



cadena="a"
print(list(cadena))
print(len(cadena))
print(pepe(cadena))

        


    
