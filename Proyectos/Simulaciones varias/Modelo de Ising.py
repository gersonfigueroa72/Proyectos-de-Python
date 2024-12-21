import numpy as np
import matplotlib.pyplot as plt

# --------------------------
# Inicialización de la red
# --------------------------
def inicializar_red(L, modo='frio'):
    """
    Inicializa la red de espines para el modelo de Ising.

    Parámetros:
    - L: Tamaño de la red (LxL).
    - modo: 'frio' para arranque frío (+1) o 'caliente' para espines aleatorios.

    Retorna:
    - Una matriz de espines de tamaño LxL.
    """
    if modo == 'frio':
        return np.ones((L, L), dtype=int)
    elif modo == 'caliente':
        return np.random.choice([-1, 1], size=(L, L))
    else:
        raise ValueError("El modo debe ser 'frio' o 'caliente'")

# --------------------------
# Cálculo de energía y magnetización
# --------------------------
def calcular_energia(red, J=1, H=0):
    """
    Calcula la energía total del sistema.

    Parámetros:
    - red: Matriz de espines (LxL).
    - J: Constante de acoplamiento (default=1).
    - H: Campo magnético externo (default=0).

    Retorna:
    - Energía total del sistema.
    """
    L = red.shape[0]
    energia = 0
    for i in range(L):
        for j in range(L):
            spin = red[i, j]
            vecinos = red[(i+1)%L, j] + red[(i-1)%L, j] + red[i, (j+1)%L] + red[i, (j-1)%L]
            energia += -J * spin * vecinos - H * spin
    return energia / 2  # Dividir por 2 para evitar contar interacciones dos veces

def calcular_magnetizacion(red):
    """
    Calcula la magnetización promedio del sistema.

    Parámetros:
    - red: Matriz de espines (LxL).

    Retorna:
    - Magnetización promedio.
    """
    return np.sum(red) / red.size

# --------------------------
# Algoritmo de Metropolis
# --------------------------

def paso_metropolis(red, beta, J=1, H=0):
    """
    Realiza un paso del algoritmo de Metropolis.

    Parámetros:
    - red: Matriz de espines (LxL).
    - beta: Inverso de la temperatura (1/T).
    - J: Constante de acoplamiento (default=1).
    - H: Campo magnético externo (default=0).

    Retorna:
    - Matriz actualizada de espines.
    """
    L = red.shape[0]
    for _ in range(L**2):  # L^2 intentos de voltear espines por paso
        i, j = np.random.randint(0, L, size=2)
        spin = red[i, j]
        vecinos = red[(i+1)%L, j] + red[(i-1)%L, j] + red[i, (j+1)%L] + red[i, (j-1)%L]
        dE = 2 * J * spin * vecinos + 2 * H * spin

        # Aceptar o rechazar el cambio
        if dE < 0 or np.random.rand() < np.exp(-beta * dE):
            red[i, j] *= -1  # Voltear el espín
    return red

# --------------------------
# Simulación del modelo de Ising
# --------------------------

def simular_ising(L, T, pasos, J=1, H=0, modo='frio'):
    """
    Simula el modelo de Ising en 2D usando el algoritmo de Metropolis.

    Parámetros:
    - L: Tamaño de la red (LxL).
    - T: Temperatura.
    - pasos: Número de pasos de Metropolis.
    - J: Constante de acoplamiento.
    - H: Campo magnético externo.
    - modo: Configuración inicial ('frio' o 'caliente').

    Retorna:
    - energias: Lista de energías por paso.
    - magnetizaciones: Lista de magnetizaciones por paso.
    """
    beta = 1 / T
    red = inicializar_red(L, modo)
    energias = []
    magnetizaciones = []

    for paso in range(pasos):
        red = paso_metropolis(red, beta, J, H)
        energias.append(calcular_energia(red, J, H))
        magnetizaciones.append(calcular_magnetizacion(red))

    return energias, magnetizaciones

# --------------------------
# Cálculo de propiedades termodinámicas
# --------------------------

def calcular_cv_y_chi(energias, magnetizaciones, beta):
    """
    Calcula el calor específico (C_v) y la susceptibilidad magnética (chi).

    Parámetros:
    - energias: Lista de energías registradas durante la simulación.
    - magnetizaciones: Lista de magnetizaciones registradas.
    - beta: Inverso de la temperatura (1/T).

    Retorna:
    - Cv: Calor específico.
    - chi: Susceptibilidad magnética.
    """
    energias = np.array(energias)
    magnetizaciones = np.array(magnetizaciones)

    # Valores medios y cuadrados
    E_mean = np.mean(energias)
    E2_mean = np.mean(energias**2)
    M_mean = np.mean(magnetizaciones)
    M2_mean = np.mean(magnetizaciones**2)

    # Calor específico y susceptibilidad
    Cv = (beta**2 / L**2) * (E2_mean - E_mean**2)
    chi = (beta / L**2) * (M2_mean - M_mean**2)


    return Cv, chi

# --------------------------
# Configuración y ejecución
# --------------------------
L = 10
J = 1
H = 0
pasos = 150  # Incrementar pasos de simulación
#temperaturas = np.linspace(1.5, 3.0, 40)  # 40 temperaturas entre 1.5 y 3.0

temperaturas=[0.1, 3, 100]

# Resultados
resultados = {}
Cv_list = []
chi_list = []

print("Simulando el modelo de Ising...")
for T in temperaturas:
    print(f"Simulando para T = {T}...")
    energias, magnetizaciones = simular_ising(L, T, pasos, J, H, modo='frio')
    beta = 1 / T
    Cv, chi = calcular_cv_y_chi(energias, magnetizaciones, beta)
    Cv_list.append(Cv)
    chi_list.append(chi)
    resultados[T] = {'energias': energias, 'magnetizaciones': magnetizaciones, 'Cv': Cv, 'chi': chi}

# --------------------------
# Hallar máximos de Cv y chi
# --------------------------
Cv_max = np.max(Cv_list)
Tc_Cv = temperaturas[np.argmax(Cv_list)]  # Temperatura donde Cv es máximo

chi_max = np.max(chi_list)
Tc_chi = temperaturas[np.argmax(chi_list)]  # Temperatura donde chi es máximo

print(f"\nResultados:")
print(f"Tc (a partir de Cv): {Tc_Cv}, Cv máximo: {Cv_max}")
print(f"Tc (a partir de Chi): {Tc_chi}, Chi máximo: {chi_max}")

# --------------------------
# Graficar resultados
# --------------------------
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

# Calor específico
plt.subplot(1, 2, 1)
plt.plot(temperaturas, Cv_list, 'o-', label="Calor específico ($C_v$)")
plt.axvline(Tc_Cv, color='r', linestyle='--', label=f"$T_c (C_v)$ = {Tc_Cv:.2f}")
plt.xlabel("Temperatura ($T$)")
plt.ylabel("$C_v$")
plt.title("Calor específico")
plt.legend()

# Susceptibilidad magnética
plt.subplot(1, 2, 2)
plt.plot(temperaturas, chi_list, 'o-', label="Susceptibilidad ($\chi$)")
plt.axvline(Tc_chi, color='r', linestyle='--', label=f"$T_c (\chi)$ = {Tc_chi:.2f}")
plt.xlabel("Temperatura ($T$)")
plt.ylabel("$\chi$")
plt.title("Susceptibilidad magnética")
plt.legend()

plt.tight_layout()
plt.show()

# --------------------------
# Gráficas conjuntas
# --------------------------
plt.figure(figsize=(16, 6))

# Energías
plt.subplot(1, 2, 1)
for T in temperaturas:
    plt.plot(resultados[T]['energias'], label=f'T = {T}', alpha=0.5)
plt.xlabel('Pasos de Metropolis')
plt.ylabel('Energía')
plt.title('Evolución de la energía')
plt.legend()

# Magnetizaciones
plt.subplot(1, 2, 2)
for T in temperaturas:
    plt.plot(resultados[T]['magnetizaciones'], label=f'T = {T}', alpha=0.5)
plt.xlabel('Pasos de Metropolis')
plt.ylabel('Magnetización')
plt.title('Evolución de la magnetización')
plt.legend()

plt.tight_layout()
plt.show()

# --------------------------
# Mostrar resultados finales
# --------------------------
print("\nResultados finales:")
for T in temperaturas:
    print(f"T = {T}: Cv = {resultados[T]['Cv']:.4f}, Chi = {resultados[T]['chi']:.4f}")

from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -------------------------------
# Función para calcular Cv para un tamaño de red L
# -------------------------------
def calcular_cv_por_L(L):
    Cv_list = []
    temperaturas = np.linspace(2.0, 2.5, 50)  # Cerca de Tc
    for T in temperaturas:
        energias, _ = simular_ising(L, T, pasos, J, H, modo='frio')
        beta = 1 / T
        Cv, _ = calcular_cv_y_chi(energias, [], beta)
        Cv_list.append(Cv)
    
    # Máximo de Cv
    Cv_max = np.max(Cv_list)
    return np.log(L), Cv_max

# -------------------------------
# Configuración y paralelización
# -------------------------------
tamaños_L = range(10, 31, 2)  # Tamaños de red

print("Calculando máximos de Cv para diferentes tamaños de red...")

if __name__ == "__main__":
    with Pool() as pool:
        resultados = pool.map(calcular_cv_por_L, tamaños_L)

    # Separar resultados en Ln(L) y Cv_max
    Ln_L, Cv_max_list = zip(*resultados)

    # Graficar ln(Cv_max) vs ln(L)
    plt.figure(figsize=(8, 6))
    plt.plot(Ln_L, np.log(Cv_max_list), 'o-', label=r'$\ln(C_v^{\text{max}})$')
    plt.xlabel(r'$\ln(L)$')
    plt.ylabel(r'$\ln(C_v^{\text{max}})$')
    plt.title('Dependencia del calor específico con el tamaño de la red')
    plt.legend()
    plt.grid(True)
    plt.show()