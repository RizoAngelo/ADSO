def num_primos(num):
    lista=[]
    con=0
    for i in range(num):
        cont=0
        for j in range(1,i):
            if i%j==0:
                cont+=1
        if cont==1:
            con+=1
            lista.append(i)
    return lista
def num_compuestos(num):
    lista=[]
    con=0
    for i in range(num):
        cont=0
        for j in range(1,i):
            if i%j==0:
                cont+=1
        if cont==1:
            con+=1
        else:
            lista.append(i)
    return lista

def num_perfecto(num):
    numero=num
    i=1
    divisores=0
    for a in range(num):
        divisores=0
        for i in range(1,numero):
            if (numero % i) == 0 :
                divisores=divisores+i
    if divisores==numero:
        print("es perfecto")
    else: 
        print("no es perfecto")
num_perfecto(2)
