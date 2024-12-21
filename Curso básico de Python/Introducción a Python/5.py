#En este video abordaremos la estructura de datos llamada diccionarios.
#Los diccionarios son similares a las listas y las tuplas, con la diferencia que estas
# son secuencias ordenadas, los diccionarios son colecciones no ordenadas de pares clave-valor.
#Los diccionarios son útiles cuando necesitas asociar información de manera estructurada y accesible
#mediante un identificador (la clave). Puedes agregar, modificar o eliminar elementos en un diccionario
#según sea necesario
#la sintaxis del diccionario es:
#mi_diccionario = {"clave1": valor1, "clave2": valor2, "clave3": valor3}

#Ejemplo
print("""Haremos un miniprograma en el cual 
       asociaremos un país con su capital """)

diccionario_1={"Alemania":"Berlin","Francia":"Paris", "España":"Madrid"}
print(diccionario_1["Francia"])#esto nos devuelve paris
#print(diccionario_1["Paris"]) No funciona a la inversa, porque solo podemos poner la clave

#Si queremos agregar un valor más a nuetro diccionario basta con hacer:
diccionario_1["Nuevo elemento"]="Nueva clave"
#Ahora si llamamos al diccionario veremos que se agregó este archivo
print(diccionario_1)

#Si queremos eliminar un elemento de nuestro diccionario usamos
del diccionario_1["Alemania"] #Ponemos la clave del valor que queremos quitar
print(diccionario_1)
#En los diccionarios se les puede asignar a los valores, tuplas o listas.

#Si queremos el valor de las claves, podemos llamarlas usando keys
print(diccionario_1.keys())
print(diccionario_1)

#si queremos regresar a los valores usamos values
print(diccionario_1.values())
print(diccionario_1)
#si queremos la longitud del diccionario usamos len
print(len(diccionario_1))