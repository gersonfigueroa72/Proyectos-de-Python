'''
Calculo del Perihelio de Mercurio.
'''
# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Constantes físicas
G = 4 * np.pi**2  # Constante gravitacional en UA^3 / (yr^2 * Ms)
Ms = 1.0  # Masa del Sol en masas solares
alpha = 0.002  # Efecto relativista (UA^2)
a = 0.39  # Semieje mayor de la órbita de Mercurio (UA)
e = 0.206  # Excentricidad de la órbita de Mercurio
N = 20000  # Número de pasos
dt = 0.0001  # Paso de tiempo en años

# Condiciones iniciales
x0 = a * (1 + e)  # Aphelio
y0 = 0.0
vx0 = 0.0
vy0 = np.sqrt(G * Ms * (1 - e) / (a * (1 + e)))

# Definimos la fuerza gravitacional con el término relativista
def fuerza(x, y):
    r = np.sqrt(x**2 + y**2)
    F = -G * Ms / r**2 * (1 + alpha / r**2)
    Fx = F * (x / r)
    Fy = F * (y / r)
    return Fx, Fy

# Definimos la función para calcular dr/dt
def calcular_dr_dt(x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)  # Distancia al Sol
    dr_dt = (x * vx + y * vy) / r  # Derivada dr/dt
    return dr_dt

# Método de Runge-Kutta de 2º orden (RK2)
def runge_kutta_2(N, dt, x0, y0, vx0, vy0):
    # Inicializamos las listas para almacenar la posición, velocidad, ángulo y dr/dt
    x = np.zeros(N)
    y = np.zeros(N)
    vx = np.zeros(N)
    vy = np.zeros(N)
    theta = np.zeros(N)
    dr_dt_list = np.zeros(N)
    dtheta_dt = np.zeros(N-1)  # Derivada de theta_p
    theta_p = np.zeros(N-1)  # Angulo theta_p
    dtheta_p_dt = np.zeros(N-2)  # Derivada temporal de theta_p

    # Condiciones iniciales
    x[0] = x0
    y[0] = y0
    vx[0] = vx0
    vy[0] = vy0

    # Loop del método RK2
    for i in range(N - 1):
        # Evaluamos la aceleración (fuerza) en el punto actual
        Fx1, Fy1 = fuerza(x[i], y[i])

        # Predicción de la velocidad intermedia
        vx_half = vx[i] + Fx1 * dt / 2
        vy_half = vy[i] + Fy1 * dt / 2

        # Predicción de la posición intermedia
        x_half = x[i] + vx[i] * dt / 2
        y_half = y[i] + vy[i] * dt / 2

        # Evaluamos la fuerza en la posición intermedia
        Fx2, Fy2 = fuerza(x_half, y_half)

        # Actualizamos las velocidades y posiciones con el segundo paso
        vx[i+1] = vx[i] + Fx2 * dt
        vy[i+1] = vy[i] + Fy2 * dt
        x[i+1] = x[i] + vx_half * dt
        y[i+1] = y[i] + vy_half * dt

        # Calcular el ángulo theta en este paso
        theta[i] = np.mod(np.degrees(np.arctan2(y[i], x[i])), 360)  # Convertimos a grados

        # Calcular la derivada dr/dt en este paso
        dr_dt_list[i] = calcular_dr_dt(x[i], y[i], vx[i], vy[i])


    return x, y, theta, dr_dt_list, dtheta_dt

# Ejecutamos el método
x, y, theta, dr_dt_list, dtheta_dt = runge_kutta_2(N, dt, x0, y0, vx0, vy0)

'''
Calculamos la orbita de Mercurio
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import matplotlib.cm as cm

# Calculamos el número de vueltas de Mercurio alrededor del Sol
num_orbitas = 8  # Por ejemplo, 5 órbitas

# Creamos una gráfica
plt.figure(figsize=(7, 4))

# Dibujamos las órbitas de Mercurio con diferentes colores
for i in range(num_orbitas):
    inicio = i * N // num_orbitas
    fin = (i + 1) * N // num_orbitas
    cmap = cm.get_cmap('viridis')
    plt.plot(x[inicio:fin], y[inicio:fin], label=f"Órbita {i+1}", color=cmap(i / num_orbitas), linewidth=0.3)

# Representamos al Sol como un punto grande en el centro
plt.scatter(0, 0, color="orange", label="Sol", s=250)

# Representamos a Mercurio en su posición final como un punto rojo
plt.scatter(x[-1], y[-1], color="red", label="Mercurio", s=10)

# Encontramos los puntos donde ocurre el perihelio
r = np.sqrt(x**2 + y**2)  # Distancia de Mercurio al Sol en cada punto
perihelio_indices, _ = find_peaks(-r)  # Mínimos locales en la distancia

# Graficamos los puntos del perihelio
plt.scatter(x[perihelio_indices], y[perihelio_indices], color="blue", label="Perihelio", s=3)

# Añadimos etiquetas, leyenda y formato de la gráfica
plt.xlabel("x (UA)")
plt.ylabel("y (UA)")
plt.title("Órbita de Mercurio con Precesión del Perihelio (colores por órbita)")
plt.legend()
plt.grid(True)
plt.axis("equal")

#plt.xlim([-0.4, 0.05])
#plt.ylim([-0.1, 0.1])

# Mostramos la gráfica
plt.show()

'''
Calculamos la precesión del perihelio de Mercurio
'''

import numpy as np
from scipy.signal import find_peaks

# Calcular los ángulos de los perihelio con respecto al Sol
def calcular_angulos_perihelio(x, y, perihelio_indices):
    angulos_perihelio = []
    for i in perihelio_indices:
        angulo = np.mod(np.degrees(np.arctan2(y[i], x[i])), 360)  # Convertir a grados
        angulos_perihelio.append(angulo)
    return np.array(angulos_perihelio)

# Calcular la diferencia de ángulos entre perihelio consecutivos (en valor absoluto)
def calcular_diferencias_angulares(angulos_perihelio):
    diferencias_angulares = np.diff(angulos_perihelio)  # Diferencia entre ángulos consecutivos
    # Asegurarse de que las diferencias estén dentro del rango [-180, 180] para evitar saltos grandes
    diferencias_angulares = np.mod(diferencias_angulares + 180, 360) - 180
    return np.abs(diferencias_angulares)  # Tomar el valor absoluto de las diferencias

# Calcular la media de las diferencias angulares
def calcular_media_diferencias(diferencias_angulares):
    return np.mean(diferencias_angulares)

# Calcular el tiempo entre perihelio consecutivos
def calcular_tiempos_entre_perihelio(tiempos, perihelio_indices):
    tiempos_entre_perihelio = np.diff(tiempos[perihelio_indices])  # Diferencia entre tiempos de perihelio consecutivos
    return tiempos_entre_perihelio

# Calcular la media del tiempo entre perihelio
def calcular_media_tiempo(tiempos_entre_perihelio):
    return np.mean(tiempos_entre_perihelio)

tiempo = np.arange(N) * dt  # Tiempo en años

# Encontrar los puntos del perihelio (mínimos locales de r)
r = np.sqrt(x**2 + y**2)  # Distancia de Mercurio al Sol en cada punto
perihelio_indices, _ = find_peaks(-r)  # Mínimos locales en la distancia

# Calcular los ángulos de los puntos del perihelio
angulos_perihelio = calcular_angulos_perihelio(x, y, perihelio_indices)

# Calcular las diferencias de ángulos entre perihelio consecutivos (en valor absoluto)
diferencias_angulares = calcular_diferencias_angulares(angulos_perihelio)

# Calcular la media de las diferencias angulares
media_diferencias = calcular_media_diferencias(diferencias_angulares)

# Mostrar los resultados de las diferencias angulares
for i, dif_angulo in enumerate(diferencias_angulares):
    print(f"Diferencia de ángulo entre el perihelio {i+1} y el perihelio {i+2}: {dif_angulo:.2f} grados")

print(f"\nPromedio de las diferencias de ángulo: {media_diferencias:.2f} grados")

# Calcular los tiempos entre perihelio consecutivos
tiempos_entre_perihelio = calcular_tiempos_entre_perihelio(tiempo, perihelio_indices)

# Calcular la media del tiempo entre perihelio
media_tiempo_perihelio = calcular_media_tiempo(tiempos_entre_perihelio)

# Mostrar los resultados del tiempo entre perihelio
for i, tiempo in enumerate(tiempos_entre_perihelio):
    print(f"Tiempo entre el perihelio {i+1} y el perihelio {i+2}: {tiempo:.4f} años")

print(f"\nTiempo promedio entre los perihelio: {media_tiempo_perihelio:.4f} años")

dthetap_dt=media_diferencias/media_tiempo_perihelio
print(f"Precesión promedio de Mercurio: {dthetap_dt} grados/año")
print(f"Precesión promedio de Mercurio: {dthetap_dt*3600*100} segundos de arco/siglo" )

'''
Calculamos la derivada temporal de dr/dt
'''

tiempo = np.linspace(0, (N)*dt, N)
# Graficar dr/dt en función del tiempo
plt.figure(figsize=(8, 6))
plt.plot(tiempo[:-1], dr_dt_list[:-1], label=r'$\frac{dr}{dt}$', color="g")
plt.xlabel('Tiempo (años)')
plt.ylabel(r'$\frac{dr}{dt}$ (UA/año)')
plt.title('Tasa de Cambio de la Distancia de Mercurio al Sol')
plt.legend()
plt.grid(True)
plt.show()

#velocidad_radial=np.mean(dr_dt_list)
#print(f"Velocidad radial promedio: {velocidad_radial:.4f} UA/año")

'''
Calculamos $\theta$ en funcion del tiempo. Donde $\theta$ es el angulo entre la horizontal 
y el vector que va del sol a mercurio.
'''

# Graficar theta
plt.figure(figsize=(9, 6))
plt.plot(np.linspace(0, (N)*dt, N), theta, label=r'$\theta$', color="g")
plt.xlabel("Tiempo (años)")
plt.ylabel(r'$\theta$ (grados)')
plt.title(r'Ángulo $\theta$ en función del tiempo')
plt.grid(True)
plt.legend()
plt.show()