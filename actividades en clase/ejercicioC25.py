def funcion(a, b, c):
try: 
    a=int(input ("ingresar a: "))
    b=int(input ("ingresar  b: "))
    c=int(input ("ingresar c: "))
    x=((-(b)+((b ** 2 - 4*a*c) ** 0.5) ))
    if x != 0:
        x= x / (2 * a)
        print(" El resultado de la función cuadratica positiva es: ", x)
except ZeroDivisionError:
    print("su valor no puede se igual a cero")
except ValueError:
        print("debe ser un numero natural")
except:
        print("vacio")
        
print (funcion(a,b,c))


"""def funcion(a, b, c):
    try:
        x=((-(b)+((b ** 2 - 4*a*c) ** 0.5) ))
        if x != 0:
            x= x / (2 * a)
            return (" El resultado de la función cuadratica positiva es: ", x)
        else:
            return ("resultado incorrecto")
    except ZeroDivisionError:
        print("su valor no puede se igual a cero")
    except TypeError:
        print("debe ser un numero natural")
    except:
        print("")    
a=int(input ("ingresar a: "))
b=int(input ("ingresar  b: "))
c=int(input ("ingresar c: "))"""