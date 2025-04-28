'''
Explicación
'''
#Importamos las librerias a utilizar
import pandas as pd
import numpy as np

#Iniciamos extraendo los datos necesarios ya sea de un archivo csv o xlsx

#formato = input('Ingrese el formato del archivo de insumos (excel o csv): ').strip().lower()
formato = 'excel'
if formato == 'excel':
    ruta = input('Ingrese la ruta del archivo de insumos:')
    df = pd.read_excel(ruta)
    #print(df)
else:
    ruta = input('Ingrese la ruta del archivo de insumos:')
    df = pd.read_csv(ruta)
    #print(df)

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

df1 = df.loc[:, 'f_analisis':'prodact_lme_actual_cli_usd'].copy()

#De este nuevo data frame eliminaremos todos los datos que no sean de 
#tarjetas de credito y nos aseguramos que en la columna prodact_beg_bpp haya 
#solo creditos beg y no bpp

df1 = df1[(df1['prodact_producto'] == 'TC') & (df1['prodact_beg_bpp']=='BEG')]
#print(df1)
#print(df1.columns) #verificamos las columnas que quedaron

#Ahora empezamos creando una columna para el id del cliente (no se debe repetir)
#el id, y a la derecha colocamos su LME aprobado en USD

id_clientes = df1['prodact_id_cli'].unique()

#Ahora crearemos una columna con la suma del saldo aprobado en USD y Q de cada cliente

id_cli = [] 
suma_saldo_usd = [] #Suma saldo * cliente
suma_saldo_gtq = []

for i in id_clientes:
    id_cli.append(i)
    saldo_clientes = df1[df1['prodact_id_cli']==i]
    suma_usd = saldo_clientes['prodact_saldok_usd'].sum()
    suma_gtq = saldo_clientes['prodact_saldok_gtq'].sum()
    suma_saldo_usd.append(suma_usd)
    suma_saldo_gtq.append(suma_gtq)

saldo = pd.DataFrame()
#agregamos id_cli y suma_saldo_usd a saldo
saldo['id_cliente'] = id_cli
saldo['suma_saldo_usd'] = suma_saldo_usd
saldo['suma_saldo_gtq'] = suma_saldo_gtq
#print(saldo) 

#Ahora vamos a eliminar los clientes repetidos en df1 y eliminamos los datos 
#de 'prodact_saldok_usd', 'prodact_saldok_gtq'  sustituimos por saldo['suma_saldo_usd'] 
#saldo[prodact_saldok_gtq] respectivamente

df1 = df1.drop_duplicates(subset=['prodact_id_cli']).reset_index(drop=True)
df1['prodact_saldok_usd'] = saldo['suma_saldo_usd']
df1['prodact_saldok_gtq'] = saldo['suma_saldo_gtq']
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
lc['prodact_descri_producto'] = 'LINEA DE CREDITO'

#Reemplazamos las fechas
lc['prodact_f_otorgado'] = lc['prodact_f_aprob_lc']
lc['prodact_f_venc'] = lc['prodact_f_venc_lc']

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
        lme = df.loc[idx, 'prodact_saldok_usd']
        LME_final.append(lme)

df['LME_final'] = LME_final #Acá termina el informe de Insumos

'''
Ahora creamos el informe para Wil
'''

df2 = df.copy() #Acá limpiaremos los datos para reporte 1

garantias = []

#Creamos la columna de garantias
for i in df2['prodact_tipo_garantia']:
    if i == 1:
        i = "FIDUCIARIA"
        garantias.append(i)
    elif i == 2:
        i = "HIPOTECARIA"
        garantias.append(i)
    elif i == 3:
        i = "PRENDARIA"
        garantias.append(i)
    elif i == 4:
        i = 'HIPOTECARIA - FIDUCIARIA'
        garantias.append(i)
    elif i == 5:
        i = 'PRENDARIA - FIDUCIARIA'
        garantias.append(i)
    elif i == 6:
        i = 'HIPOTECARIA - PRENDARIA'
        garantias.append(i)
    elif i == 7:
        i = 'HIPOTECARIA - PRENDARIA - FIDUCIARIA'
        garantias.append(i)
    elif i == 8:
        i = 'BONO DE PRENDA'
        garantias.append(i)    
    elif i == 9:
        i = 'GARANTIA DE OBLIGACIONES PROPIAS'
        garantias.append(i)
    elif i == 11:
        i = 'GARANTIA MOBILIARIA'
        garantias.append(i)
    elif i == 12:
        i = 'FIDUCIARIA BIENES INMUEBLES OTRAS GARANTIAS'
        garantias.append(i)
    elif i == 19 or i == 20:
        i = 'GARANTIA MOBILIARIA - FIDUCIARIA'
        garantias.append(i)
    elif i == 16 or i == 21:
        i = 'FIDEICOMISO DE GARANTIA'
        garantias.append(i)
    elif i == 99 or i ==17:
        i = 'OTRAS'
        garantias.append(i)
    else:
        i = 'No info'

#concatenamos las columnas prodact_cod_libro - prodact_libro
libro = df2['prodact_cod_libro'].astype(str) + '-' + df2['prodact_libro'].astype(str)
df2['libro'] = libro

#Extraemos las columnas a utilizar de df
columnas_a_agregar = ['prodact_id_cli','prodact_id_oblig_sis','prodact_nombre_cli'
                      ,'libro','prodact_producto','plazo']
reporte1 = df2[columnas_a_agregar].copy()
reporte1['Garantía'] = pd.Series(garantias)
reporte1['LME actual'] = np.nan
reporte1['Saldo actual'] = np.nan
reporte1['Unidad de riesgo'] = np.nan

#Ahora exportamos el data frame df a un archivo reporte_insumos.xlsx
if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\reporte_insumos.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        df.to_excel(writer, sheet_name='Reporte Insumos', index=False)
        reporte1.to_excel(writer, sheet_name='Reporte Wil', index=False)
