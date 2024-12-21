#En este archivo vamos a utilizar decoradores
#Con parametros

def decorador(funcion_parametro):
    def funcion_interior(*args,**kwargs):
       
        print("vamos a realizar un calculo: ")
        funcion_parametro(*args,**kwargs) 
        print("Hemos terminado el calculo: ")
    return funcion_interior #return de decorador
@decorador
def suma(num1,num2):
    print(num1+num2)
    
@decorador
def resta(num1,num2):
    print(num1-num2)
    
suma(1,2)
resta(3,2)

@decorador
def potencia(base,exponente):
    print(pow(base,exponente))

potencia(int(input("numero 1: ")),int(input("numero 1: ")))

#otro ejemplo

import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"La función '{funcion.__name__}' tomó {tiempo_transcurrido:.2f} segundos en ejecutarse.")
        return resultado
    return envoltura

@medir_tiempo
def proceso():
    # Simular un proceso que tarda un tiempo aleatorio
    time.sleep(2)
    print("¡Proceso completado!")

# Llamada al proceso decorado
proceso()
