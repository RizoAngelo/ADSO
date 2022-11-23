Artista={}
Cancion={}
genero={}
Duracion={}
Spotify={}

def Art(Artita):
    while True:
        Artista=input("nombre del artista: ")
        if Artista == "":
            break
        
def Can(Cancion):
        while True:
            Cancion=input("nombre de la cancion: ")
            if Cancion == "":
                break

def gen(genero):
    while True:    
        genero=input("que genero es: ")
        if genero == "":
            break

def tiempo(Duracion):
    while True:    
        Duracion=input("cuanto dura la cancion: ")
        if Duracion == "":
            break
    anidado={Artista:{
                "cancion":Cancion,
                "genero":genero,
                "duracion":Duracion
                },}
    print(anidado)
print(Art("Artita"))










    
 
        