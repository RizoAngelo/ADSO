#este codigo no funciona porque lo esta hagarando como si fuera un texto
print("primera funcion")
def calculo(base,altura):
    try:
        area = (base * altura) / 2
        return area
    except TypeError:
        print("Debe se numero no letra ni caracteres especiales gracias:)")
base=(input("introduce la base\nBase:"))#lo esta hagarando como texto
altura=(input("introduce la altura\nAltura:"))#tambien lo esta hagarando como texto
print(calculo(base,altura))
print("_______________________________________________________________________________________________________________________")
#para que funcione el codigo solo debe colocar "int" atra el input como se muestra en el siguiente codigo
print("segunda funcion")
def calculo(base,altura):
    try:
        area = (base * altura) / 2
        return area
    except TypeError:
        print("Debe se numero no letra ni caracteres especiales gracias:)")
base=int(input("introduce la base\nBase:"))#lo hagara como numero
altura=int(input("introduce la altura\nAltura:"))#igual lo hagara como numero 
print(calculo(base,altura))