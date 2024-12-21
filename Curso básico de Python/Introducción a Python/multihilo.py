'''
Para esto debemos empezar hablando acerca de qué es un
hilo.
Un hilo es tambien conocido como un subproceso,
estos permiten que varias parte de un programa 
se ejecuten simultaneamente, mejorando así la eficiencia
del programa.
Los hilos dentro de un mismo proceso (instrucción o instancia)
comparten el mismo espacio en memoria y recursos del sistema.
Los hilos se pueden comunicar y compartir datos de manera
más eficiente que procesos separados.
Los hilos tienen menos sobrecarga de recursos del sistema
en comparacion con los multiprocesos.
Los hilos coperan entre sí y se coordinan para realizar
tareas complejas.
'''
#En phyton usamos el modulo threading para trabajar
#con multiples hilos
#(Un modulo es un archivo que contiene un conjunto de funciones)

#EJEMPLO:

import threading
#Definimos la funcion que será ejecutada por cada hilo
def tarea(num):
    print(f"Hilo {num}: está ejecutando esta tarea")

#Ahora debemos crear a los hilos
hilos=[]
for i in range(5):
    hilo=threading.Thread(target=tarea,args=(i,))
    hilos.append(hilo)

#Inicializamos los hilos
for hilo in hilos:
    hilo.start()

#Explicación del código:
'''
Definimos una función tarea que será ejecutada por
cada hilo, esta función toma un número como argumento
para identificar el hilo.

Creamos una lista de hilos para almacenar cada hilo

Creamos cinco hilos utilizando un bucle for, 
donde cada hilo ejecutará la función tarea con 
un número único como argumento.

Iniciamos cada hilo llamando al método start().

Esperamos a que todos los hilos terminen 
utilizando el método join() para cada hilo.

Finalmente, imprimimos un mensaje indicando 
que todos los hilos han terminado.
'''

#EJEMPLO 2

import random
import time

#Clase para representar un estudiante:
class Estudiante(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre=nombre

    def correr(self):
        distancia_total=100
        distancia_recorrida=0
        while distancia_recorrida<distancia_total:
            #simulamos un paso
            print(f"{self.nombre} ha recorrido {distancia_recorrida} metros")
            time.sleep(0.1) #tiempo en dar el paso
        print(f"{self.nombre} ha llegado a la meta")

#Función para que el estudiante inicie su carrera:
def iniciar_carrera(estudiantes):
    print("La carrera comenzó")
    for estudiante in estudiantes:
        estudiante.start() #iniciamos cada estudiante en un hilo

nombres_estudiantes=("Gerson","Nay","xd","a")
