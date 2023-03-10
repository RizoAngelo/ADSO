class Materia:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.__id_estudiante = id_estudiante
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)
    
    def mostrarmaterias(self):
        return self.materias

materias = []


while True:
    print("1. Agregar materia")
    print("2. Registrar estudiante")
    print("3. Buscador de materia")
    print("4. Cancelacion de materia")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        codigo = input("Ingrese el codigo de la materia: ")
        nombre = input("Ingrese el nombre de la materia: ")
        materia = Materia(codigo, nombre)
        materias.append(materia)

    elif opcion == 2:
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        id_estudiante = input("Ingrese su numero de identificación: ")

        print("Seleccione una materia para inscribirse:")

        for i, materia in enumerate(materias):
            print(f"{i+1}. {materia.nombre} ({materia.codigo})")

        opcion_materia = int(input("Escribe el codigo que desea estudiar: "))

        estudiante = Estudiante(nombre, apellido, id_estudiante)
        materia_seleccionada = materias[opcion_materia - 1]
        materia_seleccionada.agregar_estudiante(estudiante)
        estudiante.agregar_materia(materia_seleccionada)

        print("Estudiante registrado con exito")
    elif opcion ==3:
        materia.mostrarmaterias()
        
             
    
    elif opcion == 4:
        None




    elif opcion == 5:
        print("Espero que regrese")
        exit()