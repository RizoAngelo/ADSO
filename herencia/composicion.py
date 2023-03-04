class Aprendiz:                                 #esta es una clase llamada aprendiz
    def __init__(self,nombre):                  #aqui inicial contrutor y tiene como parametros nombre        
        self.__nombre=nombre                    #esta linea de codigo sirve para que nombre lo ponga en privado 
        self.__cursos=[]                        #esta es una linea de codigo donde curso lo ponen en privado y que sea igual a una lista

    def agregarCurso(self,titulo):              #esta linea de codigo es una funcion que se llamada agregarCurso y tiene como parametro titulo
        self.__cursos.append(titulo)            #esta liena de codigo sirve para agregar lo que hay en titulo a la lista de __curso

    def getCursos(self):                        #esta funcion que tiene como nombre get Cursos
        return self.__cursos                    #esto retorna lo que hay en __curso

class Curso:                                    #es una clase llamada curso
    def __init__(self,titulo):                  #aqui inicia el construtor  que tiene como parametro titulo
        self.__titulo=titulo                    #aqui ponemos en privado titulo

    def getTitulo(self):                        #es una funcion llamada getTitulo
        return self.__titulo                    #esto retorna lo que esta en __titulo  
    
a=Aprendiz('Martha')                            #aqui a es aprendiz y le agregar martha
c1=Curso('Python Intermedio')                   #aqui c1 es curso y le agregar martha
c2=Curso('Python Basico')                       #aqui c2 es curso y le agregar martha
c3=Curso('Introduccion a Java')                 #aqui c3 es curso y le agregar martha

a.agregarCurso(c1)                              #esto agrega lo que hay en c1 lo agrega a (a)
a.agregarCurso(c2)                              #esto agrega lo que hay en c2 lo agraga a (b)
a.agregarCurso(c3)                              #esto agrega lo que hay en c3 lo agraga a (c)

print(a.getCursos())                            #aqui imprime donde esta localido todas la clase


for curso in a.getCursos():                     #esto es un bucle donde curso = a.getCursos()
    print(curso.getTitulo())                    #aqui imprime en en modo horizontal todo lo que esta en lista de curso