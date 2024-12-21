#Crear una clase Planeta, con diámetro, masa, superficie y volumen de atributos, 
#y un método que determine aleatoriamente las coordenadas en un espacio de 3 dimensiones.
#Luego, crear una lista de objetos tipo Planeta, en donde se tengan todos los objetos del sistema solar.
import math
import random
class Planeta:
    def __init__(self,diametro,masa,superficie,volumen):
        diametro.diametro=diametro
        masa.self=masa
        superficie.self=4*math.pi*pow(diametro/2, 2)
        volumen.self=(4/3)*math.pi*pow(diametro/2,3)
    def coordenadas(x,y,z,p): 
        x=random.randint(0,100)
        y=random.randint(0,100)
        z=random.randint(0,100)
        p=[x,y,z]
        print(9)
        return p
        
    
