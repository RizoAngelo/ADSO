values = [1, 4]#esto es una lista con numeros adentro de la lista
#x,y=19,30
#print(divmod(10,3))
try:#comienza la prueba de excepciones
    q, r = divmod(values)#aqui q=1 r=4 aqui divide los numero por su mismo numero que es 4/4=1 1/1=
    #print('q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)