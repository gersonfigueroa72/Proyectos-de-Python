#Este programa nos ayuda a determinar si un
#número es o no par.
#número%2==0 nos dice que el número que ingresemos
#al programa se comprobará por medio del operador
# == que el resto sea igual a 0, ya que == compara
#que dos o mas cantidades sean iguales
#a diferencia de !=
#si son iguales dará true (par) y false para impar
numero=int(input("Ingrese el número "))
print(numero%2==0)
############################################
suma=0
num=int(input("introduzca el número "))
while num!=0:
    suma+=num
    num=int(input("Intruzca el número "))
print("La suma de los números ingresados es: ",suma)
#Este es un programa que nos pide ingresar números
#para ser sumados, la condicion es que el numero
#no sea igual a cero, sino se termina la suma.

#############################################

cantidad=0
n=int(input("Numero "))
while n>0 and n%10!=0:
    cantidad=cantidad+1
    n=int(input("Numero "))
print(cantidad)

#Este programa nos da la cantidad de números 
#que no sean multiplos de 10 que ingresemos

###########################################

def cantidadDigitos(numero_1):
    cantidad_1=0
    while numero_1!=0:
        cantidad_1=cantidad_1+1
        numero_1=numero_1//10
    return cantidad_1
print("La cantidad es de dígitos es: "
      ,cantidadDigitos(1534))

#Ese programa es una funcion destinada a contar 
#la cantidad de digitos de un número.
#Esto lo hace mediante a la division entera //
#Si nosotros metemos un número_1=15
#este será dividido entre 10 y regresará el valor 
#entero, sumandi así un 1 en cantidad_1
#luego el while se volvera a ejecutar hasta que
#la division entera sea 0

############################################

mayor=-1
n=int(input("Número positivo: "))
while cantidadDigitos(n)%3!=0:
    if n>mayor:
        mayor=n
    n=int(input("Número positivo: "))
print("Mayor número ingresado",mayor)

'''Este programa nos da el número mayor que hemos
ingresado, siempre que el número sea +, para ello
iniciamos asignando en memoria el número mayor 
-1, para que cualquier número mayor a este, tome 
su lugar en la memoria del programa.
La condicion del While es que no podemos meter 
números con cantidad de digitos multiplos de 3
ejem: 545, 965123, etc
sin embargo para números diferentes a este
el codigo toma el número y en un inicio ve que sea
mayor a -1, si lo es entonces este número se guarda
en memoria es lugar de mayor, y así sucesivamente
'''