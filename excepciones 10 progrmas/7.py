def numero(num):
    try:
        if num* -1:
            print("resultado de la multiplicacion",num)
    except TypeError:
        print("no se puede multiplicar con negativos")
angelo=input("intruduce letra")
print(numero(angelo))


