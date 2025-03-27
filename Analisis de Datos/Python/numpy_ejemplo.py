import numpy as np

vector = np.array([1,2,3])
print(vector)

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)

#sumar listas vs sumar arrays

lista1 = [1,2,3]
lista2 = [4,5,6]
vec1 = np.array(lista1)
vec2 = np.array(lista2)

print(lista1 + lista2)
print(vec1 + vec2)

#Podemos crear matrices como

matriz1 = np.array([[1,2],[3,4],[5,6]]) #3x2
matriz2 = np.array([[1,2,3],[4,5,6]]) #2x3

#Si queremos crear una matriz nxm donde los elementos vayan de 0 a i tenemos:

matriz3 = np.arange(12).reshape(3,4) #matriz del 0 al 11 3x4 

#Si queremos crear una matriz vacia (de ceros) usamos:

matriz4 = np.zeros((3,4)) #matriz de ceros 3x4

#Si queremos saber la dimension de una matriz usamos:
print(matriz4.shape)

#Tambien podemos saber si la matriz es unidimensional (vector) o bidimensional (matriz)
#tridimensional (tensor) etc. Usando:

print(matriz4.ndim)

#El mumero total de elementos de una matriz se obtiene con:

print(matriz4.size)

#Podemos crear matrices equiespacidas con linspace

matriz5=np.linspace(1,100,10).reshape(2,5) #Matriz 2x5, del 1 al 100 con 10 elementos equiespacidos
print(matriz5)

#Para crear matrices en 3 dimensiones usamos

matriz6 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])

print(matriz6) #Matriz 2x3x3

#Otra forma podría ser

matriz7 = np.arange(24).reshape(2,3,4) #Matriz 2x3x4
print(matriz7)

#Podemos acceder a los elementos de una matriz con
print(matriz7[1,2,3]) #Elemento 1,2,3 (contando desde el cero)


#Podemos ordenar una matriz de forma ascendente como:

matriz8=np.array([54,52,1,54,654,87,8,5,2,4,87,8454])
print(np.sort(matriz8)) 

#Si queremos elevar cada entrada de una matriz a una potencia usamos

print(np.power(matriz5,2))


#Podemos hacer operaciones logicas con matrices
print(np.array(matriz8<=100)) 

#Para hallar el valoro maximo y minimo de una matriz podemos usar

print(np.max(matriz8))
print(np.min(matriz8))

#Si queremos combinar dos matrices podemos usar

m1=np.arange(12).reshape(3,4)
m2=np.arange(12,27).reshape(3,5)
print(np.concatenate((m1,m2),axis=1)) #Concatenar por columnas
