import numpy as np
import matplotlib.pyplot as plt

# Constantes
L = 1000   # Lado del cuadrado
r = 0.5  # Radio de las partículas
epsilon = 1  # Profundidad del pozo potencial de Lennard-Jones
sigma = 4    # Parámetro de Lennard-Jones
dt = 0.000001      # Paso de tiempo
n_steps = 1000 # Número de pasos de tiempo
n_particles = 4
T = 10       # Temperatura del sistema
k_B = 1.38e-23 # Constante de Boltzmann
m = 1e-5        # Masa de las partículas


# Inicialización de posiciones y velocidades específicas
def inicializar(N, L, T, r, k_B, m):
    # Asegurarnos de que haya al menos 4 partículas
    if N < 4:
        raise ValueError("Debe haber al menos 4 partículas para colocarlas en las esquinas.")

    # Posiciones en las esquinas del cuadrado L
    posiciones = np.array([
        [0.1, 0.1],      # Esquina inferior izquierda
        [0.1, L-0.1],      # Esquina superior izquierda
        [L-0.1, 0.1],      # Esquina inferior derecha
        [L-0.1, L-0.1]       # Esquina superior derecha
    ])
    
    # Si hay más de 4 partículas, inicializamos las posiciones adicionales aleatoriamente
    if N > 4:
        for i in range(4, N):
            while True:
                pos = np.random.uniform(r, L - r, 2)
                if all(np.linalg.norm(pos - posiciones[j]) > 2 * r for j in range(len(posiciones))):  # Evitar superposición
                    posiciones = np.vstack([posiciones, pos])
                    break
    
    # Desviación estándar de la velocidad en cada dirección
    sigma_vel = np.sqrt(k_B * T / m)

    # Velocidades iniciales según distribución normal
    velocidades = np.random.normal(0, sigma_vel, (N, 2))  # Media 0, desviación estándar sigma_vel
    
    return posiciones[:N], velocidades


# Fuerza de Lennard-Jones
def lennard_jones_force(rij, epsilon, sigma, r_min=1e-20):
    r2 = np.dot(rij, rij)  
    # Evitar que r2 sea menor que r_min^2 para prevenir divisiones por cero
    if r2 < (r_min * sigma)**2:
        r2 = (r_min * sigma)**2
    r6 = r2**3
    r12 = r6**2
    force_magnitude = 24 * epsilon * (2 * (sigma**12 / r12) - (sigma**6 / r6))
    
    # Multiplicar por el vector unitario rij/|rij| para obtener la dirección de la fuerza
    return force_magnitude * rij / np.sqrt(r2) 

# Método de Verlet
def verlet_step(posiciones, velocidades, fuerzas, dt, epsilon, sigma, L, r):
    N = posiciones.shape[0]
    nuevas_fuerzas = np.zeros_like(fuerzas, dtype=np.float64)
    nuevas_posiciones = posiciones + velocidades * dt + 0.5 * (fuerzas / m) * dt**2
    nuevas_velocidades = np.zeros_like(velocidades)
    
    # Asegurarse que las partículas no salgan del cuadrado y aplicar condiciones de contorno periódicas
    nuevas_posiciones %= L
    
    for i in range(N):
        for j in range(i + 1, N):
            rij = nuevas_posiciones[i] - nuevas_posiciones[j]
            rij -= L * np.round(rij / L)  # Condiciones de contorno periódicas
            dist = np.linalg.norm(rij)
            
            if dist < 2 * r:
                # Colisión elástica: intercambiar velocidades
                velocidades[i], velocidades[j] = -velocidades[i], -velocidades[j]
            
            # Calcular las fuerzas de Lennard-Jones
            fuerza = lennard_jones_force(rij, epsilon, sigma)
            nuevas_fuerzas[i] += fuerza
            nuevas_fuerzas[j] -= fuerza
    
    nuevas_velocidades = velocidades + 0.5 * (fuerzas / m + nuevas_fuerzas / m) * dt
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
colores=['blue', 'orange','green','red']

# Graficar las trayectorias de las partículas
plt.figure(figsize=(8, 8))
for i in range(n_particles):
    # Trayectoria
    plt.scatter(trayectorias[:, i, 0], trayectorias[:, i, 1], label=f'Partícula {i+1}', s=5, alpha=0.2)
    # Punto inicial
    plt.scatter(trayectorias[0, i, 0], trayectorias[0, i, 1], color=colores[i], marker='o', label=f'Inicio Partícula {i+1}',s=30)
    # Punto final
    plt.scatter(trayectorias[-1, i, 0], trayectorias[-1, i, 1], color=colores[i], marker='x', label=f'Fin Partícula {i+1}', s=100)

plt.xlim(0, L)
plt.ylim(0, L)
plt.xlabel('Posición en x')
plt.ylabel('Posición en y')
plt.title('Trayectorias de las partículas')
plt.legend()
plt.grid(True)
plt.show()