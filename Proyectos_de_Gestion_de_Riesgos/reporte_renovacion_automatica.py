import sys
sys.path.append(r'C:\Users\Fam. Figueroa\Desktop\Gerson\ECFM\Programas\Curso Phyton\Proyectos_de_Gestion_de_Riesgos')
import reporte_insumos as insumos
import pandas as pd
import numpy as np

#Ahora iniciamos el reporte de renovación
#Llamamos las tablas necesarias

#C:\\Users\\Fam. Figueroa\\Desktop\\Grupos e integrantes LZ 10.xlsx
#print(insumos.df)

'''formato = input('Ingrese el formato del archivo Grupos e integrantes LZ 10: '
'(excel o csv): ').strip().lower()'''
formato = 'excel'
if formato =='excel':
    #df3 = pd.read_excel(input('Ingrese la ruta del archivo Grupos e integrantes LZ 10:'))
    df3 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Grupos e integrantes LZ 10.xlsx')
elif formato =='csv':
    #df3 = pd.read_csv(input('Ingrese la ruta del archivo Grupos e integrantes LZ 10:'))
    df3 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Grupos e integrantes LZ 10.xlsx')
else:
    print("Entrada no válida")

#C:\\Users\\Fam. Figueroa\\Desktop\\Ratings LZ 11.xlsx
'''formato1 = input('Ingrese el formato del archivo Rating LZ: '
'(excel o csv): ').strip().lower()'''
formato1 = 'excel'
if formato1 =='excel':
    #df4 = pd.read_excel(input('Ingrese la ruta del archivo Rating LZ:'))
    df4 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Ratings LZ 11.xlsx')
elif formato1 =='csv':
    df4 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Ratings LZ 11.xlsx')
else:
    print("Entrada no válida")

#Vamos a extraer df la columna con clientes unicos de prodact_id_cliente 
id_clientes1 = pd.Series(insumos.df['prodact_id_cli'].unique()).copy()

#Buscamos el nit, nombre cliente,  de cada cliente en la tabla grupos e integrantes
nit = []
nombre_cli = []
cod_grupo = []
nombre_grupo = []
nombre_ejecutivo = []
banca_final = []

for i in id_clientes1:
    buscar = df3[df3["codigo_cliente"] == i]
    if not buscar.empty:
        hallar_nit = buscar["nit"].iloc[0]
        hallar_cliente = buscar["nombre_cliente"].iloc[0]
        hallar_cod_grupo = buscar["codigo_grupo"].iloc[0]
        hallar_nom_grupo = buscar["nombre_grupo"].iloc[0]
        hallar_nom_ejecutivo = buscar["nombre_gerente_beg"].iloc[0]
        hallar_banca_final = buscar["banca_sis"].iloc[0]
    else:
        hallar_nit = ''
        hallar_cliente = ''
        hallar_cod_grupo = ''
        hallar_nom_grupo = ''
        hallar_nom_ejecutivo = ''
        hallar_banca_final = ''        

    nit.append(hallar_nit)
    nombre_cli.append(hallar_cliente)
    cod_grupo.append(hallar_cod_grupo) 
    nombre_grupo.append(hallar_nom_grupo)
    nombre_ejecutivo.append(hallar_nom_ejecutivo)
    banca_final.append(hallar_banca_final)

#Creamos el dataframe df_renov, que será el informe de renovación
df_renov = pd.DataFrame()
df_renov["COD. CLIENTE"] = id_clientes1
df_renov["NIT"] = nit
df_renov["NOMBRE CLIENTE"] = nombre_cli
df_renov["COD. GRUPO"] = cod_grupo
df_renov["NOMBRE GRUPO"] = nombre_grupo
df_renov['NOMBRE EJECUTIVO'] = nombre_ejecutivo
df_renov.reset_index(drop=True)

#Hallamos ahora los datos del rating del cliente, el cual sacamos de rating LZ
#Utilizando la id_clientes1, buscamos en insumos.df la columna 'prodact_id_oblig_sis'
rating = []
no_rating = []
tipo_cliente = []
for i in id_clientes1:
    #Ahora buscamos el rating del cliente en la tabla df4
    buscar1 = df4[df4["num_doc"] == i]
    if not buscar1.empty:
        hallar_rating = buscar1["Rating"].iloc[0]
        hallar_tipo_cliente = buscar1['tipo_persona'].iloc[0]
    else:
        hallar_rating = ''
        hallar_tipo_cliente = ''
    
    if hallar_rating == 'R1':
        numero = 1
        no_rating.append(numero)
    elif hallar_rating == 'R2+':
        numero = 2
        no_rating.append(numero)
    elif hallar_rating == 'R2':
        numero = 3
        no_rating.append(numero)
    elif hallar_rating == 'R2-':
        numero = 4
        no_rating.append(numero)
    elif hallar_rating == 'R3+':
        numero = 5
        no_rating.append(numero)
    elif hallar_rating == 'R3':
        numero = 6
        no_rating.append(numero)
    elif hallar_rating == 'R3-':
        numero = 7
        no_rating.append(numero)
    elif hallar_rating == 'R4':
        numero = 8
        no_rating.append(numero)
    elif hallar_rating == 'R5':
        numero = 9
        no_rating.append(numero)
    else:
        numero = 0 #n/a
        no_rating.append(numero)

    rating.append(hallar_rating)
    tipo_cliente.append(hallar_tipo_cliente)

#Agregamos estas nuevas columnas al informe
df_renov['Rating'] = rating
df_renov['RATING NUMERO'] = no_rating


#Hallaremos ahora el maximo rating por grupo y a esto le llamaremos rating grupal
#extraemos los grupos de insumos.df
no_grupo = pd.Series(df_renov['COD. GRUPO'].unique().copy()).reset_index(drop = True)
rating_grupal = []
for i in no_grupo:
    buscar = df_renov[df_renov['COD. GRUPO'] == i]
    hallar_rating_grupal = buscar['RATING NUMERO'].max()
    rating_grupal.append(hallar_rating_grupal)

#Agregamos rating_grupal al informe, tal que rating_grupal[i] le corresponde a 
#no_grupo[i]
rating_grupo_dict = dict(zip(no_grupo, rating_grupal))

# Asignar rating grupal a cada cliente según su grupo
df_renov['RATING GRUPAL'] = df_renov['COD. GRUPO'].map(rating_grupo_dict)
df_renov['Tipo de cliente'] = tipo_cliente
#Exportamos el informe df_renov a un archivo excel como informe_renovacion.xlsx
if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\informe_renovacion.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        df_renov.to_excel(writer, sheet_name='Reporte Renovacion', index=False)