#2. Ternas pitagoricas. Un tringulo rectangulo puede tener lados que sean todos enteros, el conjunto de 3 valores enteros para los lados de un triangulo rectangulo se conoce como una terna pitagorica. Estos 3 lados deben satisfacer la relacion que la suma de los cuadrados de los dos lados es igual al cuadrado de la hipotenusa. Encuentre todas las ternas pitagóricas para el lado 1, lado 2 y la hipotenusa, todos ellos no mayores que 500. ejemplo c=3,c=4,h=5
for n in range (1,500+1):
    for c in range (1,500+1):
        x=n**2+c**2
        for i in range (1,500+1):
            h=i**2
            if x ==h:
                print("ca",n,"co",c,"h",i,sep="-")