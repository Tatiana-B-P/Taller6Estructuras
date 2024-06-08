def bubble_sort(lista):
    #tamaño lista de datos
    tamaño_lista = len(lista)
    #i representa la cantidad de posiciones ordenadas
    for i in range(tamaño_lista):
        #j nos permite realizar las comparaciones de los elementos adyacentes(continuos)
        for j in range(0, tamaño_lista-i-1):
            #se realiza la verificacion de si un dato es mayor a otro dato en la posicion adyacente y de ser asi se realiza el intercambio
            if lista[j] > lista[j+1]:
                primer_numero = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = primer_numero
# Dada una lista desordenada                
lista_datos = [9, 8, 7, 5, 4, 3, 0]

# La ordenamos utilizando bubble sort
bubble_sort(lista_datos)
print(lista_datos)
# [0, 3, 4, 5, 7, 8, 9]