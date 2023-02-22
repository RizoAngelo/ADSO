try:
    with open("archivo.txt") as a:
        contenido = a.read()
except FileNotFoundError:
    print("no se encontro ningun archivo")