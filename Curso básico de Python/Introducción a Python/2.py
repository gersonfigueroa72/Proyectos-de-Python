#vamos a profundizar en las funciones en phyton 
#una de las principales utilidades de las funciones será reutilizar un codigo, llamando a las funciones
#la sintaxis es la siguiente:
#def nombre_funcion(parametros):
#instrucciones de la funcion
#return (opcional)
def mensaje(): #notemos que esta funcion no recibe ningun argumento
    print("esta")
    print("es")
    print("la instrucción")
mensaje() #llamamos a la función en la consola poniendo su nombre

def fun(x): #esta función ya tiene un argumento
    print(3+x)
fun(3) #llamamos a la funcion con el argumento que queremos

def fun_2(y,w): #funcion con mas de un argumento
    print(y*w)
fun_2(5,2)

#Ahora aprenderemos a usar el return