Beatles =  []
print("Paso 1:", Beatles)
Beatles.append("john lennon, Paul McCartney, George Harrison")
print("Paso 2:", Beatles)
for i in range (1):
    banda = input("ingrese su banda ")
    Beatles.append(banda)
print("Paso 3:", Beatles)
del banda [0]
print("Paso 4:", Beatles)

# paso 5
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))