def numero(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print("")
n = int(input("Introduce la altura del triángulo (entero positivo): "))
print(numero(n))