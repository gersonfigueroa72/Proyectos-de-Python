import pandas as pd

# Creamos un DataFrame principal con índices no consecutivos
df_principal = pd.DataFrame({
    'id_cliente': [101, 102, 103],
    'grupo': [2, 1, 3],
    'valor_actual': [50, 60, 70]
}, index=[2, 0, 1])
print("DataFrame principal original:")
print(df_principal)
print()  # Línea en blanco

# Creamos un DataFrame extra con índices diferentes. Por ejemplo, calculamos una suma:
df_extra = pd.DataFrame({
    'id_cliente': [101, 102, 103],
    'suma_valor': [500, 600, 700]
})
# Como queremos asociar el valor usando el id_cliente, por defecto el índice de df_extra es 0,1,2.
print("DataFrame extra:")
print(df_extra)
print()

# Opción A: Asignamos directamente usando la posición (esto depende de los índices)
# Si hacemos una asignación directa, pandas alinea por el índice:
df_principal['suma_valor'] = df_extra['suma_valor']
print("Después de asignar directamente (alineación por índice):")
print(df_principal)
print()

# Nótese que df_principal tiene índices [2, 0, 1] y df_extra tiene índices [0,1,2].
# Esto significa que el valor en el índice 2 de df_principal recibe el valor correspondiente al índice 2 en df_extra.
# Es decir, la fila del cliente 101 (índice 2 en df_principal) recibirá 700, aunque en realidad ese
# cliente (101) debería tener 500 según df_extra.

# Para evitar ese problema, usamos una asignación por clave (por ejemplo, usando map)
# Primero creamos un diccionario que mapea id_cliente a suma_valor:
mapa = dict(zip(df_extra['id_cliente'], df_extra['suma_valor']))
# Ahora asignamos usando el id_cliente de df_principal:
df_principal['suma_valor'] = df_principal['id_cliente'].map(mapa)
print("Después de asignar usando map (alineación por 'id_cliente'):")
print(df_principal)
print()

# Ahora, supongamos que ordenamos el DataFrame principal por el número de grupo
df_ordenado = df_principal.sort_values(by='grupo', ascending=True)
print("DataFrame principal ordenado por 'grupo':")
print(df_ordenado)