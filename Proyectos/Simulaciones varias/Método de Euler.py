import numpy as np
import matplotlib.pyplot as plt

# Definimos los valores iniciales
b = 0.00004 # b es B_2/m
g = 9.81
v0 = 700
theta = np.pi / 6
vox = v0 * np.cos(theta)
voy = v0 * np.sin(theta)
N = 10000
dt = 0.01

# Función que resuelve el problema del movimiento de un proyectil con y sin resistencia del aire
def proyectil(vox: float, voy: float, b: float):
    posicionx = []
    posiciony = []
    velocidadx = []
    velocidady = []
    tiempo = []
    
    # Inicialización de las variables fuera del bucle
    t = 0
    x = 0
    y = 0
    v = v0

    for i in range(N):
        posicionx.append(x)
        posiciony.append(y)
        velocidadx.append(vox)
        velocidady.append(voy)
        tiempo.append(t)
        
        # Iteración de las velocidades
        vox = vox - b * v * vox * dt
        voy = voy - g * dt - b * v * voy * dt
        
        # Iteración de la velocidad
        v = (vox**2 + voy**2)**0.5
        
        # Iteración de las posiciones
        x = x + vox * dt
        y = y + voy * dt
        
        # Iteración del tiempo
        t = t + dt
        
        # Condiciones de parada del bucle: si el proyectil cae al suelo o deja de moverse en x
        if y <= 0 or vox <= 0:
            break        

    return tiempo, posicionx, posiciony 

# Ejecutar la simulación
simulacion = proyectil(vox, voy, b)
T = simulacion[0]
X = simulacion[1]
Y = simulacion[2]

# Imprimir la altura máxima en y

print(f"la altura máxima recorrida es: {max(Y)}")

# Imprimir la distanica final en x
print(f"La distancia recorrida en x es: {X[-1]}")

# Graficar posición en x vs tiempo
plt.plot(T, X, label='Posición en x vs tiempo')
plt.legend()
plt.xlabel('Tiempo(s)')
plt.ylabel('Posición en el eje x(m)')
plt.show()

# Graficar posición en y vs tiempo
plt.plot(T, Y, label='Posición en y vs tiempo')
plt.legend()
plt.xlabel('Tiempo(s)')
plt.ylabel('Posición en el eje y(m)')
plt.show()

#Ahora haremos una función que nos permita ver distintas soluciones para las mismas condiciones
#iniciales, aunque registrando solamente el alcance maximo en x. variaremos los angulos, y de esta forma determinaremos 
#que ángulo es el que tiene el mayor alcance horizontal

#generamos los ángulos, que será los que leerá el bucle

n_angulos = 15  
angulos = np.linspace(0.6544985, 0.6894051, n_angulos)
angulos_lista = angulos.tolist()

def var_angulos():
    plt.figure()  #Crear una nueva gráfica

    for angulo in angulos:
        vx = v0 * np.cos(angulo)
        vy = v0 * np.sin(angulo)
        simular=proyectil(vx, vy, b)
        t = simular[0]
        x = simular[1]
        y = simular[2]
        # Graficamos la trayectoria para este ángulo
        plt.scatter(max(x), np.degrees(angulo), s=100, label=f'Ángulo = {np.degrees(angulo):.1f}, xmax={round(max(x),2)}')

    # Añadimos etiquetas
    plt.xlabel('Alcance máximo en x(m)')
    plt.ylabel('Ángulo')
    plt.title('Trayectorias de un proyectil para diferentes ángulos')
    plt.legend(fontsize=15)
    plt.grid(True)
    plt.show()

#ejecutamos nuestra función:

var_angulos()

