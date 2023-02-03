semaforo=input("¿que color esta el semaforo?: \n")
if semaforo.lower()=="verde":
    print("puede seguir")
elif semaforo.lower()=="amarillo":
    print("valla frenado")
elif semaforo.lower()=="rojo":
    print("detengase")
else:
    print("no coincide con los colores de lo semaforo") 