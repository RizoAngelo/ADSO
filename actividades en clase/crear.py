
import random
vec=[round(random.random()*100) for i in range(10)]
print(vec)
#10 ejercio compresion
pares=[x for x in vec if x%2==0]
impares=[x for x in vec if x%2!=0]
print(pares)
print(impares)

pares2=[x if x%2==0 else 0 for x in vec]
print(pares2)
# lo que tenga un solo digitos colocarte 0
# lista de edad colocarle si es mayor o menor

unnumero=[x if x<10 else 0 for x in vec]
print=(unnumero)

edad=["mayor" if x>=18 else "menor" for x in vec]
print=(edad)