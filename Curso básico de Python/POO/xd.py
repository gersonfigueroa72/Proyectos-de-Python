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