import sqlite3                                          #importa el modulo sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')   #aqui conecta con una ruta (asoluta)  
con=sqlite3.connect('conpython.db')              #esto es para conectar la ruta (relativa)
print(type(con))                                        #impreme el tipo de dato (sqlite3.connect)
micursor=con.cursor()                                   #aqui hace que podamos manejar los datos con el curso
print(type(micursor))                                   #imprime el tipo de dato (con.cursor)
sentencia="SELECT * FROM alumno;"                       #aqui hace una sentecia de sql
micursor.execute(sentencia)                             #aqui es para ejecutar la sentencia con el micursor.execute 
for fila in micursor.fetchall():                        #aqui es para repertir varia veces micurso.fechall con el nombre de file
    print(fila[0])                                      #aqui imprime la posicion de la fila 0
    print(fila[1])                                      #aqui imprime la posicion de la  fila 1
    print(fila[2])                                      #aqui imprime la posicion de la  fila 2
    print(fila[3])                                      #aqui imprime la posicion de la  fila 3
    print('-'*50)                                       #aqui imprime 50 veces (-)