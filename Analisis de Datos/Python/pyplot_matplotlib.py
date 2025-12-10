import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#pyplot es elmodulo usado para graficar estilo MATLAB

# Cargar datos
df = pd.read_csv('C:\\Users\\Fam. Figueroa\\Downloads\\Eu-152_15min_NaI-Tl_bicron900V.csv', 
                 header=None, #Se asume que no hay encabezados
                 names=['Canal' , 'Conteos'])

print(df.columns)

#Iniciamos haciendo la grafica mas básica
plt.plot(df['Canal'], df['Conteos'])
plt.title('Espectro de rayos gamma de la fuente 152EU')
plt.ylabel('No. de conteos')
plt.xlabel('Canales')
plt.show()

#Supongamos que tenemos ahora nuevos datos y queremos graficarlos juntos 
#esto lo hacemos simplemente agregando un plt.plot mas:

df1 = pd.read_csv('C:\\Users\\Fam. Figueroa\\Downloads\\Cs-137_15min_NaI-Tl_bicron_900V.csv', 
                  header = None, names=['Canal' , 'Conteos'])

#Ploteamos ambas graficas
plt.plot(df['Canal'], df['Conteos'])
plt.plot(df1['Canal'], df1['Conteos'])
#Podemos agregar leyendas sobre que grafica representa cada una
plt.legend(['152Eu', '137Cs']) #Aca el orden es importante, porque la primera
#leyenda de la lista representa la primer grafica que agregamos y el segundo
#la segunda grafica agregada...
plt.title('Espectro de rayos Gamma')
plt.ylabel('No. de conteos')
plt.xlabel('Canales')
plt.show()

#Si no sabemos la forma en la que fueron agregadas las graficas, tambien podemos
#agregar leyendas, directamente de la construccion de la gráfica

#Ploteamos ambas graficas
plt.plot(df['Canal'], df['Conteos'], label = '152Eu')
plt.plot(df1['Canal'], df1['Conteos'], label = '137Cs')
plt.title('Espectro de rayos Gamma')
plt.ylabel('No. de conteos')
plt.xlabel('Canales')
plt.legend() #igual hay que ponerlo para que aparezcan las leyendas
plt.show()

#Haremos ahora una grafica cambiando color, estilo, grosor y marcadores
plt.plot(df1['Canal'], df1['Conteos'],
         color = 'red', #Color de la grafica, se puede usar RBG '#000FF00'
         linestyle = '--', #Estilo de la grafica
         linewidth = 2, #Grosor de la grafica
         marker = 'o', #Marcador de los puntos
         markersize = 1, label = '137Cs') #Tamaño del marcador
plt.legend()
plt.grid() #Agrega una cuadrícula a la gráfica
plt.show()

#Tambien podemos cambiar el estilo de la gráfica, los estilos disponibles son:
print(plt.style.available) #Muestra los estilos disponibles

#Usaremos el de ggplot
plt.style.use('ggplot') 
#cambio de estilo, el estilo afecta a todas las graficas siguientes
plt.plot(df['Canal'], df['Conteos'])
plt.title('Espectro de rayos gamma de la fuente 152EU')
plt.ylabel('No. de conteos')
plt.xlabel('Canales')
plt.show()

#Regresamos al estilo por defecto
plt.style.use('default')

#Podemos usar un estilo de comic usando plt.xkcd()

#Podemos guardar la grafica
plt.savefig('Espectro_152Eu.png', dpi=300) #dpi es la calidad de la imagen
#guarda la figura en el directorio actual, si no se especifica la ruta