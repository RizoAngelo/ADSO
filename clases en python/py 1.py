class Empleados:
    def __init__(self,nombre,cargo,salario,extrasalario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        self.__extrasalario=extrasalario
        
    def getNombre(self):
        return self.__Nombre
    
    def getCargo(self):
        return self.__Cargo
    
    def getSalario(self):
        return self.__Salario
    
    def getExtrasalario(self):
        return self.__Extrasalario
    
    def setNombre(self,nombre):
        self.__Nombre=nombre
        
    def setCargo(self,cargo):
        self.__Cargo=cargo
        
    def setSalario(self,salario):
        self.__Salario=salario
    
    def setExtrasalario(self,extrasalario):
        self.__Extrasalario=extrasalario
        
    def Calculo(self):
        self.Calculo = (self.__salario/20)/8
    
    def ipc(self,salario):
        if salario==1300000:
            a=(salario*0.16)
            print("se le sube el 0.16%",a)
        elif salario>1300000:
            i=(salario*0.13)
            print("se le sube el 0.13%",i)
        else:
            ("no se le puede incremeta")        
    
    
        
    
ob=Empleados("Angelo","Desarrollador",1300000,4800)
ob.Calculo()
ob.ipc()