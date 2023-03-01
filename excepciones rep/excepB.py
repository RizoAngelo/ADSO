values = (1, 0)#esta es una tupla que tiene dos variables
#x,y=19,30
#print(divmod(10,3))
try:#aqui inicia una prueba de excepciones
    q, r = divmod(*values)#Aqui se le hacina a la q(10) r(3)
    #print('q=',q)#haci es como utlizamos diariamente para llamar una variable 
    print(f'q={q}')#no poduede imprimir porque es un cero en una tupla
    print(f'r={r}')#no lo imprime porque hay un error en la linea 7
except (ZeroDivisionError, TypeError) as e:#esta except sirve para que si hay un except de (ZeroDivisionError, TypeError) pero e es todo los errores de esta linea
    print(type(e), e)#esto imprime que tipo de error trago (e) y imprime el error que trago e