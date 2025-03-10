archivo=open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba.txt", "r")
print(archivo.read())
print(archivo.name)
archivo.close()

# Abrir el archivo y cerrarlo automáticamente
with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba.txt", "r") as archivo:
    # Leer el contenido del archivo
    contenido = archivo.read()  # se guarda el texto (archivo) en la variable contenido
    print(contenido)
    
    # Mover el puntero del archivo al principio
    archivo.seek(0)
    
    # Leer todas las líneas del archivo
    lista = archivo.readlines()  # se guarda el texto (archivo) en la variable lista
    print(lista)
    print(lista[0])  # se imprime la primera línea del 
    

"""aunque se cierra automáticamente, se puede seguir accediendo al contenido, ya que
se guarda en la variable contenido"""

#para leer linea por linea, se hace lo siguiente:
with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba.txt", "r") as archivo:
    leer=archivo.readline()
    print(leer) #imprime la primera línea
    leer=archivo.readline()
    print(leer) #imprime la segunda línea
    leer=archivo.readline()
    print(leer) #imprime la tercera línea

    archivo.seek(0)

    #para leer cierto numero de palabras se usa el método readline(número de palabras)
    leer=archivo.read(3)
    print(leer) #imprime las primeras 3 letras de la primera línea
    leer=archivo.read(16) 
    print(leer) #imprime las siguientes 16 letras, respetando las lineas

'''
ahora vamos a escribir en el archivo prueba2.txt usando el metodo write
Este metodo crea un archivo si no existe, si existe, lo sobreescribe, es decir
borra el contenido anterior y escribe todo de nuevo.
'''


with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba2.txt", "w") as archivo1:
    archivo1.write("Hola mundo")
    archivo1.write(" soy Gerson")
    archivo1.write("\n y estoy escribiendo.")

#ahora leemos el archivo

with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba2.txt", "r") as archivo1:
    print(archivo1.read())
    archivo1.seek(0)


'''
si queremos escribir sobre un texto ya existente, usamos el método append
'''

with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba2.txt", "a") as archivo1:
    archivo1.write("\n Ahora estoy escribiendo sobre un texto existente.")

with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba2.txt", "r") as archivo1:
    print(archivo1.read())


'''
Por ultimo para copiar un archivo a otro se hace lo siguiente:
'''

with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba2.txt", "r") as archivo1:
    with open("C:\\Users\\Fam. Figueroa\\Downloads\\prueba3.txt", "w") as archivo2:
        for linea in archivo1:
            archivo2.write(linea)