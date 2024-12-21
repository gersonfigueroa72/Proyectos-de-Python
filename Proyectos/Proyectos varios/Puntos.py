'''
Realice un programa orientado a objetos en el cual, ingresamos un total de n
puntos (0<=n<=10), a los cuáles se les iniciará a cada uno en una posición inicial aleatoria
diferente en coordenadas cartesianas (x, y, z), dónde inicialmente las coordenadas deben de
estar en valores 0<=x,y,z<=1000. El programa debe considerar lo siguiente:
'''
import random

class Vector:
    def __init__(self):
        self.x = random.randint(1, 1000)
        self.y = random.randint(1, 1000)
        self.z = random.randint(1, 1000)

    def mostrar(self):
        print(F"({self.x}, {self.y}, {self.z})")

# Crear una lista para almacenar los vectores aleatorios
vectores = []

# Generar 5 vectores aleatorios y agregarlos a la lista
for _ in range(10):
    vector = Vector()
    vectores.append(vector)

# Mostrar los vectores almacenados en la lista
print("Vectores aleatorios generados:")
for vector in vectores:
    vector.mostrar()


        