#Condicional if (repaso)
def evaluacion(nota):
    valoracion="aprobado"
    if nota<6:
        valoracion="reprobado"
    return valoracion #le decimos que imprima valoración
print(evaluacion(7))
print(evaluacion(4))

#Ahora haremos un programa de evaluación de notas
#implementaremos el codigo input el cual nos permite poner valores en la consola
nota_alumno=input()
print(evaluacion(int(nota_alumno))) #usamos int para que el valor que tome la funcion sea un entero
#debido a que input solo recibe texto
#Para dejarle una nota de texto al usuario, para que sepa que tipo de dato se
#le está solicitando hacemos lo siguiente
nota_alumno_1=input("acá dejamos el mensaje") 
print(evaluacion(int(nota_alumno)))