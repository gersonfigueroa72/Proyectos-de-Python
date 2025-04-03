'''

'''
#Importamos las librerias a utilizar
import pandas as pd
import numpy as np

#Iniciamos extraendo los datos necesarios ya sea de un archivo
#csv o xlsx
#"C:\\Users\\Fam. Figueroa\\Desktop\\query-impala-17328357 original.xlsx"
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

#print(df)

#Creamos un nuevo data frame que van desde la col. 'f_analisis' a 
#'prodact_lme_actual_cli_usd'

df1 = df.loc[:, 'f_analisis':'prodact_lme_actual_cli_usd']

#De este nuevo data frame eliminaremos todos los datos que no sean de 
#tarjetas de credito y nos aseguramos que en la columna prodact_beg_bpp haya 
#solo creditos beg y no bpp

df1 = df1[(df1['prodact_producto'] == 'TC') & (df1['prodact_beg_bpp']=='BEG')]
#print(df1)
#print(df1.columns) #verificamos las columnas que quedaron

#Ahora empezamos creando una columna para el id del cliente (no se debe repetir)
#el id, y a la derecha colocamos su LME aprobado en USD

id_clientes = df1['prodact_id_cli'].unique()

#Ahora crearemos una columna con la suma del LME aprobado en USD de cada cliente

id_cli = [] 
suma_lme_aprobado = [] #Suma LME aprob * cliente
for i in id_clientes:
    id_cli.append(i)
    lme_clientes = df1[df1['prodact_id_cli']==i]
    suma=lme_clientes['prodact_lme_aprobado_cli_usd'].sum()
    suma_lme_aprobado.append(suma)

lme = pd.DataFrame()

#agregamos id_cli y suma_lme_aprobado a lme
lme['id_cliente'] = id_cli
lme['suma_lme_aprobado'] = suma_lme_aprobado
#print(lme)

#Ahora vamos a eliminar los clientes repetidos en df1 y eliminamos los datos 
#de 'prodact_lme_aprobado_cli_usd' y sustituimos por lme['suma_lme_aprobado']

df1 = df1.drop_duplicates(subset=['prodact_id_cli']).reset_index(drop=True)
df1['prodact_lme_aprobado_cli_usd'] = lme['suma_lme_aprobado']
#df1 = df1.sort_values(by='prodact_id_grupo', ascending=True)
df1['prodact_f_venc'] = df1['prodact_f_venc'].replace('NULL', 0)

#Ahora de df eliminamos todas las columnas que sean 'TC'
df = df[df['prodact_producto'] != 'TC']

#Concatenamos df1 a df
df = pd.concat([df, df1], axis=0, ignore_index=True)

'''
Ahora que terminamos TC, vamos a trabajar con las LC
'''
#Creamos un nuevo data frame que tiene los mismos datos que df pero solo de LC
lc = df[df['prodact_linea_credito'].notna()] #unicamente extramos lc

#Ahora que guardamos las LC en lc, las eliminamos de df
df = df[df['prodact_linea_credito'].isna()]

#Extraemos de prodact_linea_credito las LC que no sean repetidas
linea_credito = lc['prodact_linea_credito'].unique()

#del dataframe lc extraemos de 'prodact_dias_mora_int' el maximo de la columna
#para cada lc en linea_credito

lc_dias_mora_max = []
for i in linea_credito:
    mora_dias = lc[lc['prodact_linea_credito']==i]
    maximo = mora_dias['prodact_dias_mora_int'].max()
    lc_dias_mora_max.append(maximo)

#Convertimos lc_dias_mora_max a un dataframe
lc_dias_mora_max = pd.DataFrame(lc_dias_mora_max, columns = 
                                ['prodact_dias_mora_int'])

#Ahora quitamos las LC repetidas del dataframe lc 
lc = lc.drop_duplicates('prodact_linea_credito').reset_index(drop=True)
#Sustituimos la columna 'prodact_dias_mora_int' por lc_dias_mora_max
lc['prodact_dias_mora_int'] = lc_dias_mora_max['prodact_dias_mora_int']

#Reemplazamos de lc['prodact_producto] todos los valores a 'LC'
lc['prodact_producto'] = 'LC'

#Ahora concatenamos lc a df
df = pd.concat([df, lc], axis=0, ignore_index=True)

#ordenamos por grupo
df = df.sort_values(by = 'prodact_id_grupo', ascending = True).reset_index(
    drop = True
)

#en df creamos una nueva columna llamada plazo,
#le asignamos el valor en meses de la diferencia entre
#prodact_f_venc - prodact_f_otorgado

df['prodact_f_venc'] = pd.to_datetime(df['prodact_f_venc'], 
                                      format= '%Y-%m-%d')#.replace(np.nan, 0)
df['prodact_f_otorgado'] = pd.to_datetime(df['prodact_f_otorgado'], 
                                          format= '%Y-%m-%d')

plazo = (df['prodact_f_venc'].dt.year - df['prodact_f_otorgado'
                                                 ].dt.year) * 12 + \
              (df['prodact_f_venc'].dt.month - df['prodact_f_otorgado'].dt.month)

# Si el día de 'prodact_f_venc' es menor que el día de 'prodact_f_otorgado', 
# restamos 1 mes (porque no se completó el mes)
plazo = plazo - (df['prodact_f_venc'
                                ].dt.day < df['prodact_f_otorgado'].dt.day
                                ).astype(int)
pos = df.columns.get_loc('prodact_f_venc')

df.insert(pos + 1, 'plazo', plazo)

#Agregamos la columna LME final:
#print(df['prodact_producto'].index)
#print(df['prodact_lme_aprobado_cli_usd'].index)
#print(df['prodact_lme_aprobado_cli_usd'].index)
LME_final = []
for idx, i in df['prodact_producto'].items():  # idx = índice, i = valor de la columna
    if i in ['LC', 'TC', 'CCR']:
        lme = df.loc[idx, 'prodact_lme_aprobado_cli_usd']  # Se usa idx para acceder directamente
        LME_final.append(lme)
    else:
        lme = df.loc[idx, 'prodact_lme_aprobado_cli_usd'] + df.loc[idx, 'prodact_lme_actual_cli_usd']
        LME_final.append(lme)

df['LME_final'] = LME_final


#Ahora exportamos el data frame df a un archivo .xlsx
ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\reporte_insumos.xlsx'
df.to_excel(ruta, index = False) 
