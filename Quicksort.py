#funcion encargada de ordenar los elementosa izquierda o derecha basandose en el elemento de referencia
def dividir_lista(lista, primera_posicion, ultima_posicion):

#eleccion del elemento de referencia, en este caso el ultimo elemento de la lista
  numero_referencia = lista[ultima_posicion]

#iterador utilizado para reordenar la lista
  i = primera_posicion - 1

#Ciclo que recorre los elemntos de la lista 
  for j in range(primera_posicion, ultima_posicion):

    #comparar el elemento actual con la referencia y de ser verdadera la comparacion intercambia la posicion del elemnto actual con la del iterador anterior
    if lista[j] <= numero_referencia:

      i = i + 1
      #intercambio de posciones
      (lista[i], lista[j]) = (lista[j], lista[i])
      print(lista)

  (lista[i + 1], lista[ultima_posicion]) = (lista[ultima_posicion], lista[i + 1])

  return i + 1

#funcion de ordenamiento rapido
def quickSort(lista, primera_posicion, ultima_posicion):
  
  if primera_posicion < ultima_posicion:

    posicion_intercambiar = dividir_lista(lista, primera_posicion, ultima_posicion)

    quickSort(lista, primera_posicion, posicion_intercambiar - 1)

    quickSort(lista, posicion_intercambiar + 1, ultima_posicion)


lista_datos = [8, 7, 2, 1]
print(lista_datos)

tamaño_lista = len(lista_datos)

quickSort(lista_datos, 0, tamaño_lista - 1)

print("Lista de datos ordenados")
print(lista_datos)