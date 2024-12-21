'''
A continuación veremos un ejemplo para entender
mejor el uso de join() en phyton.
Supongamos que queremos realizar tres tareas en hilos
separados y luego imprimir un mensaje cuando todas 
las tareas hayan terminado. Utilizaremos join()
para asegurarnos de que el programa espere a que todas 
las tareas hayan finalicen antes de imprimir el 
mensaje de finalización
'''
import time
import threading

#Definimos la funcion que hará una tarea:
def tarea(id_tarea):
    print(f"Tarea {id_tarea} iniciada")
    time.sleep(2) #simulamos que la tarea tardará 2s
    print("Tarea completada")

#creamos una lista en la cual almacenaremos nuestros hilos
hilos=[]
#Crear hilos e iniciar cada tarea:
for i in range(1,8):
    hilo=threading.Thread(target=tarea, args=(i,))
    hilo.start()
    hilos.append(hilo)

#Esperamos a que todos los hilos se ejecuten
for hilo in hilos:
    hilo.join()
#Cuando terminen todos los hilos, por fin 
#se enviara el sig mensaje:
print("TODAS LAS TAREAS FUERON COMPLETADAS")
