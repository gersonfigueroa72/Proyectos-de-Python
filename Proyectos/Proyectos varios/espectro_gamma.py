import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks


# Cargar datos
df = pd.read_csv('C:\\Users\\Fam. Figueroa\\Downloads\\Eu-152_15min_NaI-Tl_bicron900V.csv', 
                 header=None, #Se asume que no hay encabezados
                 names=['Canal' , 'Conteos'])

df1 = pd.read_csv('C:\\Users\\Fam. Figueroa\\Downloads\\Cs-137_15min_NaI-Tl_bicron_900V.csv', 
                  header = None, names=['Canal' , 'Conteos'])

#Iniciaremos hallando los maximos 
# Detectar picos en el espectro de Eu-152
# Puedes ajustar height y distance según tu espectro
picos_idx, _ = find_peaks(df['Conteos'], 
                          height=df['Conteos'].max() * 0.006, distance=50)

# Extraer canales y conteos correspondientes
canales_pico = df['Canal'].iloc[picos_idx].values
conteos_pico = df['Conteos'].iloc[picos_idx].values

# Imprimir resultados
print("Canales donde hay máximos:")
print(canales_pico)

print("\nConteos en esos canales:")
print(conteos_pico)

# Mostrar tabla combinada
tabla_picos = pd.DataFrame({
    'Canal': canales_pico,
    'Conteos': conteos_pico
})
print("\nTabla de picos detectados:")
print(tabla_picos)

import matplotlib.pyplot as plt

# Gráfico del espectro con 
plt.style.use('bmh')
plt.figure(figsize=(10, 5))
plt.plot(df['Canal'], df['Conteos'], 
         label='Espectro Eu-152', color='navy')

# Marcar los picos detectados
plt.scatter(canales_pico, conteos_pico, color='red', 
            marker='x', s=100, label='Picos detectados')

# Etiquetar cada pico con su canal
for canal, conteo in zip(canales_pico, conteos_pico):
    plt.annotate(f'{canal}', xy=(canal, conteo), xytext=(0, 10), 
                 textcoords='offset points', ha='center', fontsize=9, color='red')

# Opcional: escala logarítmica para mejor visualización
#print(plt.style.available)
plt.yscale('log')
plt.xlabel('Canal')
plt.ylabel('Conteos (log)')
plt.title('Espectro de $^{152}$Eu con picos detectados')
plt.legend()
#plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

#Ahora almacenamos los maximos hallados con su respectiva energía 

maximos_canal = [78,148,207,450,564,637,802]
maximos_energia_teo = [122,245,344,779,964,1112,1408]

# Realizar el ajuste lineal
coef = np.polyfit(maximos_canal, maximos_energia_teo, 1)
m, b = coef  # m es la pendiente, b es el intercepto

# Crear puntos para la línea de ajuste
x_ajuste = np.array([min(maximos_canal), max(maximos_canal)])
y_ajuste = m * x_ajuste + b

maximos_energia = []
for i in maximos_canal:
    ener = m*i+b
    ener = round(ener,2)
    maximos_energia.append(ener)

# Graficar los datos y el ajuste
plt.figure(figsize=(10, 6))
plt.scatter(maximos_canal, maximos_energia_teo, color='blue', 
           label='Datos experimentales', s=100)
plt.plot(x_ajuste, y_ajuste, 'r-', 
         label=f'Ajuste: E = {m:.2f}C + {b:.2f}')

# Personalizar la gráfica
plt.xlabel('Canal')
plt.ylabel('Energía (keV)')
plt.title('Calibración en energía del detector NaI(Tl)')
plt.grid(True)
plt.legend()
plt.show()

# Imprimir los resultados del ajuste
print(f"Pendiente (m): {m:.4f} keV/canal")
print(f"Intercepto (b): {b:.4f} keV")
print(f"Ecuación de calibración: E = ({m:.4f})C + ({b:.4f})")

#Con esto ya podemos crear la grafica de energía vs conteos

energia = []
for i in df['Canal']:
    energ = m*i+b
    energia.append(energ)

# Crear la gráfica del espectro en energía
plt.figure(figsize=(12, 6))
plt.plot(energia, df['Conteos'], label='Espectro Eu-152', color='navy')

# Encontrar los índices más cercanos a las energías máximas
indices_maximos = []
for e in maximos_energia:
    # Encuentra el índice del valor más cercano en el array energia
    idx = np.abs(np.array(energia) - e).argmin()
    indices_maximos.append(idx)

# Marcar los picos y agregar etiquetas
plt.scatter([energia[i] for i in indices_maximos], 
           [df['Conteos'][i] for i in indices_maximos], 
           color='red', marker='x', s=100, label='Picos detectados')

# Agregar etiquetas a cada pico
for e, i in zip(maximos_energia, indices_maximos):
    plt.annotate(f'{e} keV', 
                xy=(energia[i], df['Conteos'][i]), 
                xytext=(0, 10),
                textcoords='offset points',
                ha='center',
                fontsize=9,
                color='red')
#plt.style.use('default')
plt.title('ESPECTRO DE ENERGÍA DEL $^{152}$Eu')
plt.xlabel('Energía (keV)')
plt.ylabel('Conteos')
plt.yscale('log')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

#Graficamos ahora el expectro del Cs

energia_cs = []
for i in df1['Canal']:
    energ = m*i+b
    energia_cs.append(energ)

# --------- Detectar picos en el espectro de Cs-137 ---------
picos_cs_idx, _ = find_peaks(df1['Conteos'], 
                             height=df1['Conteos'].max() * 0.2, distance=50)

# Extraer canales y conteos correspondientes
canales_pico_cs = df1['Canal'].iloc[picos_cs_idx].values
conteos_pico_cs = df1['Conteos'].iloc[picos_cs_idx].values

# Calcular energías calibradas correspondientes a esos canales
energias_pico_cs = m * canales_pico_cs + b

# --------- Graficar el espectro con los picos detectados ---------
plt.figure(figsize=(12, 6))
plt.plot(energia_cs, df1['Conteos'], label='Espectro $^{137}$Cs', color='darkgreen')
#plt.yscale('log')

# Marcar los picos detectados
plt.scatter(energias_pico_cs, conteos_pico_cs, color='red', marker='x', s=100, label='Picos detectados')

# Etiquetar los picos con su energía calibrada
for energia, conteo in zip(energias_pico_cs, conteos_pico_cs):
    plt.annotate(f'{energia:.1f} keV', 
                 xy=(energia, conteo), 
                 xytext=(0, 10), 
                 textcoords='offset points', 
                 ha='center', fontsize=9, color='red', rotation = 45)

plt.title('ESPECTRO DE ENERGÍA DEL $^{137}$Cs')
plt.xlabel('Energía (keV)')
plt.ylabel('Conteos (log)')
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()

'''if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\datos.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        df.to_excel(writer, sheet_name='EU', index=False)
        df1.to_excel(writer, sheet_name='CS', index=False)'''