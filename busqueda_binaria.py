def busqueda_binaria(lista, buscado):
    pasos = 0
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        pasos +=1
        medio = (inicio + final) // 2
        if lista[medio] == buscado:
            return medio
        elif lista[medio] < buscado:
            inicio = medio + 1
        else:
            final = medio - 1

    return None


lista_numeros = []
for i in range(20):
    lista_numeros.append(i)

buscado = 12

resultado = busqueda_binaria(lista_numeros, buscado)

if resultado == None:
    print(f'El elemento {buscado} no se encuentra en la lista')
else:
    print(f'El elemento {buscado} se encuentra en la posición {resultado}')
        
    
    

