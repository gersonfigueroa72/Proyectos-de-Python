import sys
sys.path.append(r'C:\Users\Fam. Figueroa\Desktop\Gerson\ECFM\Programas\Curso Phyton\Proyectos_de_Gestion_de_Riesgos')
import reporte_insumos as insumos
import pandas as pd
import numpy as np

#Ahora iniciamos el reporte de renovación
#Llamamos las tablas necesarias

#C:\\Users\\Fam. Figueroa\\Desktop\\Grupos e integrantes LZ 10.xlsx
#print(insumos.df) #revisemos los indices de insumos.df

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

#C:
'''formato1 = input('Ingrese el formato del archivo Reporte SIB: '
'(excel o csv): ').strip().lower()'''
formato2 = 'excel'
if formato2 =='excel':
    #df5 = pd.read_excel(input('Ingrese la ruta del archivo Reporte SIB LZ:'))
    df5 = pd.read_excel('C:')
elif formato1 =='csv':
    df5 = pd.read_excel('C:\\Users\\Fam. Figueroa\\Desktop\\Ratings LZ 11.xlsx')
else:
    print("Entrada no válida")

#Vamos a extraer df la columna con clientes unicos de prodact_id_cliente 
id_clientes1 = pd.Series(insumos.df['prodact_id_cli'].unique()).copy().reset_index(drop=True)

#Buscamos el nit, nombre cliente,  de cada cliente en la tabla grupos e integrantes
nit = []
nombre_cli = []
cod_grupo = []
nombre_grupo = []
nombre_ejecutivo = []
banca_final = []

for i in id_clientes1:
    buscar = df5[df5["ctrlext_id_cli"] == i]
    if not buscar["ctrlext_id_cli"].empty:
        hallar_nit = buscar["ctrlext_nit_cli"].unique()
    else:
        hallar_nit = ""
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
df_renov.reset_index(drop=True)

#Hallamos ahora los datos del rating del cliente, el cual sacamos de rating LZ
#Utilizando la id_clientes1
rating = []
no_rating = []
tipo_cliente = []
for i in id_clientes1:
    #Ahora buscamos el rating del cliente en la tabla df4
    buscar1 = df4[df4["num_doc"] == i]
    if not buscar1["rating_act"].empty:
        hallar_rating = buscar1["rating_act"]
        hallar_tipo_cliente = buscar1["tipo_persona"]
    else:
        hallar_rating = buscar1["rng_score_actual"]
        hallar_tipo_cliente = buscar1["tipo_persona"]
    
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

#Ahora calcularemos el LME por grupo y asignaremos el LME individual a cada cliente
LME_grupal=[]
for i in df_renov["COD. GRUPO"]:
    buscar = insumos.df[insumos.df[prodact_id_grupo] == i]
    if not buscar.empty:
        hallar_lme_grupal = buscar["LME_final"].unique().sum()
    else:
        hallar_lme_grupal = ""
    LME_grupal.append(hallar_lme_grupal)

#Asignamos ahora este valor a su grupo correspondiente

LME_grupal_dict = dict(zip(no_grupo, LME_grupal))
df_renov['LME GRUPAL'] = df_renov['COD. GRUPO'].map(LME_grupal_dict)

lme_cli = []
for i in df_renov["COD. CLIENTE"]:
    buscar = insumos.df[insumos.df["LME_final"] == i]
    hallar_lme_cli = buscar["LME_final"].unique() #revisar
    lme_cli.append(hallar_lme_cli)

df_renov["LME Cliente"] = lme_cli
df_renov['Tipo de cliente'] = tipo_cliente

#Hallamos ahora a la persona lider de empresa 

persona_lider = []
for i in df_renov["COD. GRUPO"]:
    buscar = df_renov[df_renov["COD. GRUPO"] == i]
    hallar_persona_lider = buscar[buscar["LME Cliente"].max()]
    if hallar_persona_lider["Tipo de cliente"] == "PJ":
        persona_lider.append("si")
    else:
        persona_lider.append("no")

df_renov["Empresa Líder"] = persona_lider

#Ahora hallamos la calificación SIB de la tabla Reporte SIB LZ 
calif_sib = []
no_calif_sib = []
for i in df_renov["COD. CLIENTE"]:
    buscar = df5[df5["ctrlext_id_cli"]==i]
    if not buscar.empty:
        for j in buscar["ctrlext_clasif"]:
            calif_min =[]
            if j == "S/C":
                hallar_no_calif_sib = 0
                calif_min.append(hallar_no_calif_sib)
            elif j == A:
                hallar_no_calif_sib = 1
                calif_min.append(hallar_no_calif_sib)
            elif j == B:
                hallar_no_calif_sib = 2
                calif_min.append(hallar_no_calif_sib)
            elif j == C:
                hallar_no_calif_sib = 3
                calif_min.append(hallar_no_calif_sib)
            elif j == D:
                hallar_no_calif_sib = 4
                calif_min.append(hallar_no_calif_sib)
            elif j == E:
                hallar_no_calif_sib = 5
                calif_min.append(hallar_no_calif_sib)
        no_calif_sib.append(min(calif_min)) #Hallamos el minimo de las j calif del cliente
        #A la altura del if not
        if min(calif_min) == 0:
            hallar_calif_sib = "S/C"
        if min(calif_min) == 1:
            hallar_calif_sib = "A"
        if min(calif_min) == 2:
            hallar_calif_sib = "B"
        if min(calif_min) == 3:
            hallar_calif_sib = "C"
        if min(calif_min) == 4:
            hallar_calif_sib = "D"
        if min(calif_min) == 5:
            hallar_calif_sib = "E"
    else:
        hallar_calif_sib = ""
        hallar_no_calif = ""
    #a la altura del for
    calif_sib.append(hallar_calif_sib)
    no_calif_sib.append(hallar_no_calif)

#Agregamos ahora estos valores a df_renov
df_renov["Calificación SIB"] = calif_sib
df_renov["NUMERO SIB"] = no_calif_sib

#Hallamos a los clientes que tengan una mora mayor a 30 días
#si mora mayor 30 entonces le asignamos 1, caso contrario 0
mora = []
for i in df_renov["COD. CLIENTE"]:
    buscar = insumos.df[insumos.df["prodact_id_cli"] == i]
    hallar_mora = buscar["prodact_mora_mayor_30"].max()
    mora.append(hallar_mora)

df_renov["Mora >30"] = mora
#Por ultimo, verificamos si el cliente tiene revolventes y si tiene solo TC 
#o mas productos
productos = []
for i in df_renov["COD. CLIENTE"]:
    buscar = insumos.df[insumos.df["prodact_id_cli"] == i]
    if (buscar["prodact_producto"] == "TC").all():
        productos.append("Solo TC")
    else:
        productos.append("Mas productos")

revolventes = []
for i in df_renov["COD. CLIENTE"]:
    buscar = insumos.df[insumos.df["prodact_id_cli"] == i]
    if buscar["prodact_productos"].isin(['LC', 'CCR']).any():
        #isin, crea una serie booleana en donde verifica si se encuentra lc o ccr
        #any, encuentra si al menos un booleando es verdadero 
        revolventes.append("Tiene revolventes")
    else:
        revolventes.append("No tiene revolventes")

df_renov["Productos"] = productos
df_renov["Revolventes"] = revolventes

#Por ultimo filtramos los datos:
df_renov = df_renov[df_renov["RATING NUMERO"]>5]
df_renov = df_renov[df_renov['Calificación SIB'].isin(['A', 'B', 'S/C'])]
df_renov = df_renov[df_renov["LME GRUPO"]< 8000000]
        
#Exportamos el informe df_renov a un archivo excel como informe_renovacion.xlsx
if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\informe_renovacion.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        df_renov.to_excel(writer, sheet_name='Reporte Renovacion', index=False)
