''' Son funciones eque a su vez añaden funcionalidades
a otras funciones.
Decoran otras funciones.
'''
#Estructura de un decorador:
'''La estructura cuenta de 3 funciones que llamaremos 
A,B,C donde A recibe como parametro a B para devolver
C. Un decorador devuelve una función.

def funcion_decorador(funcion): #A
    def funcion_interna(): #B
        #codigo de la función interna
    return funcion_interna #C
'''
#################################################
#Primer ejemplo de sintaxis (no tiene utilidad):
def decorador(funcion_parametro):
    def funcion_interior():
        '''acá agregamos las acciones adicionales
        #en este caso dejaremos un mensaje para que
        la funcion sea mas entendible'''
        print("vamos a realizar un calculo: ")
        funcion_parametro() #le decimos que ejecute f
        print("Hemos terminado el calculo: ")
    return funcion_interior #return de decorador
#esta parte encerrada la agregamos de ultimo
##################################################
@decorador # con @ decoramos la funcion
def suma():
    print(15+20)
    
@decorador
def resta():
    print(30-10)

suma()
resta() #llamamos a las funciones

#Notemos que tenemos un programa complejo
#aunq ahorita solo tenemos funciones
#¿Qué pasa si quiere agregarle funcionalidades a las
#funciones

#Para un codigo largo esto sería muy dificil de hacer
#para esto introducimos los decoradores 
#Ahora definiremos una funcion decoradora en la 
#parte de arriba



