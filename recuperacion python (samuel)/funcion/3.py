def preguntas(x):
    if x==pepe:
        return "correcto"
    else:
        return "murio envenamiento"
x="1"
pepe=int(input("¿como murio socrate?\n1.envenamiento\n2.cancer\n3.por honor\nR:"))
print(preguntas(x))
print("_______________________________________________________________________________________")
def pregunta(d):
    if d==mario:
        return "correcto"
    else:
        return "zeus el dios de trueno"

d="5"
mario=int(input("¿quien es el dios de trueno en la meteologia griega?\n1.hercules\n2.andromeda\n3.buda\n4.valkidia\n5.zeus\nR:"))
print(pregunta(d))

def prefunta(a):
    if a==don:
        return "correcto"
    else:
        return "medusa fue las mas temida por los hombres"
a="medusa"
don=input("como se llama la que tiene cabeza de serpiente y con su mirada puede poner de estatua todo lo que mira\nR:")