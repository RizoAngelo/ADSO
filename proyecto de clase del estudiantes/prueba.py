import random

class Matricula:
    def __init__(self,estudiante,curso):
        self.estudiante = estudiante
        self.curso = curso

class Maestro:
    def __init__(self,nombre,apellido,id_maestro,usuario,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.__id_maestro = id_maestro
        self.__usuario=usuario
        self.__contraseña=contraseña
        self.curso_asignado = []
        
    def darclase(self):
        if self.curso_asignado:
            print(f"El instrutor(ar) ({self.nombre}) esta dando la formacion ({self.curso_asignado}) a los estudiante del sena")
        else:
            print(f"El Instructor(ar) {self.nombre} no tiene un curso asignado en el sena.")

class Estudiante:
    def __init__(self,nombre,apellido,id_estudiante,usuario,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.__id_estudiante = id_estudiante
        self.curso_asignado = []
        self.__usuario=usuario
        self.__contraseña=contraseña

    def matricularse(self,curso,maestro):
        matricula = Matricula(self, curso)
        self.curso_asignado = curso
        maestro.curso_asignado = curso
        print(f"El estudiante ({self.nombre}) ya a sido matriculado en el ({curso}), con el instrutor ({maestro.nombre}) que dictará la formacion.")
        return matricula

cursos_disponibles = ["educacion fisica", "Analista desarrollador de sotfware", "Analista en sotfware", "Desarrollador de sotfware"]
maestro1 = Maestro("Jose", "Rizo", 1,"Joserizo93@hotmail.com","1252859854852")
curso_asignado = random.choice(cursos_disponibles)
maestro1.curso_asignado = curso_asignado
maestro1.darclase()


print("________________________________________________________________________________________________________________________________________")
estudiante1 = Estudiante("Angelo", "Gulloso",1,"Angelo@hotmail.com","12528596265841651852")
curso_elegido = random.choice(cursos_disponibles)
matricula1 = estudiante1.matricularse(curso_elegido, maestro1)
print("______________________________________________________________________________________________________________________________________________")
maestro2 = Maestro("Maria", "Rodríguez", 2,"MariaR@gmail.com","15584581572")
curso_asignado = random.choice(cursos_disponibles)
maestro2.curso_asignado = curso_asignado
maestro2.darclase()
print("__________________________________________________________________________________________________________________________________________________________")
estudiante2 = Estudiante("Jian", "López", 2,"JianLP3@hotmail.com","158488584156842")
curso_elegido = random.choice(cursos_disponibles)
matricula2 = estudiante2.matricularse(curso_elegido, maestro2)
print("__________________________________________________________________________________________________________________________________________________________")
maestro3 = Maestro("Pepe", "Rodríguez", 55,"PEPER@gmail.com","1558458155126158156972")
curso_asignado = random.choice(cursos_disponibles)
maestro3.curso_asignado = curso_asignado
maestro3.darclase()
a= estudiante1
print("____________________________________________________________________________________________________________________________________________________________")
estudiante3 = Estudiante("Jose", "Gulloso",66,"joselo@hotmail.com","841651852")
curso_elegido = random.choice(cursos_disponibles)
matricula1 = estudiante3.matricularse(curso_elegido, maestro3)
print("______________________________________________________________________________________________________________")
try:
    print("aqui se imprime que el instrutor pepe elimino a  estudiante Angelo de base de dato con conclucio va a salir error en python")
    del a
    print(a)
except:
    print("estoy dentro de las prueba de error para confirmacion de elimnicacion de estudiante angelo")




