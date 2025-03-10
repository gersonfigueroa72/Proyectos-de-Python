"""
La idea de este programa, es verificar si dado un número entero, este es primo o no.
Para ello se realiza una división entre todos los números enteros menores al número ingresado.
Haremos una lista de divisores de ese número, si la lista tiene más de dos elementos, 
el número no es primo.
"""
n=int(input("Ingrese un número entero: "))
m=n #guardamos el valor de n en m para usarlo en la función factores_primos
def primo(n):
    global divisores #para que la variable divisores pueda ser usada en la función factores_primos
    divisores=[]
    for i in range(1,n+1): #range empieza en 0 y termina en n-1, por eso se suma 1
        if n%i==0:
            divisores.append(i)
    if len(divisores)>2:
        print("El número no es primo")
    else:
        print("El número es primo")
    return print(f"Los divisores de {n} son \n {divisores}")
primo(n)

# Dado este número, tambien hallaremos su descomposición en factores primos

def factores_primos(n):
    if len(divisores)==2:
        print(f"No tiene factores primos, ya que el número {n} es primo")
    else:
        factores=[]
        for i in range(2,n): #empezamos en 2 ya que el 1 no es primo
            #y terminamos en n ya que range termina en n-1 y n no es primo
            while n%i==0: #verifica el minimo divisor de n
                factores.append(i)
                n=n//i #actualiza el valor de n a n/i
        return print(f"Los factores primos de {m} son \n {factores}")

factores_primos(n)