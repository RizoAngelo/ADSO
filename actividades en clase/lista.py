import random
def llenarlista(list):
    tam=round(random.randint(5,20))
    for i in range(tam):
        list.append(round(random.randrange(100)))

def sumarlista(list):
    sum=0
    for i in list:
        sum+=i
    return sum

lista=[]
lista=llenarlista(lista)
print(lista)
print('la suma es=',sumarlista(lista)) 