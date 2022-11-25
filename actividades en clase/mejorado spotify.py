Spotify={}
def Artista(Spotify):
    Artista=input('Ingrese nombre del artista: ')
    Spotify.update({Artista:{}})
    return Spotify
def agregarcancionalartista(Spotify):
    Artista=input('Ingrese el nombre del artista que quiere buscar: ')
    if Artista not in Spotify:
        print('El artista no existe quisiera agregralo')
        a=input("agregar artista (si) o quiere volver a la lista (no) o quiere volver a buscar solo coloque (buscar): ")
        if a == "si":
            Artista=input('Ingrese nombre del artista: ')
            Spotify.update({Artista:{}})
            return agregarcancionalartista(Spotify)

        elif a == 'no':
            return ("regreso a la lista"), Spotify#repr
        elif a == "buscar":
            return agregarcancionalartista(Spotify)
        elif a == "":
            return("no puede dejar el campo vacio"),Spotify
        else:
            return Spotify
    cancion=input("Ingrese la cancion: ")
    genero=input("Ingrese el genero de la cancion: ")
    duracion=input("Cuanto dura la cancion: ")
    if Artista in Spotify:
        Spotify.update({Artista:{"cancion":cancion,"genero":genero,"duracion":duracion}})

def buscarartista(Spotify):
    Buscar=input('Que artista quiere buscar: ')
    for b in Spotify.keys():
        if Buscar in b:
            return('el artista que busca',Buscar,"si se encuentra")
        else:
            return('el nombre de este artista',Buscar,'no se encuentra por favor registre el artista')
def eliminarunartista(Spotify):
    eliminar=input("Que artista quiere eliminar: ")
    for G in Spotify.keys():
        if eliminar==G:
            del Spotify[G]
            return("El (La) artista",eliminar,"fue eliminada con exito de Spotify")
        return None
    return("este artista no se encuentra en la Spotify")
def mayor(Spotify):
    a=int
    mayor_valor=0
    for p in (Spotify.keys()):
        minutos=Spotify[p]["duracion"][0]
        minutos+=Spotify[p]["duracion"][1]
        segundos=Spotify[p]["duracion"][3]
        segundos+=Spotify[p]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if mayor_valor<=segundos:
            mayor_valor=segundos
            a=Spotify[p]['cancion']
            
    return("la cancion mas larga es:", a)
    
def menor(Spotify):
    menor = dict
    menor_valor=9e99999
    for z in (Spotify.keys()):
        minutos=Spotify[z]["duracion"][0]
        minutos+=Spotify[z]["duracion"][1]
        segundos=Spotify[z]["duracion"][3]
        segundos+=Spotify[z]["duracion"][4]
        segundos=int(segundos)+int(minutos)*60
        if menor_valor>=segundos:
            menor_valor=segundos
            menor=Spotify[z]['cancion']
    return("la cancion mas corta es", menor)

while True:
    print("1-Crear un atista")
    print("2-Crear una cancion para un artita")
    print("3-Buscar un artista")
    print("4-Eliminar un artista")
    print("5-Mostrar que cancion es mas larga")
    print("6-Mostrar que cancion es mas corta")
    print("7-Mostrar todos los artista con su respectivas canciones")
    print("8-Salir")
    Letf4dead=int(input("Digite unas de las opciones (1-8):  ")) 

    match Letf4dead:
        case 1:
            print(Artista(Spotify))
        case 2:
            print(agregarcancionalartista(Spotify))
        case 3:
            print(buscarartista(Spotify))
        case 4:
            print(eliminarunartista(Spotify))
        case 5:
            print(mayor(Spotify))
        case 6:
            print(menor(Spotify))
        case 7:
            print("Esta es la lista de los artista con su respectivas canciones; ",Spotify)
        case 8:
            print("Que no sea la ultima vez que nos vemos :)",exit())
            
        case "":
            print("no puede dejar el campo vacio")
            break