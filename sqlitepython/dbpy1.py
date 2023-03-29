import sqlite3                                              #importa del modulo sqlite3
with sqlite3.connect('sqlitepython/conpython.db')as con:    #aqui busca la busca la ubicacion del archivo
    micursor=con.cursor()                                   #aqui hagara le pone un cursor para ejecutar mas adelante los datos de con
    sentencia="SELECT nombre,apellido FROM alumno;"         #una sentecia de sql para selecionar nombre y apeelido de la tabla alumno
    print(micursor.execute(sentencia).fetchmany(10))        #imprime la ejecucion de la sentcia perro implime 10 registro

#print()

