import sqlite3                                          #aqui importa el modulo sqlite3
con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')    #aqui le da la ruta de donde esta el archivo
print(type(con))                                        #imprime que tipo de con
micursor=con.cursor()                                   #aqui le da un cursor
print(type(micursor))                                   #y le muestra el tipo de micursor