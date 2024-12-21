#vamos a empezar definiendo variables, cabe destacar que en phyton no se define el tipo de variable como en c
#si yo escribo a="ejemplo", phyton entenderá sin necesida de decirle que es un str (texto).
#Si yo defino b=15, phyton entenderá que es un entero.
#Para definir una variable usamos =
a=5
b=3
c="Juan"
#para llamar a las variables (imprimirlo en consola) utilizo print
print(a)
#Operaciones básicas en phyton:
a+b 
a-b
a*b
a**b #exp
a%b #modulo, resto
a//b #División entera
#Para saber el tipo de variable que tenemos usamos el codigo type(variable)
print(type(a)) #para que aparezca en la consola
print(type(c))
print(c*5) #xd
#Para escribir en phyton usamos print como sabemos, pero si queremos agregar saltos de linea, a diferencia
#de c, acá utilizamos 3 comillas y separamos el texto como lo hariamos normalmente.
mensaje="""este
será
un
texto
con saltos de linea"""
print(mensaje)
#Ahora empezaremos a utilizar comparadores y condicionales
# empezamos con el condicional if, sabemos que este sirve para condicionar al programa y decirle que
#si se cumple x cosa, realice x cosa 
#si no se cumple tambien podemos darle una instrucción
no1=7
no_2=3
if no1>no_2:
    print(no1+no_2)
else: #intruccion si no se cumple
    print(no1-no_2)
#otro ejemplo:
if no1<=no_2:
    print("número 2 es mayor o igual que el numero 1")
else:
    print("numero 2 no es mayor o igual que el número 1")

    

