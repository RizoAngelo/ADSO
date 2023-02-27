values = (1, 0)#esta es un atupla que tiene dos variables
#x,y=19,30
#print(divmod(10,3))
try:#aqui inicia una prueba de excepciones
    q, r = divmod(*values)#Aqui se le hacina a la ()y ()
    #print('q=',q)
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)