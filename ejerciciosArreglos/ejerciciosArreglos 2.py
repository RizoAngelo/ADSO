#2. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números 
#aleatorios. Muestre cuales y cuantos son primos

import random
n=0
cont=0
cont = 0
for i in range(random.randint(10,25)):
    if n%i==0:
        cont +=1
if cont>0:
    print ("el número es primo",n)
else:
    print ("el número no es primo",n)