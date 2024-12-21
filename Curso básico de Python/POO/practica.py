import math
import random as rn

class Planeta:
  def __init__(self, nombre: str, diametro: float, masa: float):
    self.nombre = nombre
    self.diametro = diametro
    self.masa = masa

    self.volumen = (4/3)*math.pi*pow(diametro/2,3)
    self.superficie = 4*math.pi*pow(diametro/2, 2)

    self.x = 0
    self.y = 0
    self.z = 0

  def posicion_inicial(self):
    #self.x = rn.randint(0,100)
    self.x = round(rn.uniform(0,100), 8)
    self.y = round(rn.uniform(0,100), 8)
    self.z = round(rn.uniform(0,100), 8)

  def cambiar_coordenada(self, coordenada: str, valor: int): #operadores ternarios?
    if coordenada == "x":
      if self.x + valor < 0: self.x = 0
      else: self.x += valor

    elif coordenada == "y":
      if self.y + valor < 0: self.y = 0
      else: self.y += valor

    elif coordenada == "z":
      if self.z + valor < 0: self.z = 0
      else:self.z += valor

    else:
      raise Exception("Coordenada no existente")

mercurio=Planeta("Mercurio",1,1)

