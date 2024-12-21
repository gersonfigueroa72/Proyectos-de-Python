#Mostrar los números multiplos 
#de 5, menores a 
for i in range(1,50):
    if i*5<=50:
        print(5*i)
    else:
        pass

#Ahora mostraremos la suma de los números 
#de 5 en 5 hasta el 50
cota=50/5
sumar=0 #debemos iniciarlizar suma acá,
#ya que sino no estará definida
for x in range(0,10):
    sumar= 5*x+sumar
print("la suma es ", sumar)

#Ahora haremos esto mismo con else
contador=0
suma=0
while contador < 50:
    suma= suma + contador #0+0
    contador += 5
print("La suma es:", suma)
#Esto sucede porque el while se repite hasta 
#que la condicion no se cumpla

#Mostrar la tabla de multiplicar del número 7
y=0
while y<=70:
    print(y)
    y+=7

#Otra forma de hacerlo:
inicio=1
tabla=7
while inicio<=10:
    resultado=inicio*tabla
    print(tabla,"*",inicio,"=",resultado)
    inicio+=1