class Persona:#es una clase persona
    def __init__(self,nombre,documento):#esta funcion es para iniciar la clase siempre en los parametros tenemos que llamar siempre self y (nombre) a hora mismo es (Ana)
        self.__nombre=nombre#esta linea de codigo hace que primero tenemos que llamar self luego nombre pero nombre esta en privado y dice que si es igual a su misma variable
        self.__documento=documento
        print('Activando constructor')#si es verda lo que hay en la line 3 entoce imprime esto

    def getNombre(self):#esta es una funcion llamada getNombre que tiene como parametro(self)
        return self.__nombre#aqui hace que retorne lo que hay en en __nombre al (print(ob.getNombre()))
    
    def setNombre(self, nombre):#es una funcion llamada setNombre tiene como parametro(self,nombre="Maria (por la modificacion)")
        self.__nombre=nombre#aqui lo que esta diciendo si lo que esta en nombre en igual a nombre

    def metodo(self):#es una funcion llamada metodo
        print('Soy un método')#imprime
    
    def myself(self):#es una funcion llamada myself
        print("Mi nombre es " + self.__nombre + " y vivo en colombia")#esto imprime el el nombre privado que hay en nombre 
        



ob=Persona('Ana',15153)#esta variable para llamar la clase persona y para que ob sea (Ana)
print(ob.getNombre())#aqui imprime lo retornado en (def getNombre(self):)
ob.setNombre('Maria')#esta linea de codigo es para modifica lo que hay en (ob=Ana)lo modifica a (ob=Maria)
print(ob.getNombre())#luego imprime lo que hay en (ob.getNombre())R:Maria
#ob.metodo()#aqui llamada la funcion metodo
#print(type(ob))#imprime que tipo es ob
print(Persona.__dict__)#esto hace que busca los metodos y atributos de lo que hay en la clase persona
ob.myself()#llama la funcio
