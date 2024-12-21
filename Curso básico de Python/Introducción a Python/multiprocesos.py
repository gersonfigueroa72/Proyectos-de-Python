"""
En el multiproceso, multiples procesos se ejecutan
independientemente (en paralelo) y cada proceso,
tiene su propio espacio dmemoria independiente.

Lo que significa que los procesos no comparten memoria
por lo que serán mas pesados de procesar.
"""
#Ejemplo:
import multiprocessing
import math
#Funcion que calcula la raiz cuadrada de un num
def raiz_cuadrada(num):
    return math.sqrt(num)

if __name__=="__main__":
    numeros=[4,9,16,25,49]
    #Creamos el pool de procesos
    pool= multiprocessing.Pool()
    #aplicamos la funcion a cada numero en paralelo
    resultados=pool.map(raiz_cuadrada, numeros)
    #Cerramos el pool de procesos
    pool.close()
    pool.join()
    print("Raices cuadradas de los numeros: ", resultados)
'''
La línea if __name__ == "__main__": se utiliza 
comúnmente en Python para controlar el 
comportamiento del código cuando se ejecuta 
como un programa principal versus cuando se 
importa como un módulo en otro programa.
De tal forma de que si importamos este modulo a 
otro script la lista numero no se ejecutará,
haciendo que en el nuevo modulo podamos nosotros
agregar nuestra propia lista de numeros
'''
'''
Pool pertenece al modulo de multiprocessing, y se
utiliza para administrar un conjunto de procesos
en paralelo
'''