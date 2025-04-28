import pandas as pd
import numpy as np

#Ahora iniciamos el reporte de renovación
#Llamamos las tablas necesarias

formato = 'excel'
if formato =='excel':
    df = pd.read_excel(input('Ingrese la ruta del archivo Reporte_insumos:'))
elif formato =='csv':
    df = pd.read_csv(input('Ingrese la ruta del archivo Reporte_insumos:'))
else:
    print("Entrada no válida")

'''formato = input('Ingrese el formato del archivo Grupos e integrantes LZ 10: '
'(excel o csv): ').strip().lower()'''
if formato =='excel':
    df3 = pd.read_excel(input('Ingrese la ruta del archivo Grupos e integrantes LZ 10:'))
elif formato =='csv':
    df3 = pd.read_csv(input('Ingrese la ruta del archivo Grupos e integrantes LZ:'))
else:
    print("Entrada no válida")

'''formato = input('Ingrese el formato del archivo Rating LZ: '
'(excel o csv): ').strip().lower()'''
if formato =='excel':
    df4 = pd.read_excel(input('Ingrese la ruta del archivo Rating LZ:'))
elif formato =='csv':
    df4 = pd.read_csv(input('Ingrese la ruta del archivo Rating LZ:'))
else:
    print("Entrada no válida")

'''formato = input('Ingrese el formato del archivo Reporte SIB: '
'(excel o csv): ').strip().lower()'''
if formato =='excel':
    df5 = pd.read_excel(input('Ingrese la ruta del archivo Reporte SIB LZ:'),
                        skiprows = 0, # Ajusta este número si hay filas vacías al inicio
                        header=0, # Ajusta este número para indicar qué fila contiene los nombres de columnas
                        na_values=['', ' ', 'NA', 'N/A']  # Valores a considerar como NA
                        )
elif formato =='csv':
    df5 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Reporte SIB LZ 5.xlsx')
else:
    print("Entrada no válida")

#Vamos a extraer df la columna con clientes unicos de prodact_id_cliente 
id_clientes1 = pd.Series(df['prodact_id_cli'].unique()).copy().reset_index(drop=True)

#Buscamos el nit, nombre cliente,  de cada cliente en la tabla grupos e integrantes
nit = [] #preguntar si sacar de grupos e integrantes
nombre_cli = []
cod_grupo = []
nombre_grupo = []
nombre_ejecutivo = []
banca_final = []

for i in id_clientes1:
    buscar = df5[df5["ctrlext_id_cli"] == i]
    if not buscar["ctrlext_id_cli"].empty:
        hallar_nit = buscar["ctrlext_nit_cli"].unique()[0]
    elif buscar["ctrlext_id_cli"].empty:
        hallar_nit = ""
    else:
        print(f"El cliente {i} tiene mas de un nit (Revisar tabla) Reporte SIB LZ")
    nit.append(hallar_nit)

for i in id_clientes1:
    buscar = df3[df3["codigo_cliente"] == i]
    if not buscar.empty:
        hallar_cliente = buscar["nombre_cliente"].iloc[0]
        hallar_cod_grupo = buscar["codigo_grupo"].iloc[0]
        hallar_nom_grupo = buscar["nombre_grupo"].iloc[0]
        hallar_nom_ejecutivo = buscar["nombre_gerente_beg"].iloc[0]
        hallar_banca_final = buscar["banca_sis"].iloc[0]
    else:
        hallar_cliente = ''
        hallar_cod_grupo = ''
        hallar_nom_grupo = ''
        hallar_nom_ejecutivo = ''
        hallar_banca_final = ''        

    nombre_cli.append(hallar_cliente) #Si esto no guarda el indice, entonces esta bien
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
df_renov['Banca Final'] = banca_final
df_renov.reset_index(drop=True)

#Hallamos ahora los datos del rating del cliente, el cual sacamos de rating LZ
#Utilizando la id_clientes1
rating = []
no_rating = []
tipo_cliente = []

for i in id_clientes1:
    # Buscamos el cliente en df4
    buscar1 = df4[df4["num_doc"] == i]
    
    if not buscar1.empty:  # Si encontramos el cliente
        # Primero intentamos obtener rating_act
        if not pd.isna(buscar1["rating_act"].iloc[0]):
            hallar_rating_no = buscar1["rating_act"].iloc[0]
        # Si rating_act está vacío, buscamos en rng_score_actual
        else:
            hallar_rating_no = buscar1["rng_score_actual"].iloc[0]
        
        hallar_tipo_cliente = buscar1["tipo_persona"].iloc[0]
    else:  # Si no encontramos el cliente
        hallar_rating_no = np.nan
        hallar_tipo_cliente = ''
    if hallar_rating_no == 1:
        rating1 = 'R1'
        rating.append(rating1)
    elif hallar_rating_no == 2:
        rating1 = 'R2+'
        rating.append(rating1)
    elif hallar_rating_no == 3:
        rating1 = 'R2'
        rating.append(rating1)
    elif hallar_rating_no == 4:
        rating1 = 'R2-'
        rating.append(rating1)
    elif hallar_rating_no == 5:
        rating1 = 'R3+'
        rating.append(rating1)
    elif hallar_rating_no == 6:
        rating1 = 'R3'
        rating.append(rating1)
    elif hallar_rating_no == 7:
        rating1 = 'R3-'
        rating.append(rating1)
    elif hallar_rating_no == 8:
        rating1 = 'R4'
        rating.append(rating1)
    elif hallar_rating_no == 9:
        rating1 = 'R5'
        rating.append(rating1)

    else:
        rating1 = '' #n/a
        rating.append(rating1)

    no_rating.append(hallar_rating_no)
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
    hallar_rating_grupal = buscar['RATING NUMERO'].max(skipna = True)
    rating_grupal.append(hallar_rating_grupal)

#Agregamos rating_grupal al informe, tal que rating_grupal[i] le corresponde a 
#no_grupo[i]
rating_grupo_dict = dict(zip(no_grupo, rating_grupal))

# Asignar rating grupal a cada cliente según su grupo
df_renov['RATING GRUPAL'] = df_renov['COD. GRUPO'].map(rating_grupo_dict)

#Ahora calcularemos el LME por grupo y asignaremos el LME individual a cada cliente
LME_grupal=[]
for i in df_renov["COD. GRUPO"]:
    buscar = df[df["prodact_id_grupo"] == i]
    if not buscar.empty:
        hallar_lme_grupal = pd.Series(buscar["LME_final"]).sum()
    else:
        hallar_lme_grupal = ""
    LME_grupal.append(hallar_lme_grupal)

#Asignamos ahora este valor a su grupo correspondiente

LME_grupal_dict = dict(zip(no_grupo, LME_grupal))
df_renov['LME GRUPAL'] = df_renov['COD. GRUPO'].map(LME_grupal_dict)


lme_cli = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df[df["prodact_id_cli"] == i]
    #Haremos la suma de el LME total del cliente
    hallar_lme_cli = pd.Series(buscar["LME_final"]).sum()
    lme_cli.append(hallar_lme_cli)

df_renov["LME Cliente"] = lme_cli
df_renov['Tipo de cliente'] = tipo_cliente

#Hallamos ahora a la persona lider de empresa 
#Solo es persona lider la persona juridica y con mayor LME del grupo
'''revisar'''
persona_lider = []

for i in df_renov["COD. CLIENTE"]:  # Iterar por cada cliente
    # Obtener el grupo al que pertenece el cliente
    grupo_cliente = df_renov[df_renov["COD. CLIENTE"] == i]["COD. GRUPO"].iloc[0]
    
    # Obtener todos los clientes del mismo grupo
    clientes_mismo_grupo = df_renov[df_renov["COD. GRUPO"] == grupo_cliente]
    
    # Obtener el LME del cliente actual
    lme_cliente = df_renov[df_renov["COD. CLIENTE"] == i]["LME Cliente"].iloc[0]
    
    # Verificar si el cliente es PJ y tiene el máximo LME de su grupo
    es_pj = df_renov[df_renov["COD. CLIENTE"] == i]["Tipo de cliente"].iloc[0] == "PJ"
    es_maximo = lme_cliente == clientes_mismo_grupo["LME Cliente"].max()
    
    if es_pj and es_maximo:
        persona_lider.append("si")
    else:
        persona_lider.append("no")

df_renov["Empresa Líder"] = persona_lider

#Ahora hallamos la calificación SIB de la tabla Reporte SIB LZ 
'''
Revisar acá si a los que no tiene calif. Les corresponde S/C
y si le corresponde 6 o 0
'''
calif_sib = []
no_calif_sib = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df5[df5["ctrlext_id_cli"]==i]
    if not buscar.empty:
        calif_min = []  # Lista temporal para cada cliente
        for j in buscar["ctrlext_clasif"]:
            if j == "S/C":
                calif_min.append(6)  # S/C tiene el valor más alto
            elif j == "A":
                calif_min.append(1)
            elif j == "B":
                calif_min.append(2)
            elif j == "C":
                calif_min.append(3)
            elif j == "D":
                calif_min.append(4)
            elif j == "E":
                calif_min.append(5)
#        else:
#            calif_min.append("S/C")
        
        # Obtener el mínimo una vez por cliente
        min_value = min(calif_min)
        no_calif_sib.append(min_value)
        
        # Convertir el número a letra
        if min_value == 6:
            hallar_calif_sib = "S/C"
        elif min_value == 1:
            hallar_calif_sib = "A"
        elif min_value == 2:
            hallar_calif_sib = "B"
        elif min_value == 3:
            hallar_calif_sib = "C"
        elif min_value == 4:
            hallar_calif_sib = "D"
        elif min_value == 5:
            hallar_calif_sib = "E"
    else:
        # Si no se encuentra el cliente
        no_calif_sib.append("")
        hallar_calif_sib = ""
    
    calif_sib.append(hallar_calif_sib)

# Agregar las columnas al DataFrame
df_renov["Calificación SIB"] = calif_sib
df_renov["NUMERO SIB"] = no_calif_sib

#Hallamos a los clientes que tengan una mora mayor a 30 días
#si mora mayor 30 entonces le asignamos 1, caso contrario 0
mora = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df[df["prodact_id_cli"] == i]
    if not buscar.empty:
        hallar_mora = buscar["prodact_mora_mayor_30"].max()
        mora.append(hallar_mora)
    else:
        # Si no se encuentra el cliente, asignar un valor por defecto
        mora.append(np.nan)  # o podriamos usar 0

df_renov["Mora >30"] = mora

#Por ultimo, verificamos si el cliente tiene revolventes y si tiene solo TC 
#o mas productos
productos = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df[df["prodact_id_cli"] == i]
    if (buscar["prodact_producto"] == "TC").all():
        productos.append("Solo TC")
    else:
        productos.append("Mas productos")
df_renov["Productos"] = productos

revolventes = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df[df["prodact_id_cli"] == i]
    if buscar["prodact_producto"].isin(['LC', 'CCR']).any():
        #isin, crea una serie booleana en donde verifica si se encuentra lc o ccr
        #any, encuentra si al menos un booleando es verdadero 
        revolventes.append("Tiene revolventes")
    else:
        revolventes.append("No tiene revolventes")

df_renov["Revolventes"] = revolventes

#Por ultimo filtramos los datos:
df_renov = df_renov[df_renov["RATING NUMERO"]>5]
df_renov = df_renov[df_renov['Calificación SIB'].isin(['A', 'B', 'S/C'])]
df_renov = df_renov[df_renov["LME GRUPAL"]< 8000000]
df_renov = df_renov.reset_index(drop = True)
        
#Exportamos el informe df_renov a un archivo excel como informe_renovacion.xlsx
if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\informe_renovacion.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        df_renov.to_excel(writer, sheet_name='Reporte Renovacion', index=False)
