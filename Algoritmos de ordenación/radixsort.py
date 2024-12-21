
def radixsort(lista):
    n=0 #n es el maximo # de digitos q tiene algun elemento de la lista
    for j in lista:
        if len(j)>n:
            n=len(j)
#ahora haremos una función que nos permitirá igualar la cantidad de n digitos
#a todos los elementos de la lista (agregando ceros)
    for i in (0, len(lista)):
        while len(lista[i])<n:
            lista[i]="0"+lista[i]

#Ahora si podemos pasar a la tarea principal de nuestro algoritmo
    for e in range(n-1,-1,-1):
        grupos=[[] for i in range(10)]
        for i in range(len(lista)):
            lista