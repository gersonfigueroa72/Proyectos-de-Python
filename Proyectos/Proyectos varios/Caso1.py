import numpy as np
import matplotlib.pyplot as plt

# Parámetros de simulación
LADO_CUADRADO = 10.0  # Tamaño del área de simulación
N = 4  # Número de partículas
DT = 0.001  # Paso de tiempo
NUM_PASOS = 2  # Número de iteraciones
EPSILON = 1e-20  # Profundidad del potencial de Lennard-Jones
SIGMA = 4  # Distancia donde el potencial es cero
MASA = 1e-4  # Masa uniforme
RADIO = 0.01  # Radio de las partículas

# Configuración inicial
def inicializar_simulacion():
    posiciones = np.array([[0.9*LADO_CUADRADO, 0.9*LADO_CUADRADO], 
                        [0.1*LADO_CUADRADO, 0.1*LADO_CUADRADO], 
                        [0.1*LADO_CUADRADO, 0.9*LADO_CUADRADO], 
                        [0.9*LADO_CUADRADO, 0.1*LADO_CUADRADO]], dtype=float)
    velocidades = np.zeros((N, 2))
    return posiciones, velocidades

# Cálculo de fuerzas utilizando el potencial de Lennard-Jones
def calcular_fuerzas(pos):
    aceleraciones = np.zeros_like(pos)
    for i in range(N):
        for j in range(i + 1, N):
            dist_vector = pos[j] - pos[i]
            distancia = np.linalg.norm(dist_vector)
            if distancia > 0 and distancia > 2 * RADIO:  # Solo aplica fuerza si están fuera del rango de colisión
                fuerza_magnitud = 24 * EPSILON * ((2 * (SIGMA / distancia)**12) - (SIGMA / distancia)**6) / distancia
                fuerza_vector = fuerza_magnitud * dist_vector
                aceleraciones[i] += fuerza_vector / MASA
                aceleraciones[j] -= fuerza_vector / MASA
    return aceleraciones

# Manejo de colisiones entre partículas
def manejar_colisiones(pos, vel):
    for i in range(N):
        for j in range(i + 1, N):
            dist_vector = pos[j] - pos[i]
            distancia = np.linalg.norm(dist_vector)
            if distancia < 2 * RADIO:  # Verifica si están colisionando
                # Calcula la dirección y magnitud de la velocidad en la dirección de colisión
                normal = dist_vector / distancia
                v_relativa = vel[i] - vel[j]
                velocidad_normal = np.dot(v_relativa, normal)

                # Actualiza las velocidades para que reboten elásticamente
                if velocidad_normal < 0:  # Solo corrige si están acercándose
                    impulso = 2 * velocidad_normal / (1 / MASA + 1 / MASA)
                    vel[i] -= impulso * normal / MASA
                    vel[j] += impulso * normal / MASA

# Simulación paso a paso con el método de Velocity Verlet
def simular():
    posiciones, velocidades = inicializar_simulacion()
    for _ in range(NUM_PASOS):
        aceleraciones = calcular_fuerzas(posiciones)
        velocidades += 0.5 * aceleraciones * DT 
        posiciones += velocidades * DT
        
        # Aplicar condiciones de frontera reflectantes
        for i in range(N):
            for d in range(2):  # Revisar cada componente (x, y)
                if posiciones[i, d] < RADIO:
                    posiciones[i, d] = RADIO
                    velocidades[i, d] = -velocidades[i, d]
                elif posiciones[i, d] > LADO_CUADRADO - RADIO:
                    posiciones[i, d] = LADO_CUADRADO - RADIO
                    velocidades[i, d] = -velocidades[i, d]

        # Manejo de colisiones entre partículas
        manejar_colisiones(posiciones, velocidades)

        nuevas_aceleraciones = calcular_fuerzas(posiciones)
        velocidades += 0.5 * nuevas_aceleraciones * DT
    return posiciones

# Gráfica final de posiciones
def graficar(pos):
    plt.figure(figsize=(8, 8))
    plt.scatter(pos[:, 0], pos[:, 1], s=(RADIO * 2000), color="blue", label="Posiciones Finales")
    for i in range(N):
        plt.text(pos[i, 0], pos[i, 1], f"{i + 1}", ha='right', color="blue")
    plt.xlim(-0.1*LADO_CUADRADO, 1.1*LADO_CUADRADO)
    plt.ylim(-0.1*LADO_CUADRADO, 1.1*LADO_CUADRADO)
    plt.xlabel("Posición X")
    plt.ylabel("Posición Y")
    plt.title("Posiciones finales de las partículas")
    plt.legend()
    plt.grid()
    plt.show()

# Ejecución de la simulación y graficación
if __name__ == "__main__":
    posiciones_finales = simular()
    print("Posiciones finales de cada partícula:")
    for i, pos in enumerate(posiciones_finales):
        print(f"Partícula {i + 1}: X = {pos[0]:.3f}, Y = {pos[1]:.3f}")
    graficar(posiciones_finales)