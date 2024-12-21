import random
import threading
''' Crear una función que devuelva un número aleatorio multiplicado por un parámetro
que recibe esa misma función, por ejemplo:'''

def num_ran(numero_a_multiplicar):
    resultado=numero_a_multiplicar*random.randint(1,100)
    numero_aleatorio=resultado/numero_a_multiplicar
    print("El resultado es: ", resultado, "El número aleatorio es: ", numero_aleatorio)
    return resultado, numero_aleatorio

#llamarla desde un hilo(multithreading) y buscar la forma de recuperar el
#número aleatorio que devuelve la función.
parametro = 10
hilo = threading.Thread(target=num_ran, args=(parametro,))
hilo.start()


#primer_numero=num_ran(3)
#print(primer_numero)