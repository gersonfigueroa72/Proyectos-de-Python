

lista=[8,5,6,5,212,54648,1]

def particionado(lista):
    pivote=lista[0]
    menores=[]
    mayores=[]

    for i in range(1, len(lista)): #0 no lo recorremos pq es el pivote
        if lista[i]<pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    
    return menores, pivote, mayores

def quicksort(lista):
    if len(lista)<2: #e.i que la lista solo puede tener 0 o 1 elemento
        return lista 
    menores,pivote,mayores=particionado(lista)
    return quicksort(menores)+ [pivote]+ quicksort(mayores)

print(quicksort(lista))
