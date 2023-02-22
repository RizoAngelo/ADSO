def dic():
    try:
        diccionario = {"a": 1, "b": 2}
        valor = diccionario["c"]
    except KeyError:
        print("la clave que esta buscando no se encuentra")
print(dic())