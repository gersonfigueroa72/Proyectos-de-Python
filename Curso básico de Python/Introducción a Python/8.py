#En este apartado entenderemos acerca de concatenacion de operadores
#de comparacion 
#operadores logicos and y or
#y el operador in

edad=int(input("COLOQUE SU EDAD "))
if 0<edad<100:#Concatenamos 2 operadores 
    print("edad correcta")
else:
    print("edad incorrecta")
    
########
#si queremos imprimir dos valores en la consola en la misma linea 
#podemos usar el operador + para concatenarlos
#deberemos tener en cuenta que phyton no puede concatenar valores de
#diferente tipo
mi_salario=int(input("Introduce tu salario "))
#Ahora imprimiremos el salario
print("Tu salario es: "+ str(mi_salario)) #nota tuvimos que convertir 
#mi salario a texto sino nos daría error
#AND
#El operador logico and se puede traducir como "y si ademas"
#y el operador logico OR se puede traducir como "o si no"

#Programa que evaluará si un alumno merece o no la beca
#debera cumplir que tenga mas de dos hermanos
#que viva a mas de 40km del instituto
#que el salario familiar sea menor a 20k
print("Programa de Beca 2024")
distancia=int(input("Introduce la distancia a la escuela en km "))
print(distancia)

hermanos=int(input("Introduce el numero de hermanos "))
print("número de hermanos"+ str(hermanos))

salario=int(input("Introduce el salario familiar "))
print("El salario familiar es "+ str(salario))

if distancia>40 and hermanos>=2 and salario<20000: #agregamos varias condiciones que debe cumplir el if
#que se deben cumplir todas para activar al if
    print("Obtuviste la beca")
else:
    print("No obtuviste la beca")

#Sin embargo el programa es un poco injusto por lo tanto renovaremos el programa

print("Programa de becas 2.0")

if distancia>40 or hermanos>=2 or salario<20000: #agregamos varias condiciones aunque el or nos permite que
#no se cumplan todas necesariamente
    print("Obtuviste la beca")
else:
    print("No obtuviste la beca")

#Crearemos un programa donde el alumno pueda escoger una asignatura optativa
print("Asignaturas optativas 2024")
print("Biofísica-Geofísica-Astronomía")
asignaturas=input("Elige tu asignatura ")
#in nos dice si en asignaturas está algunos de los valores
#que queremos

if asignaturas in ("Biofisica", "Geofisica", "Astronomia"):
    print("Escogiste " + asignaturas)
else:
    print("Esta asignatura no está disponible")

#Notemos que debemos poner las asignaturas tal cual como las declaramos en el in
#pq sino nos marcará que la asignatura no está disponible
#para solucionar esto podemos usar lower() y upper()
#lower() transforma texto a minuscula
#upper() "               " a mayuscula

#Ejemplo
texto="hola que hace"
print(texto.upper())