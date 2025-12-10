#en este video ahondaremos en el tema de las tuplas
#las tuplas son listas que no se pueden modificar despues de su creación
#tampoco permiten que busquemos entre sus elementos (index)
#la ventaja de estas es que optimizan el codigo al ser inmutables 
tupla_1=(1,2,3,4,5)
print(tupla_1)
tupla_2=(6,7,8)

#se pueden sumar
tupla=tupla_1+tupla_2
print(tupla)

#para convertir una tupla a una lista usamos:
#nombre_de_la_lista=list(nombre_de_la_tupla)
lista_1=list(tupla_1)

#para convertir una lista en un tupla usamos tuple
lista_2=[9,8,4,5]
tupla_2=tuple(lista_2)

#contar los elementos de una tupla:
print(tupla_2.count(9)) #nos dirá que el elemento 9 solo se encuentra una vez

#saber la longitud de una tupla
print(len(tupla)) #nos dirá que tiene 8 elementos

#si queremos asignarle una variable a la tupla podemos hacer lo siguiente:
(a,b,c,d,e)=tupla_1
print(b) #nos devuelve el valor de 2 para b ya que es el lugar que tiene en la tupla_1
