import random
def busqueda_Lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1
numeros = [0,2,3,4,6,7,1,8,10,9,15,12,11,14,13,16,19,17,18,5]

"""
for _ in range(20):
    numeros.append(random.randint(0,10))

"""

objetivo = 5

resultado = busqueda_Lineal(numeros, objetivo)

if resultado != -1:
    print(f"encontrado {objetivo} en la posicion {resultado}")
    print(numeros)
else:
    print(f"El numero objetivo no fue encontrado")
    print(numeros)