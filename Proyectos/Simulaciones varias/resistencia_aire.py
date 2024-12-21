'''
Con el método de Euler vamos a resolver el problema de un ciclista moviendose a una velocidad v, el cual experimenta 
resistencia del aire. Teoricamente planteamos la edo y solo nos quedaría plantear el código
'''
import matplotlib.pyplot as plt

def euler(dt,vtot,C,rho,A,m,P,v0):
    velocidades=[]
    tiempos=[]
    v=v0
    t=0
    for i in range(vtot):
        velocidades.append(v)
        tiempos.append(t)
        v=v+(P/(m*v)-C*rho*A*v**2/m)*dt
        t+=dt
    return velocidades, tiempos
#Definimos valores:
v0=1
vtot=200
dt=0.01
C=1
rho=1
A=1
m=1
P=100

# Ejecutar la función euler
velocidades, tiempos = euler(dt, vtot, C, rho, A, m, P, v0)

# Graficar los resultados
plt.plot(tiempos, velocidades)
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Cambio de velocidad con el tiempo usando el método de Euler')
plt.grid(True)
plt.show()