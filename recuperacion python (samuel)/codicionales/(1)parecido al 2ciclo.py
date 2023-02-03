clave="the last of us"
cliente="angelo29@gmail.com"
correo=input("introdusca el correo: \n")
if cliente ==correo.lower():
    contraseña=input("introdusca la contraseña: \n")
    if clave ==contraseña.lower():
        print("contraseña correcta\nBienvenido")
    else:
        print("constraseña incorrecta porfavor vuelva intentarlo")
else:
    print("correo incorrecto porfavor vuelva intentarlo")

    