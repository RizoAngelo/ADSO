from Carga import * #aqui importa todo lo que hay en carga
from Conductor import *#aqui importa todo lo que hay en coductor
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor') #aqui es una variable nomCoductor que tiene un input donde uno puede escribir
docConductor=int(input('Ingrese documento del conductor')) #aqui es una variable docConductor que tiene un input donde uno puede escribir
placa=input('ingrese placa')#aqui es una variable placa que tiene un input donde uno puede escribir
capacidad=input('ingrese capacidad en toneladas')#aqui es una variable capacidad que tiene un input donde uno puede escribir
ejes=input('ingrese numero de ejes')
c1=Conductor(nomConductor,docConductor)
obCarga=Carga(placa,c1,capacidad,ejes)
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())

with open('poo-archivos/listado.txt','a') as flujo:
    flujo.write(cadCarga+'\n')