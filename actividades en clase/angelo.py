import random
from statistics import multimode
tam=random.randint(10,25)
lis = []
suma = 0
media = 0 
variable = 0
n = 0
for i in range (tam):
    lis.insert(0,random.randint(10,25))
for i in range (len(lis)):
    if lis != 0:
         suma += lis[i]
         media = suma // tam
         vm = min(lis)
         n = max(lis)
print(lis)
print("la suma de sus digitos es ", suma)
print("la media de sus digitos es ", media)
print("la moda de sus digito es",multimode(lis))