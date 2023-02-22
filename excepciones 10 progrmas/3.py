class ValorNegativoError(ValueError):
    pass

def pepe(numero):
    if numero < 0:
        raise ValorNegativoError("El número no puede ser negativo.")
    else:
        raiz = numero ** 0.5
        return raiz

try:
    a=pepe(-1)
except ValorNegativoError as e:
    print(e)
