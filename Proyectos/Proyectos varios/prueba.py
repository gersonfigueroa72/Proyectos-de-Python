import threading
import random
import multiprocessing

def random_number(parametro_a_multiplicar):
    resultado = parametro_a_multiplicar * random.random()
    return resultado

def ejecutar_desde_hilo(parametro_a_multiplicar, resultado):
    resultado[0] = random_number(parametro_a_multiplicar)

# Crear una lista para almacenar el resultado
resultado = [None]

# Crear un hilo y ejecutar la función desde allí
parametro = 10
hilo = threading.Thread(target=ejecutar_desde_hilo, args=(parametro, resultado))
hilo.start()
hilo.join()

# Recuperar el número aleatorio que devuelve la función
numero_aleatorio = resultado[0]
print("Número aleatorio recuperado:", numero_aleatorio)

#inciso b)

def random_number(parametro_a_multiplicar):
    resultado = parametro_a_multiplicar * random.random()
    return resultado

def ejecutar_desde_proceso(parametro_a_multiplicar, resultado):
    resultado.value = random_number(parametro_a_multiplicar)

# Crear un objeto para almacenar el resultado
resultado = multiprocessing.Value('d', 0.0)

# Crear un proceso y ejecutar la función desde allí
parametro = 10
proceso = multiprocessing.Process(target=ejecutar_desde_proceso, args=(parametro, resultado))
proceso.start()
proceso.join()

# Recuperar el número aleatorio que devuelve la función
numero_aleatorio = resultado.value
print("Número aleatorio recuperado:", numero_aleatorio)
