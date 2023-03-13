import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:#El archivo o directorio no existe. Este error se asigna a la excepción FileNotFoundError.
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:#Desbordamiento de la tabla de archivos
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
#rt	rb	lectura
#wt	wb	escritura
#at	ab	adjuntar
#r+t	r+b	lectura y actualización
#w+t	w+b	escritura y actualización
#si quiere saber mas sobre como se utiliza el errno https://docs.python.org/es/3/library/errno.html
