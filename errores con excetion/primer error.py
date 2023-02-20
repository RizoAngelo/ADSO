def numero(dic):
    a=0
    for dic in dicionario:
        a+=dic[num]
        raise
        
try: 
    num=input("ingrese el numero que quiera buscar en el diccionario: ")
    numero(num)
    dicionario=[{"Angelo":1,"Jose":2,"Dario":3,"carlos":4,"Marelis":5}]

except KeyError:
    print("no se encuentra la clave que ingreso")
