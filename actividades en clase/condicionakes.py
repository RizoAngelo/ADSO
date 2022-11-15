import random


def ascendente(x,y):
    if x<y:
        return 'ascendente'
    elif x>y:
        return 'descendente'
    else:
        return 'iguales'

print(ascendente(1,5))

for i in range(10):
    x=round(random.randrange(100))
    y=round(random.randrange(100))
    print(x,'',y,ascendente(x,y))
    