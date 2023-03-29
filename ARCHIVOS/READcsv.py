from Humanos import *
import csv
lista=[]
with open('D:\ADSO\ARCHIVOS\enterprises.csv') as empresa:
    prueba=csv.reader(empresa)
    for a in prueba:
        #print(a[1])
        #print(a[2])
        EMPRESA=humano(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])   
        lista.append(EMPRESA)
print(lista)
for s in lista:
    print(s.informaciondecompañia())