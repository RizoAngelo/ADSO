class Curso:                            #esta linea de codigo es una clase
    def __init__(self,titulo):          #esta linea de codigo es una funcion donde  inicia el codigo que tiene como parametro titulo
        self.__titulo=titulo            #esta linea de codigo es donde ponemos titulo en privado y que sea igual a titulo

    def getTitulo(self):                #esta linea de codigo es una funcion  llamada getTitulo(para acceder)
        return self.__titulo            #esto return lo que hay en __titulo(privado)

class Aprendiz:                         #esta linea de codigo  es una clase llamada aprendiz
    def __init__(self,nombre):          #esta linea de codigo es una funcion donde inicia el contrutor y tiene como parametros nombre
        self.__nombre=nombre            #esta linea de codigo  sirve para que __nombre se ponga en privado y que sea igual a nombre
        self.__cursos=[]                #esta linea de codigo sirve para crear una lista en privado

    def agregarCurso(self,nombreCursito): #esta linea de codigo es una funcion llamada agragarcurso que tiene como parametros nombreCursito 
        cursito=Curso(nombreCursito)      #esta linea de codigo es una variables que tiene 
        self.__cursos.append(cursito)      #esta linea de codigo sirve para que _lo que este en cursito se agradado a la lista

    def getCursos(self):                   #esta linea de codigo es una funcion que tiene como nombre getCursos
        return self.__cursos               #aquie retorna los que hay en __cursos

ap=Aprendiz('Sofia')                    #esta liena de codigo es para colocarle a la clase aprendiz el parametro de Sofia
ap.agregarCurso('Python Basico')        #esta linea de codigo es para agregarle los curso al aprendiz
ap.agregarCurso('Python Intermedio')    #esta linea de codigo es para agregarle los curso al aprendiz

for c in ap.getCursos():                #esta linea de codigo es para repetir varias veces ap.getCursos() pero colocandole como variable c para ser mas sencillo
    print(c.getTitulo())                #aqui imprime el c.getTitulo de lo que return en la linea 6 

