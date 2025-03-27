'''

'''
#Importamos las librerias a utilizar
import pandas as pd
import numpy as np

#Iniciamos extraendo los datos necesarios ya sea de un archivo
#csv o xlsx

formato = input('Ingrese el formato del archivo (excel o csv): ')

if formato == 'excel':
    ruta = input('Ingrese la ruta del archivo:')
    df = pd.read_excel(ruta)
    print(df)
else:
    ruta = input('Ingrese la ruta del archivo:')
    df = pd.read_csv(ruta)
    print(df)

#Iniciaremos eliminando columnas que no nos interesan

columnas = df.columns #Visualizamos el nombre de las columnas
#print(columnas)

columnas_a_eliminar = [
    'fa','f_ejecucion','prodact_id_oblig','prodact_subsegmento',
    'prodact_cod_activi_economica','prodact_activi_economica',
    'prodact_cod_segmento_sib', 'prodact_segmento_sib', 
    'prodact_cod_subsegmento_sib', 'prodact_subsegmento_sib',
    'prodact_reserva_especifica_gtq', 'prodact_reserva_especifica_usd'
]
df = df.drop(columnas_a_eliminar, axis = 1)

print(df)

#Creamos un nuevo data frame que van desde la col. 'prodact_id_oblig_sis' a 
#'prodact_lme_actual_cli_usd'

df1 = df.loc[:, 'prodact_id_oblig_sis':'prodact_lme_actual_cli_usd']

#De este nuevo data frame eliminaremos todos los datos que no sean de 
#tarjetas de credito y nos aseguramos que en la columna prodact_beg_bpp haya solo creditos 
#beg y no bpp

df1 = df1[(df1['prodact_producto'] == 'TC') & (df1['prodact_beg_bpp']=='BEG')]
#print(df1)
#print(df1.columns) #verificamos las columnas que quedaron

#Ahora crearemos un nuevo data frame, que será el resultado del informe
#Iniciaremos colocando una columna para el id del cliente (no se debe repetir)
#el id, y a la derecha colocamos su LME aprobado en USD

informe = pd.DataFrame() #Acá iremos recopilando la info. relevante

#Hacemos una lista con los id de los clientes, tal que no se repitan

id_clientes = df1['prodact_id_cli'].unique()
informe['id_cliente'] = id_clientes #agregamos esta columna al informe

#Ahora crearemos una columna con la suma del LME aprobado en USD de cada cliente


