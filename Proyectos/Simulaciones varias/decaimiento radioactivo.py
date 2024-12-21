'''
Vamos a calcular de forma númerica el decaimiento radioactivo para el Uranio 235

Empezaremos la función Euler, que se encargará de iterar los pasos de nuestro método
'''

def Euler(N0,tau,dt,Ntot):
    n=N0
    t=0
    N=[]
    T=[]
    for i in range(Ntot):
        N.append(n)
        T.append(t)
        n=n-n/tau*dt
        t=t+dt
    return N,T

N0 = 100
tau = 1
dt = 0.01
Ntot = 1000

sol = Euler(N0,tau,dt,Ntot) #Invocar la función para la solución de la ecuación diferencial
T = sol[1] #acá estamos diciendo que en la lista T que ya declaramos, guarde la salida 1 de la funcion sol
N = sol[0] #Variable de cantidad de partículas

print(N)
print(T)

import matplotlib.pyplot as plt

plt.plot(T,N)
plt.xlabel('Tiempo')
plt.ylabel('Cantidad de partículas')
plt.show()