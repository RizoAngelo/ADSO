import sqlite3                                                                  #importa del modulo sqlite3
with sqlite3.connect('conpython.db')as con:                        #aqui le muestra la ubicacion de donde esta los datos y se llama con
    micursor=con.cursor()                                                       #aqui hagara le pone un cursor para ejecutar mas adelante los datos de con
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"            #aqui le da una sencia de sql que seleciona la (id,nombre,apellido) de la tabla alumno que tenga como una codicion que la id>=400
    #print(micursor.execute(sentencia).fetchall())
def miselect(conexion,tabla,campo,operador,dato):                               #una funcion llama miselct que tiene comop parametros (conexion,tabla,campo,operador,dato)
    micursor=conexion.cursor()                                                  #aqui le pone un cursor para ejecutar mas adelante los datos de conexion
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"          #aqui le da una sencia de sql que seleciona toda la tabla de alumno de que el capo se email y que sea igual a dato que le proporcione el usuario 
    print(sentencia)                                                            #imprime la sentencia
    print(micursor.execute(sentencia).fetchall())                               #imprime la ejecucion de la sentecia para y que sea un solo dato
miselect(con,'alumno','email','=','dbrabon2@irs.gov')                           #aqui le da parametro a miselct que son (con,'alumno','email','=','dbrabon2@irs.gov')
