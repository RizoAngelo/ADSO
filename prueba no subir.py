import random
class Estrella:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.forma=random.choice(["*", ".", ".", "."])
	def __str__(self):
		return self.forma
class Cielo:
	def __init__(self,filas,columnas):
		self.filas=filas
		self.columnas=columnas
		self.cielo=[]
		for i in range(filas):
			self.cielo.append([])
			for j in range(columnas):
				self.cielo[i].append(" ")
	def poner_estrellas(self,numero_estrellas):
		for i in range(numero_estrellas):
		    x = random.randint(0, self.columnas-1)
		    y = random.randint(0, self.filas-1)
            estrella = Estrella(y, x)
            self.cielo[y][x] = estrella
	
	def mostrar(self):
		for i in range(self.filas):
			for j in range(self.columnas):
				print(self.cielo[i][j], end="")
			print()
import os
os.system("cls")
cielo_1=Cielo(18,60)
cielo_1.poner_estrellas(150)
cielo_1.mostrar()