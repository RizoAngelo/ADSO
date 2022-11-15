''''def numerosamigos(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma
        
def numeroamigos(num):
    sum=numeroamigos(num)
    if sum==num:
        return 'es amigo'
    else:
        return 'no es amigo'
print(numeroamigos(6))
'''''''
#usar una funcion de numero primo'''

def sumadivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma

def primos(num):
    sum=sumadivisores(num)
    if sum==1:
        return 'es primo'
    else:
        return 'no es primo'
print(primos(4))