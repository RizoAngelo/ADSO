print("impresion desde el modulo de angelo")
print(__name__)
if __name__=="__main__":
    print("estoy en el modulo")
else:
    print("estoy en el ejecutable")    
def numero(num):
    cont = 0
    for i in range (2,num,1):
        if num%i==0:
            cont +=1
    if cont>0:
        return ("el número es primo")
    else:
        return ("el número no es primo")
num = int(input("ingrese un número= "))
print(numero(num))
def numero(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print("")
n = int(input("Introduce la altura del triángulo (entero positivo): "))
print(numero(n))
