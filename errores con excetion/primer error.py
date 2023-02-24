def numero(num):
    for dic in dicionario:
        if num.v!=dic:
            return(dic[num])
        raise
        
try: 
    num=int(input("ingrese el numero que quiera buscar en el diccionario: "))
    
    dicionario={"Angelo":1,"Jose":2,"Dario":3,"carlos":4,"Marelis":5}
    pepe=list(dicionario.index(num))
    print(numero(pepe))

except KeyError:
    print("no se encuentra la clave que ingreso")
