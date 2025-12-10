import matplotlib.pyplot as plt
import pandas as pd
# Datos de la tabla
medias = [84, 91, 93, 96, 98, 100, 102, 103, 105, 107, 108, 110, 112]
frecuencias = [1, 2, 2, 2, 3, 2, 1, 2, 4, 2, 1, 2, 1]
# Configurar el gráfico
plt.figure(figsize=(12, 6))
plt.bar(medias, frecuencias, width=3, edgecolor="black", align="center")

# Personalización
plt.title("Distribución de Medias Muestrales", fontsize=14)
plt.xlabel("Media Muestral", fontsize=12)
plt.ylabel("Frecuencia", fontsize=12)
plt.xticks(medias, rotation=45)  # Mostrar todas las medias en el eje X
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

