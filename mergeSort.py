#lista de datos a ordenar
lista = [7, 9, 7, 7, 3, 1, 5]
#funcion que realiza la division de la lista de datos
def mergeSort(lista_principal):
    #caso base
    if len(lista_principal) == 1:
        return lista_principal
    #lista izquierda y derecha para almacenar la lista dividida
    lista_izquierda = []
    lista_derecha = []

    #division de las listas
    for i in range(0,len(lista_principal)):
        #asignacion lista izquierda
        if i < len(lista_principal)//2:
            lista_izquierda.append(lista_principal[i])
        #asignacion lista derecha
        else:
            lista_derecha.append(lista_principal[i])

    #recursividad para ordenar la lista izquierda
    lista_izquierda_ordenada = mergeSort(lista_izquierda)
    #recursividad para ordenar la lista derecha
    lista_derecha_ordenada = mergeSort(lista_derecha)
    #devolver la union ordenada de ambas listas
    return union(lista_izquierda_ordenada, lista_derecha_ordenada)

#funcion que une de manera ordenada la lista izquierda y derecha
def union(lista_izquierda, lista_derecha):
    lista_ordenada = []
    #odenamiento de los elementos entre la lista izquierda y derecha
    while len(lista_izquierda) > 0 and len(lista_derecha) > 0:
        if lista_izquierda[0] > lista_derecha[0]:
            lista_ordenada.append(lista_derecha[0])
            lista_derecha.pop(0)
        else:
            lista_ordenada.append(lista_izquierda[0])
            lista_derecha.pop(0)
    
    while len(lista_derecha) >0:
        lista_ordenada.append(lista_derecha[0])
        lista_derecha.pop(0)

    while len(lista_izquierda) >0:
        lista_ordenada.append(lista_izquierda[0])
        lista_izquierda.pop(0)
    
    return lista_ordenada
    
print(mergeSort(lista))