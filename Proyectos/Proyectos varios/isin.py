import numpy as np
import matplotlib.pyplot as plt
"""
Definimos la clase modelo de ising y en el constructor definimos los parametros
estos serán temperatura y el tamaño de la red (tamaño).
En el tamaño de la red nos dirá que la cantidad de espines que tendremos, si el 
tamaño es n, entonces habra n*n spines.
Por otra parte la temperatura es crucial para el modelo de ising, ya que 
La temperatura del sistema afecta la probabilidad de que un espín cambie de estado. 
A altas temperaturas, los espines tienden a orientarse aleatoriamente, 
mientras que a bajas temperaturas tienden a alinearse.

"""
class ModeloIsing:
    def __init__(self, tamano, temperatura):
        # Inicializa el modelo con el tamaño de la red y la temperatura
        self.tamano = tamano
        self.temperatura = temperatura
        # Configuración inicial aleatoria de espines (-1 o 1)
        self.espines = np.random.choice([-1, 1], size=(tamano, tamano))#crea una matriz bidimensional de spines


#Hamiltoniano del sistema.
#con esta función calculamos la energía del sistema de spins de la red bidimensional
#i,j representan las sumatorias que recorren la red de nxn
#Para cada espín en la posición (i, j), se calcula su contribución a la energía total y la de sus vecinos
    def calcular_energia(self, espines):
        # Calcula la energía total del sistema de Ising
        energia = 0 #en esta variable se guardará la energía de cada paso
        for i in range(self.tamano):
            for j in range(self.tamano):
                # Suma la energía de interacción con los vecinos derecho y abajo
                energia += -espines[i, j] * (espines[(i+1)%self.tamano, j] + espines[i, (j+1)%self.tamano])
        return energia

#En este paso utilizamos el algoritmo metropolis para hallar la energía resultante del sistema al tomar aleatoriamente
#el spin en la posición i,j e invertir ese spin. Obviante al cambiar de posicion ese spin, sus vecinos interactuaran de
#forma diferente con él, por lo tanto tambíen calculamos la nueva energía, que surge de la nueva interacción del nuevo
#espin girado con sus vecinos
#El if, es para analizar si se acepta o no el cambio del spin, basado en su nueva energía
#La energía del sistema tiende a disminuir, así que si spin_flip_energy <= 0, el cambio de espín se acepta 
#incondicionalmente porque reduce o no cambia la energía del sistema.

    def paso_metropolis(self, espines):
        # Realiza un paso de Metropolis para actualizar los espines
        i, j = np.random.randint(0, self.tamano, size=2)
        # Calcula el cambio en la energía si se invierte el espín seleccionado
        delta_energia = 2 * espines[i, j] * (espines[(i-1)%self.tamano, j] + 
                                             espines[(i+1)%self.tamano, j] +
                                             espines[i, (j-1)%self.tamano] + 
                                             espines[i, (j+1)%self.tamano])
        # Condición para invertir el espín basado en el criterio de Metropolis
        if delta_energia <= 0 or np.random.rand() < np.exp(-delta_energia / self.temperatura):
            espines[i, j] *= -1
        return espines

    def simular(self, pasos):
        # Simula el sistema de Ising por un número dado de pasos
        for _ in range(pasos):
            self.espines = self.paso_metropolis(self.espines)
        return self.calcular_energia(self.espines)


# Parámetros del modelo
tamano = 50  # Tamaño de la red bidimensional
temperatura = 2.5  # Temperatura del sistema
pasos = 100
# Crear el modelo de Ising y mostrar la distribución inicial de espines
ising_model = ModeloIsing(tamano, temperatura)
plt.imshow(ising_model.espines, cmap='binary', interpolation='nearest')
plt.title("Distribución Inicial de Espines")
plt.colorbar(label="Valor de Espín")
plt.show()

# Simular el sistema de Ising y mostrar la distribución final de espines
energia_final = ising_model.simular(pasos)
plt.imshow(ising_model.espines, cmap='binary', interpolation='nearest')
plt.title("Distribución Final de Espines")
plt.colorbar(label="Valor de Espín")
plt.show()

# Simular el modelo de Ising para diferentes temperaturas y graficar la energía promedio
temperaturas = np.linspace(0.1, 5.0, 20)  # Temperaturas a evaluar
energias_promedio = [ModeloIsing(tamano, temp).simular(pasos) for temp in temperaturas]

plt.plot(temperaturas, energias_promedio)
plt.xlabel('Temperatura')
plt.ylabel('Energía Promedio del Sistema')
plt.title('Evolución de la Energía con la Temperatura')
plt.grid(True)
plt.show()

# Graficar la energía en función de los pasos de simulación
energias = [ising_model.simular(paso) for paso in range(pasos)]
plt.plot(range(pasos), energias)
plt.xlabel('Paso de Simulación')
plt.ylabel('Energía del Sistema')
plt.title('Evolución de la Energía a lo largo de los Pasos de Simulación')
plt.grid(True)
plt.show()