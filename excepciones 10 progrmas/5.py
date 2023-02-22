def lis(lista):
    try:
        lista[4]
    except IndexError:
        print("no se encutra lo que esta buscando")
lista = [1, 2, 3]
print(lis(lista))