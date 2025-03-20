import numpy as np
import pandas as pd
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo Excel
file_path = "C:\\Users\\Fam. Figueroa\\Desktop\\rutherford.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name="Hoja1")

# Excluir la columna "0 grados" (porque en el modelo I=0 para theta=0)
columns_to_use = [col for col in df.columns if col != "0 grados"]
df_subset = df[columns_to_use]

# Calcular la intensidad promedio para cada ángulo
promedios = df_subset.mean().values

# Extraer los ángulos a partir de los nombres de las columnas (suponiendo formato "15 grados", etc.)
angulos = np.array([int(col.split()[0]) for col in columns_to_use])
print("Ángulos (°):", angulos)
print("Intensidades promedio:", promedios)

# Convertir los ángulos a radianes y calcular sin(theta/2)
theta_rad = np.radians(angulos)
sin_theta_half = np.sin(theta_rad / 2)

# Definir el modelo: I = k * sin(theta/2)^n
def modelo(x, k, n):
    return k * x**n

# Ajustar el modelo usando curve_fit, usando valores iniciales razonables
params, covariance = opt.curve_fit(modelo, sin_theta_half, promedios, p0=[max(promedios), 2])
k_fit, n_fit = params

print("\nResultados del ajuste:")
print("k =", k_fit)
print("n =", n_fit)

# Generar la curva de ajuste
x_fit = np.linspace(min(sin_theta_half), max(sin_theta_half), 100)
y_fit = modelo(x_fit, k_fit, n_fit)

# Graficar los datos y la curva ajustada
plt.figure(figsize=(8,6))
plt.scatter(sin_theta_half, promedios, color='blue', label='Datos experimentales')
plt.plot(x_fit, y_fit, color='red', label=f'Ajuste: I = {k_fit:.2e} sin^({n_fit:.2f})(θ/2)')
plt.xlabel(r'$\sin(\theta/2)$')
plt.ylabel('Intensidad Promedio')
plt.title(r'Ajuste del modelo $I = k\,\sin^n(\theta/2)$ (sin 0°)')
plt.legend()
plt.grid(True)
plt.show()

#CALCULAMOS LA COTA SUPERIOR

# Parámetros
Z1 = 2
Z2 = 79
e = 1.602e-19         # C
eps0 = 8.854e-12      # F/m
E = 5.5e6 * 1.602e-19  # J, convertimos 5.5 MeV a Joules

# Definir el prefactor que aparece en b(θ)
prefactor = (Z1 * Z2 * e**2) / (4 * np.pi * eps0) * (1 / (2 * E))

# Definir un rango de ángulos en grados (evitando 0° y 180° para evitar singularidades)
theta_deg = np.linspace(1, 179, 10000)
theta_rad = np.radians(theta_deg)

# Calcular el parámetro de impacto b(θ)
b = prefactor * np.sqrt((1 + np.cos(theta_rad)) / (1 - np.cos(theta_rad)))

# Calcular r(θ)
r = b * np.cos(theta_rad / 2) / (1 - np.sin(theta_rad / 2))

# Encontrar el valor mínimo de r en el rango considerado
min_index = np.argmin(r)
theta_min = theta_deg[min_index]
r_min = r[min_index]

print("El ángulo que minimiza r es aproximadamente:", theta_min, "grados")
print("La cota superior mínima para el radio nuclear es aproximadamente:", r_min, "m")

# Graficar r(θ) vs sin(θ/2)
plt.figure(figsize=(8,6))
plt.plot(np.sin(theta_rad/2), r, label=r"$r(\theta)$")
plt.scatter(np.sin(theta_rad/2)[min_index], r_min, color='red', zorder=5, 
            label=f"$r_{{min}} \\approx {r_min:.2e}$ m\n($\\theta \\approx {theta_min:.1f}^\\circ$)")
plt.xlabel(r"$\sin(\theta/2)$")
plt.ylabel(r"$r(\theta)$ (m)")
plt.title(r"Cota Superior del Radio Nuclear $r(\theta)$")
plt.legend()
plt.grid(True)
plt.show()