#def divisores(num):
#    suma=0
#    for i in range(1,num+1):
#        if num%i==0:
#            suma+=1
#    return suma

#print(divisores(20))

def sumadivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma

def perfectos(num):
    sum=sumadivisores(num)
    if sum==num:
        return 'perfecto'
    else:
        return 'no es perfecto'
print(perfectos(6))