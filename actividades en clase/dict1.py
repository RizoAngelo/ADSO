prueba_olimpica={}
while True:
    name= input("nombre del participate: ")
    if name == "":
        break
    score= int(input('ingresar metros(M) recorridos: '))
    if score not in range(0,50):
        break
    
    if name in prueba_olimpica:
        prueba_olimpica[name] += (score,)
    else:
        prueba_olimpica[name] = (score,)

for name in sorted(prueba_olimpica.keys()):
    adding = 0
    counter = 0
    for score in prueba_olimpica[name]:
        adding += score
        counter += 1
    
    print(name, '', adding / counter)