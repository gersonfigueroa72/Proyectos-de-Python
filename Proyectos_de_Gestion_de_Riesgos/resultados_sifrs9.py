import pandas as pd
#Iniciamos llamando a las tablas a utilizar
formato = 'excel'
if formato =='excel':
    df = pd.read_excel(input('Ingrese la ruta del archivo Reporte_insumos:'))
elif formato =='csv':
    df = pd.read_csv(input('Ingrese la ruta del archivo Reporte_insumos:'))
else:
    print("Entrada no válida")

if formato =='excel':
    df1 = pd.read_excel(input('Ingrese la ruta del archivo :'))
elif formato =='csv':
    df1 = pd.read_csv(input('Resultados SIFRS9 :'))
else:
    print("Entrada no válida")

# de df iniciamos eliminando a clientes BEG

df = df[df['prodact_beg_bpp'] == 'BEG']

# Extramos los clientes sin repetir de df 

clientes_id = df['prodact_id_cli'].unique()

#Buscamos ahora el nombre y grupo del cliente 

nombre = []
grupo = []

for i in clientes_id:
    buscar = df[df['prodact_id_cli'] == i]
    hallar_nombre = buscar['prodact_nombre_cli'].iloc[0]
    hallar_grupo = buscar['prodact_nombre_cli'].iloc[0]
    nombre.append(hallar_nombre)
    grupo.append(hallar_grupo)

#Agregamos estas columnas al informe

informe = pd.DataFrame()

informe['ID'] = clientes_id
informe['NOMBRE'] = nombre
informe['GRUPO'] = grupo

#Ahora de df1, hallamos 
expo = []
obligacion = df['prodact_id_oblig']
for i in obligacion:
    buscar = df1[df1['NUMERO_OBLIGACION'] == i]
    hallar_expo = buscar['EXPOSICION_TOTAL_FA']
    expo.append(hallar_expo)

informe['EXPOSICION CIERRE'] = expo 
informe['GRUPO INTERNO'] = ''

#Exportamos el informe df_renov a un archivo excel como bam.xlsx
if __name__ == '__main__':
    ruta = 'C:\\Users\\Fam. Figueroa\\Desktop\\bam.xlsx'
    with pd.ExcelWriter(ruta, engine='openpyxl') as writer:
    # Exportar cada DataFrame a una hoja diferente
        informe.to_excel(writer, sheet_name='Bam Cierre', index=False)