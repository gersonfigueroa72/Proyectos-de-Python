import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, b):
    """Función lineal para el ajuste."""
    return m * x + b

# Solicitar al usuario la ruta del archivo Excel
ruta_excel = 'C:\\Users\\Fam. Figueroa\\Desktop\\plank1.xlsx'

try:
    # Lee el archivo Excel.
    # Ajusta sheet_name si tus datos están en otra hoja.
    datos = pd.read_excel(ruta_excel, sheet_name=4)
    
    # Convertir columnas a tipo numérico y manejar errores
    datos['V1']  = pd.to_numeric(datos['V1'],  errors='coerce')
    datos['SV1'] = pd.to_numeric(datos['SV1'], errors='coerce')
    datos['V2']  = pd.to_numeric(datos['V2'],  errors='coerce')
    datos['SV2'] = pd.to_numeric(datos['SV2'], errors='coerce')
    
    # Eliminar filas con NaN
    datos = datos.dropna()
    if len(datos) == 0:
        raise ValueError("No hay datos válidos después de eliminar NaN.")
    
except Exception as e:
    print(f"Error al leer o procesar el archivo: {e}")
    exit()

# Extraer los datos en arrays de NumPy
V1  = datos['V1'].values
SV1 = np.abs(datos['SV1'].values)  # incertidumbre en V1 (tomamos valor absoluto)
V2  = datos['V2'].values
SV2 = np.abs(datos['SV2'].values)  # incertidumbre en V2 (valor absoluto)

# ------------------------------------------------------------------
# 1. ORDENAR LOS DATOS POR VOLTAJE
# ------------------------------------------------------------------
idx_sorted = np.argsort(V1)
V1_sorted  = V1[idx_sorted]
SV1_sorted = SV1[idx_sorted]
V2_sorted  = V2[idx_sorted]
SV2_sorted = SV2[idx_sorted]

# ------------------------------------------------------------------
# 2. DEFINIR MANUALMENTE UN PUNTO DE CORTE PARA SEPARAR LAS REGIONES
#    PRE-FRENADO Y POST-FRENADO
# ------------------------------------------------------------------
# Ajusta este valor según la forma de tus datos (puedes mirar la gráfica).
cutoff_voltage = -1.1  # Ejemplo: a partir de -0.5 V, consideramos la región post-frenado

mask_pre  = (V1_sorted <= cutoff_voltage)
mask_post = (V1_sorted >  cutoff_voltage)

V1_pre  = V1_sorted[mask_pre]
V2_pre  = V2_sorted[mask_pre]
SV1_pre = SV1_sorted[mask_pre]
SV2_pre = SV2_sorted[mask_pre]

V1_post  = V1_sorted[mask_post]
V2_post  = V2_sorted[mask_post]
SV1_post = SV1_sorted[mask_post]
SV2_post = SV2_sorted[mask_post]

# ------------------------------------------------------------------
# 3. REALIZAR LOS AJUSTES LINEALES EN CADA REGIÓN
# ------------------------------------------------------------------
try:
    # Ajuste región pre-frenado
    params_pre, cov_pre = curve_fit(linear, V1_pre, V2_pre)
    m1, b1 = params_pre
    
    # Ajuste región post-frenado
    params_post, cov_post = curve_fit(linear, V1_post, V2_post)
    m2, b2 = params_post
    
    # Desviaciones estándar de los parámetros (m1, b1) y (m2, b2)
    sigma_m1, sigma_b1 = np.sqrt(np.diag(cov_pre))
    sigma_m2, sigma_b2 = np.sqrt(np.diag(cov_post))
    
except Exception as e:
    print(f"Error en el ajuste lineal: {e}")
    exit()

# ------------------------------------------------------------------
# 4. GRAFICAR LOS DATOS + BARRAS DE ERROR + RECTAS AJUSTADAS
# ------------------------------------------------------------------
plt.figure(figsize=(8, 4))

# Graficar los datos experimentales con barras de error
plt.errorbar(V1_sorted, V2_sorted,
             xerr=SV1_sorted, yerr=SV2_sorted,
             fmt='o', color='blue', ecolor='lightgray',
             capsize=3, label='Datos experimentales')

plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (A)')
plt.title('Corriente vs Voltaje (Color UV)')
plt.axhline(0, color='gray', linestyle='--')
plt.grid(True)

# Crear un rango de voltaje para dibujar las rectas ajustadas
V_fit = np.linspace(min(V1_sorted), max(V1_sorted), 300)
V2_fit_pre  = linear(V_fit, m1, b1)
V2_fit_post = linear(V_fit, m2, b2)

# Graficar las rectas
plt.plot(V_fit, V2_fit_pre,  '--', color='red',   label='Ajuste región pre-frenado')
plt.plot(V_fit, V2_fit_post, '--', color='green', label='Ajuste región post-frenado')

# ------------------------------------------------------------------
# 5. ENCONTRAR LA INTERSECCIÓN DE LAS DOS RECTAS (POTENCIAL DE FRENADO)
#    m1*x + b1 = m2*x + b2  =>  x = (b2 - b1) / (m1 - m2)
# ------------------------------------------------------------------
if np.isclose(m1, m2, atol=1e-12):
    print('Las rectas son prácticamente paralelas. No se puede determinar la intersección.')
    plt.legend()
    plt.show()
    exit()

V_f = (b2 - b1) / (m1 - m2)

# ------------------------------------------------------------------
# 6. CALCULAR LA INCERTIDUMBRE EN V_f MEDIANTE PROPAGACIÓN DE ERRORES
# ------------------------------------------------------------------
# Fórmula aproximada:
#   SV_f^2 = (∂V_f/∂m1)^2 * σ_m1^2 + (∂V_f/∂b1)^2 * σ_b1^2
#          + (∂V_f/∂m2)^2 * σ_m2^2 + (∂V_f/∂b2)^2 * σ_b2^2
#   donde V_f = (b2 - b1) / (m1 - m2)
#
#   ∂V_f/∂b1 = -1 / (m1 - m2)
#   ∂V_f/∂b2 =  1 / (m1 - m2)
#   ∂V_f/∂m1 = - (b2 - b1) / (m1 - m2)^2
#   ∂V_f/∂m2 =   (b2 - b1) / (m1 - m2)^2

dVf_db1 = -1.0 / (m1 - m2)
dVf_db2 =  1.0 / (m1 - m2)
dVf_dm1 = -(b2 - b1) / (m1 - m2)**2
dVf_dm2 =  (b2 - b1) / (m1 - m2)**2

SV_f = np.sqrt( (dVf_dm1**2)*(sigma_m1**2) +
                (dVf_dm2**2)*(sigma_m2**2) +
                (dVf_db1**2)*(sigma_b1**2) +
                (dVf_db2**2)*(sigma_b2**2) )

# Mostrar la línea vertical en la gráfica con el potencial de frenado
plt.axvline(V_f, color='purple', linestyle='--',
            label=f'Potencial de frenado: {V_f:.3f} V\nIncertidumbre: ±{SV_f:.3f} V')

# Mostrar valores en consola
print(f'Potencial de frenado (V_f): {V_f:.3f} V')
print(f'Incertidumbre en V_f: ±{SV_f:.3f} V')

plt.legend()
plt.show()
