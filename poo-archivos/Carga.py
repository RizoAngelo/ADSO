from Vehiculo import *                                  #Importa todo lo que hay en vehiculos
class Carga(Vehiculo):                                 #la clase se llama carga que tiene como parametro vehiculo
    def __init__(self,placa,conductor,capacidad,ejes):#abre el cotrutor que tiene como para merametro (self,placa,conductor,capacidad,ejes)
        Vehiculo.__init__(self,placa,conductor)#segundo contrutor para vehiculo que tiene como parametro(self,placa,conductor)
        self.__capacidad=capacidad #aqui pone en privado
        self.__ejes=ejes    #aqui es para ponerlo en privado
    def getCapacidad(self): #una funcion llama getcapacidad
        return self.__capacidad     #aqui retorna __capacidad
    def getEjes(self):  #una funcion llamada getejes
        return self.__ejes #aqui retorna lo que hay en __ejes