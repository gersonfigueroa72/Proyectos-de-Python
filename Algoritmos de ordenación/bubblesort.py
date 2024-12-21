'''
El ordenamiento burbuja itera en cada elemento de una lista, viendo si el elemento a la derecha
es mayor o menor.
Este ordenamiento es de menor a mayor 
'''

arr=[2,6,3,2,5,4,8,9,151,213,5,48]

band= False
while band==False:
    band=True
    for i in range(len(arr)-1): #No tiene caso que lo hagamos para toda la longitud de 
#arr, debido a que el ultimo elemento no tendra nada a la derecha
        if arr[i]>arr[i+1]:
            aux=arr[i] #aux, nos servirá a guardar la variable, ya que como arr[i]=arr[i+1]
#entonces, esta variable se perderá si no la guardamos
            arr[i]=arr[i+1]
            arr[i+1]=aux
            band= False
print(arr)