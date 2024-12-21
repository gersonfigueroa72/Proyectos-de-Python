import numpy as np
import matplotlib.pyplot as plt

# Generamos los ángulos, que serán los que leerá el bucle
n_angulos = 15  
angulos = np.linspace(0, np.pi/2, n_angulos)

# Definimos la función proyectil
def proyectil(vx, vy, b):
    posicionx = []
    posiciony = []
    tiempo = []
    x, y, t = 0, 0, 0
    v0 = np.sqrt(vx**2 + vy**2)  # Magnitud de la velocidad inicial
    dt = 0.01  # Paso temporal

    while y >= 0:  # Mientras el proyectil esté por encima del suelo
        posicionx.append(x)
        posiciony.append(y)
        tiempo.append(t)

        # Ecuaciones de movimiento con resistencia del aire
        v = np.sqrt(vx**2 + vy**2)
        vx = vx - b * v * vx * dt
        vy = vy - 9.81 * dt - b * v * vy * dt
        
        # Actualizamos las posiciones
        x = x + vx * dt
        y = y + vy * dt
        t = t + dt

    return tiempo, posicionx, posiciony

# Función para probar distintos ángulos
def var_angulos():
    plt.figure()  # Crear una nueva gráfica

    for angulo in angulos:
        vx = v0 * np.cos(angulo)
        vy = v0 * np.sin(angulo)
        t, x, y = proyectil(vx, vy, b)

        # Graficamos la distancia máxima alcanzada para cada ángulo
        plt.scatter(max(x), np.degrees(angulo), label=f'Ángulo = {np.degrees(angulo):.1f}°')

    # Añadimos etiquetas y otras características
    plt.xlabel('Posición máxima en el eje x')
    plt.ylabel('Ángulo (grados)')
    plt.title('Distancia máxima horizontal para diferentes ángulos')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecutamos nuestra función
var_angulos()
