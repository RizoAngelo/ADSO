from ast import Str
hora = int(input("que hora es "))
minutos = int(input("que minuto es "))
segundos = int(input("que segundo es "))
if (hora<=12):
    print (str(hora), " : ", str(minutos), ":", str(segundos))
    segundoss= segundos + 1
else:
    print ("xxxxxxx")
if segundos == 60:
    minutoss = minutos + 1
    print (str(hora), " : ", str(minutoss), ":", str(segundoss))


