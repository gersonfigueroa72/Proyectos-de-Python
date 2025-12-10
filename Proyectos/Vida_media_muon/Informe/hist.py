import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

df1 = pd.read_excel('tiempos_picos1.xlsx')
df2 = pd.read_excel('tiempos_picos2.xlsx')
df3 = pd.read_excel('tiempos_picos3.xlsx')
df4 = pd.read_excel('tiempos_picos4.xlsx')
df5 = pd.read_excel('tiempos_picos5.xlsx')
#Concatenamos los tres dataframes
df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

df = df[df['Tiempos entre pulsos'] > 0.68]
#df.to_excel('tiempos_picos_total.xlsx', index=False)

#Hacemos un ajuste de la curva del histograma de la forma y = N*exp(-t/tau) + c
def exp_func(x, N, tau, c):
    return N * np.exp(-x / tau) + c

# Calculamos el histograma
hist, bin_edges = np.histogram(df['Tiempos entre pulsos'], bins=50)
bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

# Estimamos parámetros iniciales más apropiados
N_init = np.max(hist)  # Altura máxima del histograma
tau_init = np.mean(df['Tiempos entre pulsos'])  # Media de los tiempos
c_init = np.min(hist)  # Valor base del histograma

# Ajustamos la curva con límites y mejores parámetros iniciales
try:
    popt, pcov = curve_fit(
        exp_func, 
        bin_centers, 
        hist, 
        p0=[N_init, tau_init, c_init],
        bounds=([0, 0, 0], [np.inf, np.inf, np.inf]),
        maxfev=10000  # Aumentamos el número máximo de iteraciones
    )
    # Calculamos las incertezas de los parámetros
    perr = np.sqrt(np.diag(pcov))

    # Calculamos el R-cuadrado para ver la calidad del ajuste
    residuals = hist - exp_func(bin_centers, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((hist - np.mean(hist))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    print(f"Parámetros del ajuste:")
    print(f"N = {popt[0]:.2f} ± {perr[0]:.2f}")
    print(f"tau = {popt[1]:.2f} ± {perr[1]:.2f} micro-segundos")
    print(f"c = {popt[2]:.2f} ± {perr[2]:.2f}")
    print(f"R² = {r_squared:.4f}")
    
    # Actualizamos la leyenda del gráfico para incluir la incerteza
    plt.figure(figsize=(10, 6))
    plt.hist(df['Tiempos entre pulsos'], bins=50, density=False, alpha=0.5, 
             color='blue', label='Datos')
    
    x = np.linspace(min(bin_centers), max(bin_centers), 1000)
    plt.plot(x, exp_func(x, *popt), 'r-', 
             label=f'Ajuste: τ = ({popt[1]:.1f} ± {perr[1]:.1f}) microsegundos')
    
    plt.xlabel('Tiempos entre pulsos (ms)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de tiempos entre pulsos con ajuste exponencial')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

except RuntimeError as e:
    print("Error en el ajuste:",str(e))