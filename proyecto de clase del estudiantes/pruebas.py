class matriculas:
    def __init__(self,id,detalle):
        self.__id=id
        self.detalle=detalle
    def getMatricula(self):
        return self.detalle
    
    

class registro:
    def __init__(self,id,usuario,contraseña):
        self.__id=id
        self.nombre=[]
        self.__usuario=usuario
        self.__contraseña=contraseña

class instrutor:
    def __init__(self,id,instrutor,):
        self.__id=id
        self.__instructor:instrutor
        

    def getAsignacion(self):
        return self.__instructor


class estudiante:
    def __init__(self,id):
        self.__id:id

class curso():
    def __init__(self,curso,fecha):
        self.curso=curso
        self.fecha=fecha
Ma=matriculas(1,"descricion:vacio")
Cu=curso("a","24")
