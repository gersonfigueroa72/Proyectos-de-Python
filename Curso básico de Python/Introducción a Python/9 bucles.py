#Un bucle en programación es una estructura que permite ejecutar un conjunto de instrucciones 
#repetidamente hasta que una condición específica se cumple.
#Tenemos en phyton dos clases de bucles
#Primer tipo: Determinados

#Los bucles determinados son de los que sabemos cuantas veces se repetirán
#como una sumatoria de 1 a 100

#mientras que los bucles indeterminados de estos no sabemos cuantas veces se repetirán
#y dependerán de la circunstancias en las cuales se ejecute el codigo
#como alguien que quiere logearse en feis pero no puede
#el bucle se repetirá hasta que ponga bien su cuenta y la dejen pasar

#empezaremos por el bucle for, su sintaxis es:
#for variable in elemento a recorrer 
# acá van las lineas de codigo que repetirá el bucle (cuerpo del bucle)

for i in [0,1,3]:
    print(i+2)

for x in range(5): 
    print("valor de x: " + str(x))

for gerson in ["primavera","otoño","invierno"]:
    print("H")
#Esto nos dice que cuando gerson="primavera" entonces se imprima la letra H y asi para
#gerson=otoño, gerson=invierno
#Notemos que el anterior bucle nos hace un salto de linea, si queremos 
#escribir todo en la misma linea podemos usar el codigo end
#end le dice al codigo que hacer luego de imprimir

for nay in [1,2,3,4]:
    print("Gerson", end="0") #acá le decimos que le luego de imprimir Gerson, coloque un cero

#En phyton cuando un for se encuentra con un str lo recorre de caracter a caracter

for i in "ABCDE":
    print(i) #i toma el valor de A,B,C y D

#Ahora crearemos una variable booleana
email=False
#vamos a hacer un programa que pida un correo y que reconozca si tiene o no @
#si no lo tiene el correo será erroneo
#si sí lo tiene el correo estará bien

for correo in input("Coloque su correo: "):
    if correo=="@":
        email=True
if email==True:
    print("Email es correcto")
else:
    print("email es incorrecto")
#acá iniciamos la variable correo como falso
#si en el correo que colocamos hay una @
#entonces correo es iguala a true
#Recordemos que for recorre todo el imput letra por letra
#si correo es true se imprime...
#si queremos que aparte @ se cumpla el punto, podemos usar if(correo=="@" and correo==".")

#Por ultimo veremos más acerca de range:
#range(no del q empezamos a contar, no al que llegaremos, de cuanto en cuanto)
for u in range(1,100,2):
    print(u)