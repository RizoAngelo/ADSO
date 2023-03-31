
def area_cuadrado(lado):
    i=lado*lado
    return i   


def perimetro_cuadrado(perimetro):
    a=perimetro*4
    return a

def area_cubo(base,altura):
    a=base*altura
    return a


def media(lista):
    media=0
    if len(lista)%2==0: 
        for i in range(len(lista)):
            if len(lista)>2:
                del lista[0]
                del lista[-1]
                media=(lista[0]+lista[1])/2
    else:
        for i in range(len(lista)):
            if len(lista)>1:
                del lista[0]
                del lista[-1]
                media=lista
    return media


    
    

            
        
  
