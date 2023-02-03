def contrasenon(contraseña):
    if clave==contraseña.lower():
        print("contraseña correcta\nBienvenido")
    else:
        print("constraseña incorrecta porfavor vuelva intentarlo")
        contrasenon(contraseña)
def usuariocliente():
    correo=input("introduzca el correo: \n")
    if cliente==correo.lower():
        contraseña=input("introduzca la contraseña: \n")
        contrasenon(contraseña)
    else:
        print("correo incorrecto")
        usuariocliente() 

cliente="angelo29@gmail.com"
clave="the last of us"
usuariocliente()


