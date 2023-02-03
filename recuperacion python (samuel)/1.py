"pregunta 1"

def funcion(num):
    while num>0:
        if num%2==0:
            print(num)
        num-=1
funcion(12)
"perdi prenguta porque pensaba que comenzaba desde el 1 hasta el 9 pero era que comenzaba desde el 12 hasta el 2"
print("_________________________________________________________________________________________________")
"pregunta 2"
def funcion(dictionary):
    for f in dictionary.items():
        print(d)
d = {"gato":"chat","perro":"chien","caballo":"cheval"}
funcion(d)
print("__________________________________________________________________________________________________")
"esta pregunta lo perdi porque pensaba que value era el que inprimia las claves y valor pero era items el que imprimia lo que hay en la lista con sus respectivas clave y valor"
"pregunta 3"
def funcion(tam,div):
    for i in range(1,tam):
        if(i%div==0):
            print(i,"es multiplo de ",div)
        else:
            print(i,"No es multiplo de ",div)
funcion(19,3)
print("___________________________________________________________________________________________________")
"este programa lo perdi porque pensaba que imprimia 7"
"pregunta 5"
print("la witsi witsi araña\nsubio a su teleraña.\n")
print("*****")
print("vino la lluvia\ny se la llevo.")
print("___________________________________________________________________________________________________")
"este programa lo perdi porque pensaba que imprimia 3 linia pero no me di cuenta de las \n que imprimia por separado las linea"
""
"pregunta 7"
a=4
b=3
c=5
rta=c//b+a*a-b+c
print(rta)
print("___________________________________________________________________________________________________")
"este la perdi por hacer la operacion mal y al final puse 66 pero era 19"
"pregunta 8"
def funcion(tam):
    lista=[i//2 for i in range(tam)]
    print(lista)
funcion(5)
print("___________________________________________________________________________________________________")
"este programa lo perdi porque imprimia 1,1,2,2,3 pero comenzaba desde el cero"
"pregunta 9"
def funcion(a,b):
    if a>b:
        print("descendente")
    elif a<b:
        print("ascendente")
    else:
        print("iguales")
a=1/5
b=1/4
funcion(a,b)
print("___________________________________________________________________________________________________")
"este programa lo perdi porque lei mal el progroma y pensaba que dicia si a es mayor que b en donde esta elif a<b: y por eso me equivoque en esta pregunta"
"pregunta 12"
def funcion(lista):
    list2=[]
    for i in my_list:
        if i in list2:
            list2.append(i)
        print(list2)
my_list=[1,2,4,4,1,4,2,6,2,9]
funcion(my_list)
print("___________________________________________________________________________________________________")
"este programa lo perdi porque no compredia muy bien lo que hace el que es lo que haci el programa"
"pregunta 13"
def funcion(a,b,c):
    for i in range (a,b,c):
        print(i)
funcion(50,0,-5)
print("___________________________________________________________________________________________________")
"este programa lo perdi porque al yo ver el bucle no me percate que comenzaba desde 50 hasta el 5 porque el 0 no lo imprime"
"pregunta 14"
def funcion(t1,t2):
    if(len(t1)>len(t2)):
        return "t1 es mayor"
    elif(len(t1)<len(t2)):
        return "t2 es mayor"
    else:
        return "son iguales"
tuple1=1000,2000,3000
tuple2=("a",2,"c",4,"d")
print(funcion(tuple1,tuple2))
print("___________________________________________________________________________________________________")
"este programa lo perdi porque pensaba que si el tuple2 combinaba el tuple1 en las a c d  pero no solo era un texto "