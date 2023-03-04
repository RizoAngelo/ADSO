class A1:                                               #es una clase llamada A1
    def __init__(self):                                 #es una funcion donde inicia el inicia contrutor
        pass                                            #nada(vacio)
    def saludo(self):                                   #es una funcion llamada saludo
        print('Hola desde A1')                          #aqui imprime (hola desde a1) si entra a la clase A1 sin error

class A2:                                               #es una clase llamada esta A2
    def __init__(self):                                 #es una funcion donde inicia el inicia contrutor
        pass                                            #nada(vacio)
    def saludo(self):                                   #es uan funcion llamada saludo
        print('Hola desde A2')                          #aqui imprime (hola desde a2) si entra a la clase A2 sin error


class B(A2,A1):                                         #es una clase llamada B que tiene como parametros(A2,A1)
    def __init__(self):                                 #es una funcion donde inicia el inicia contrutor
        pass                                            #nada(vacio)
    def saludo(self):                                   #es una funcion llamada saludo
        print('Hola desde B')                           #imprime lo ('Hola desde B')  
    def __str__(self):                                  #esto es una funcion donde __str__ es una cadena texto o numeros
        return 'Soy un objeto de la clase B'            # aqui retorna 'Soy un objeto de la clase B'   
obj=B()                                                 #obj es B y no hay nada de parametros
print(obj.__str__())                                    #aqui imprime la cadena de texto que hay en __str__
#obj.saludo()                                           #aqui llama obj.saludo
#obj.saludo()                                           #aqui llama obj.saludo
    

# cad="sena"                                            #cad=sena
# lista=[1,2,3]                                         #es una lista que tiene vario nuemeros
# print(cad.__str__())                                  #aqui imprime la cadena de texto que hay en __str__
# print(lista.__str__())                                #imprime lista.__str__()