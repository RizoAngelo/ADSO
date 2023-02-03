import random

def numeros(x,y,z):
    if x*y==z:
        return "correctos"
    else:
        return "incorrecto"

for i in range(10):
    x=round(random.randrange(100))
    y=round(random.randrange(100))
    z=round(random.randrange(100))
    print(x,'*',y,"=",z,numeros(x,y,z))