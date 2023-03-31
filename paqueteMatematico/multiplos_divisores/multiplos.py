def multiplos(num):
    for i in range (10):
        multiplo=num*i 
        print ("los multiplos son ", multiplo)


def divisor(num):
    contador=0
    for i in range (2, num + 1):
        if (num % i == 0):
            contador+=i
    return "el numero ",num,"tiene ",contador,"divisores"

def regla(a,c,b):
    print(c*b/a)

regla(1,2,3)

    

