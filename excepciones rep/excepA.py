try: # Sirve para comenzar una prueba de errores
    #print(1/1)) codigo esta mal porque tiene un parentecis de mas y se reconoce como un error de SyntaxError 
    raise SyntaxError# este codigo simula un error de  SyntaxError y lo arroja con un raise
except SyntaxError:#Luego la except SyntaxError Hagara el raise que esta simulando el error que arrojo el la linea 3 y luego saca un print con un mentario
    print('Cierra el parentesis')#este print es el comentario para el error de except SyntaxError