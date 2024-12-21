import numpy as np
import matplotlib.pyplot as plt

# Constantes
L = 1e-6   # Lado del cuadrado
r = 1e-10  # Radio de las partículas
epsilon = 1  # Profundidad del pozo potencial de Lennard-Jones
sigma = 1e-8    # Parámetro de Lennard-Jones
dt = 0.01      # Paso de tiempo
n_steps = 100 # Número de pasos de tiempo
n_particles = 4
T = 0         # Temperatura del sistema
k_B = 1.38e-23 # Constante de Boltzmann
m = 1e-20        # Masa de las partículas

# Inicialización de posiciones y velocidades
def inicializar(N, L, T, r, k_B, m):
    posiciones = np.zeros((N, 2))
    
    # Desviación estándar de la velocidad en cada dirección
    sigma_vel = np.sqrt(k_B * T / m)
    
    # Velocidades iniciales según distribución normal
    velocidades = np.random.normal(0, sigma_vel, (N, 2))  # Media 0, desviación estándar sigma_vel
    
    for i in range(N):
        while True:
            pos = np.random.uniform(r, L - r, 2)
            if all(np.linalg.norm(pos - posiciones[j]) > 2 * r for j in range(i)):  # Asegurar no superposición
                posiciones[i] = pos
                break
    
    return posiciones, velocidades

# Fuerza de Lennard-Jones
def lennard_jones_force(rij, epsilon, sigma):
    r2 = np.dot(rij, rij)
    r6 = r2**3
    r12 = r6**2
    force_magnitude = 6 * epsilon * (-(sigma**12 / r12) +2 * (sigma**6 / r6))
    return force_magnitude 

# Método de Verlet
def verlet_step(posiciones, velocidades, fuerzas, dt, epsilon, sigma, L, r):
    N = posiciones.shape[0]
    nuevas_fuerzas = np.zeros_like(fuerzas)
    nuevas_posiciones = posiciones + velocidades * dt + 0.5 * (fuerzas/m) * dt**2
    nuevas_velocidades = np.zeros_like(velocidades)
    
    # Asegurarse que las partículas no salgan del cuadrado y aplicar condiciones de contorno periódicas
    nuevas_posiciones %= L
    
    for i in range(N):
        for j in range(i+1, N):
            rij = nuevas_posiciones[i] - nuevas_posiciones[j]
            rij -= L * np.round(rij / L)  # Condiciones de contorno periódicas
            dist = np.linalg.norm(rij)
            if dist < 2 * r:
                # Colisión elástica: intercambiar velocidades
                velocidades[i], velocidades[j] = -velocidades[i], -velocidades[j]
            # Calcular las fuerzas de Lennard-Jones
            nuevas_fuerzas[i] += lennard_jones_force(rij, epsilon, sigma)
            nuevas_fuerzas[j] -= lennard_jones_force(rij, epsilon, sigma)
    
    nuevas_velocidades = velocidades + 0.5 * (fuerzas + nuevas_fuerzas) * dt
    return nuevas_posiciones, nuevas_velocidades, nuevas_fuerzas

# Inicializar posiciones y velocidades
posiciones, velocidades = inicializar(n_particles, L, T, r, k_B, m)

# Inicializar las fuerzas
fuerzas = np.zeros_like(posiciones)

# Simulación
trayectorias = [posiciones.copy()]
for step in range(n_steps):
    posiciones, velocidades, fuerzas = verlet_step(posiciones, velocidades, fuerzas, dt, epsilon, sigma, L, r)
    trayectorias.append(posiciones.copy())

# Convertir trayectorias a numpy array para graficar
trayectorias = np.array(trayectorias)

# Graficar las trayectorias de las partículas
plt.figure(figsize=(8, 8))
for i in range(n_particles):
    # Trayectoria
    plt.plot(trayectorias[:, i, 0], trayectorias[:, i, 1], label=f'Partícula {i+1}')
    # Punto inicial
    plt.scatter(trayectorias[0, i, 0], trayectorias[0, i, 1], color='green', marker='o', label=f'Inicio Partícula {i+1}')
    # Punto final
    plt.scatter(trayectorias[-1, i, 0], trayectorias[-1, i, 1], color='red', marker='x', label=f'Fin Partícula {i+1}')

plt.xlim(0, L)
plt.ylim(0, L)
plt.xlabel('Posición en x')
plt.ylabel('Posición en y')
plt.title('Trayectorias de las partículas')
plt.legend()
plt.grid(True)
plt.show()