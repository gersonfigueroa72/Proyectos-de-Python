import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos de la tabla (I^2 en A², V en V)
I_squared = np.array([0.5476, 0.8464, 1.1449, 1.4161, 1.8225])
V = np.array([100, 149, 200, 250, 300])

# Función para el ajuste lineal: V = A * I^2 + B
def linear_model(x, A):
    return A * x

# Realizar el ajuste
params, covariance = curve_fit(linear_model, I_squared, V)
A = params[0]  # Extraer el valor escalar
A_err = np.sqrt(np.diag(covariance))[0]  # Extraer el valor escalar del error

# Crear valores para la curva de ajuste
I_squared_fit = np.linspace(min(I_squared), max(I_squared), 100)
V_fit = linear_model(I_squared_fit, A)

# Graficar datos y ajuste
plt.figure(figsize=(10, 6))
plt.scatter(I_squared, V, color='red', label='Datos experimentales', zorder=5)
plt.plot(I_squared_fit, V_fit, 'b-', label=f'Ajuste: $V = A I^2$\n$A = {A:.1f} \pm {A_err:.1f}$')

# Personalizar gráfica
plt.xlabel('$I^2$ (A²)', fontsize=12)
plt.ylabel('$V$ (V)', fontsize=12)
plt.title('Ajuste lineal de $V$ vs $I^2$ para determinar $e/m$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()

# Mostrar resultados del ajuste
print(f"Resultados del ajuste:")
print(f"A (pendiente) = {A:.1f} ± {A_err:.1f} V/A²")

plt.show()