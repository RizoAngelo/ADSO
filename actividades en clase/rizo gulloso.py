from fractions import Fraction

print('Suma, Resta, Multiplicación, Divion de fraccionarios ')

n1 = Fraction(input('Introduce primer numero fraccionario:  '))
print(n1)

n2 = Fraction(input('Introduce el segundo numero fraccionario:  '))
print(n2)


print("El resultado de la suma es: " + str(n1+n2))
print("El resultado de la resta es: " + str(n1-n2))
print("El resultado de la multiplicación es: " + str(n1*n2))
print("El resultado de la divición es: " + str(n1/n2))