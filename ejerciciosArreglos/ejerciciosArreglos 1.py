#1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.

from calendar import c
import random

n=[]
cont=0
c=0
s=0

for i in range(random.randint(10,25)):
    n.insert(i,round(random.random()*100)) 

for i in range(len(n)):
    c+=1
    s+=n[i]
    p = s//c

print (n)

    
    
 
 