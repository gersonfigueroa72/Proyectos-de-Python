''' En este apartado aprenderemos la utilización de
*args y **kwargs.
primero que todo tanto args como kwargs no son variables
reservadas en phyton, es mas una convención entre 
programadores. Lo que sí aprenderemos a utilizar será
* o ** 
'''
#Empezaremos viendo el uso de *args 
'''
El principal uso de *args y **kwars es en la definición
de funciones. Ambos permiten pasar un número variable
de argumentos a una función, por lo que sí quieres 
definir una función cuyo número de parametros será variable
podemos utilizar esta opción.
A continuación veremos un ejemplo del uso de args
'''
def test_var_args(f_arg, *argv):
    print("Primer argumento normal: ", f_arg)
    for arg in argv:
        print("argumentos de *argv: ", arg)

test_var_args("phyton", "xd", 'xdd')
#Uso de kwargs
'''
Kwargs nos permite pasar argumentos de longitud variable
asociados con un nombre o key (de diccionario),
ejemplo de su uso:
'''

def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0}={1}".format(key, value))

saludame(nombre="Gerson")