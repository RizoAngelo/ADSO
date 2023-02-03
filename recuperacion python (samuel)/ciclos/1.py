
capital=float(input("¿cantida invertido?: \n"))
intereses=float(input("¿interes anual?:\n "))
años=int(input("¿años de invercion?:\n "))
for i in range(años):
    capital *=1+intereses/100
    print("capital tras", str(i+1),"años: ", str(round(capital,2)))
