import pandas as pd

serie1 = pd.Series([1,2,"hola",4,5])
print(serie1)

#en lugar de usar una lista, usamos un diccionario

materias = pd.Series({"mate":91,"fisica":95,"quimica":5})
print(materias)

#podemos acceder a los valores de la serie con el nombre de la clave
print(materias[["mate","fisica"]])

#podemos hacer operaciones con las series
print(materias+10)
print(materias/10)

#Algunas funciones utiles son:

serie2 = pd.Series([1,2,3,4,5])

print(serie2.sum())
print(serie2.mean())
print(serie2.median())
print(serie2.max())
print(serie2.min())
print(serie2.std()) #desviacion estandar
print(serie2.describe()) #nos da un resumen de la serie


#si queremos filtrar los datos de una serie usamos:
print(serie2[serie2>3])

#Podemos ordenar los datos de menor a mayor
print(materias.sort_values())

#Podemos ordenar los datos de mayor a menor
print(materias.sort_values(ascending=False))

#Podemos crear una serie de un solo valor usando
serie_rep = pd.Series(5, index=range(0,5)) #podemos pedir que el primer indice sea 1 tambien
print(serie_rep)

#Podemos usar asignar un indice a cada elemento de la serie
#y que el indice no nesesariamente sea un numero
serie3 = pd.Series([20,56,'palabra'], index=['a','b','c'])
print(serie3)

'''
APRENDEREMOS AHORA A UTILIZAR DATAFRAMES
'''

#Un DataFrame es una estructura de datos bidimensional, es decir, una tabla
#Podemos crear un DataFrame a partir de un diccionario

datos = {'nombre':['Gerson','Lorena','Noé','Mel','Angel'],'edad':[22,47,55,18,24],
         'puntos':[91,95,5,70,80]}
print(datos) # esto aun no es un data frame

familia = pd.DataFrame(datos) 
print(familia)

#Tambien podemos crear un data frame a partir de una lista:

df1 = pd.DataFrame([['Gerson',22,91],['Lorena',47,95],['Noé',55,5],['Mel',18,70],['Angel',24,80]],
                   columns=['nombre','edad','puntos'])

print(df1)


#Podemos crear dataframes usando arrays de numpy
import numpy as np
df2=pd.DataFrame(np.array([[1,2],[9,0],[3,8]]),columns=['a','b'])
print(df2)

'''
Ahora aprenderemos a leer archivos csv y .xlsx
'''
#Para leer un archivo csv usamos
df3 = pd.read_csv('C:\\Users\\Fam. Figueroa\\Desktop\\Gerson\\ECFM\\Programas\\Curso Phyton\\Analisis de Datos\\Python\\Mobiles Dataset (2025).csv',encoding='latin1')
print(df3)

#Si queremos seleccionar un elemento de un dataframe usamos
print(df3['Model Name'][1]) #primero se pone el nombre de la columna y luego el indice
print(df3['Model Name'][1:5]) #podemos seleccionar un rango de elementos

#Para filtrar una columna podemos usar:
filtrar=df3['Company Name']=='Samsung'

#Esto nos devuelve una serie de booleanos
#Si queremos filtrar realmente usamos:
dataframe_filtrado = df3[filtrar]
print(dataframe_filtrado)

filtrar_año = df3['Launched Year']>2020
dataframe_filtrado_año = df3[filtrar_año]
print(dataframe_filtrado_año)

'''
Algunos atributos de un dataframe son:
'''
n=3
print(df3.head(n)) #nos muestra los primeros n elementos del data frame
print(df3.tail(n)) #Nos muestra los ultimos n elementos del data 
print(df3.index) #Nos muestra los indices del data frame
print(df3.columns) #Nos muestra las columnas del data frame
print(df3.shape) #Nos muestra la forma del data frame
print(df3.dtypes) #Nos muestra los tipos de datos de las columnas

#Para leer un archivo .xlsx usamos
df4 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Gerson\\ECFM\\Programas\\Curso Phyton\\Analisis de Datos\\Python\\rutherford.xlsx')
print(df4)

'''
Ahora aprenderemos a manipular los data frames
'''
#Vimos anteriormente como seleccionar un elemento definiendo 
#la columna y el indice, ahora lo haremos especificando
#fila y columna

print(df4.iloc[3,4]) #tercera fila y cuarta col. (empiezan en 0)

#Si queremos seleccionar una fila completa usamos
print(df4.iloc[3,:])

#Si queremos seleccionar una columna completa usamos
print(df4.iloc[:,4])

#Si queremos seleccionar un rango de filas y columnas usamos
print(df4.iloc[1:4,2:5])

#Si queremos seleccionar un elemento de una columna por su nombre
print(df4.loc[3,'30 grados'])

#Podemos seleccionar una fila
print(df4.loc[5,()]) #Nos da toda la fila 5

print(df4.loc[3,['30 grados','45 grados']]) #Nos da los elementos de la fila 3 en las columnas 30 y 45 grados



'''
La diferencia entre iloc y loc es que iloc se usa para seleccionar
por indice y loc se usa para seleccionar por nombre
'''

#podemos agregar una columna a un data frame de la siguiente forma
df4['nueva columna']=pd.Series(range(1,13))
print(df4)

#podemos eliminar una columna de un data frame de la siguiente forma
df4.pop('nueva columna')
print(df4)

#podemos agregar una fila como:

df4.loc[len(df4)]=[1,2,3,4,5,6,7,8,9,10]
print(df4)

#podemos eliminar una fila de un data frame de la siguiente forma:
df4.drop()