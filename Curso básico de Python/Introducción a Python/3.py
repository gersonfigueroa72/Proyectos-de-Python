#En este archivo hablaremos de listas
#Estas son estructuras de datos que nos permiten guardar varios valores, como un vector o un conjunto.
#nombre_de_la_lista=[elem0,elem1,...], tambien podemos usar () pero mejor siempre usa []
lista_1=[1,5,"perro"] #el primer elemento de la lista simpre tiene el indice 0
print(lista_1)
print(lista_1[1])
print(lista_1[0], lista_1[2])
#nueva lista
lista_2=[5.3, 3+2, 9, "el gato", 555, 666,777]
print(lista_2[0:4]) #acá le decimos que llame a los valores del 0 al 4
#si quiero agregar un elemento a una lista utilizo el código 
#nombre_de_la_lista.append(elemento_nuevo)
lista_1.append("5") #agrega al nuevo elemento de ultimo
print(lista_1) #ahora vemos que ya hay un nuevo elemento    
#si quiero agregar el elemento en un indice especifico usamos:
#nombredelista.insert(indice, nuevo elemento)
lista_3=[1,2,3,4,5,6]
lista_3.insert(0,0)
print(lista_3)

#Si queremos agregar varios elementos usamos:
lista_4=["Gerson","Lorena"]
lista_4.extend(["Noé","Mel","Angel"]) #agrega estos elementos al final
print(lista_4)

#si queremos buscar en qué indice está algun elemento en especifico de la lista usamos:
print(lista_4.index("Mel")) #nos dirá que esta en el indice 3 (pq inicia desde el 0)

#si quiero saber si un elemento está en mi lista entonces uso:

print("Nacho" in lista_4) #me devolverá falso o verdadero, dependiendo si en la lista está el 
#elemento Nacho o no, en este caso da falso

#para eliminar un elemento de la lista uso:
lista_4.remove("Gerson")
print(lista_4) #ya no aparecera el elemento Gerson

#podemos sumar listas
lista_5=lista_1+lista_2
print(lista_5)

#podemos multiplicar la lista por un escalar y esto lo repetirá n veces
print(lista_5*3) #lista 5 repetida 3 veces
