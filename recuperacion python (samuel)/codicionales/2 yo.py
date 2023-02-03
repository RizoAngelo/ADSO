edad=int(input("Cuanto años tienes:\n"))
if edad<18:
    print("usted es meno de edad no puedo ingresar")
else:
    genero=input("Usted es hombre o mujer: \n")
    if genero.lower()=="hombre":
        print("costo de ingreso: 20.000\nno consumible y no hay devoluciones")
        pago=int(input("con que billete va apagar: \n"))
        if pago<20000:
            print("no le alcaza para entrar porfavor valla a retirar plata")
        else:
            cambio=pago-20000
            print("tome sus vueltas",cambio,"\ndifrute la fiesta")
    elif genero.lower()=="mujer":
        print("costo de ingreso: 19.000\nincluye bebidas de bienvenida sin devoluciones")
        pago=int(input("con que billete va apagar: \n"))
        if pago<19000:
            print("no le alcaza para entrar porfavor valla a retirar plata")
        else:
            cambio=pago-19000
            print("tome sus vueltas",cambio,"\ndifrute la fiesta")
    else:
        print("por favor aclare el genero")
