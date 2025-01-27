"""
1.	Llenar una lista de forma automática con números enteros, recibiendo como parámetros una lista vacía, el número de elementos que contendrá la lista, el límite inferior del rango de números a generar y el límite superior del rango de números a generar 
2.	Mostrar el contenido de una lista indicando la posición de cada elemento.
3.	Ordenar una lista de forma ascendente
4.	Ordenar una lista de forma descendente
5.	Determinar si un número es par, recibiendo un número y devolviendo una variable booleana (True/False) 
6.	Determinar si un número es primo, recibiendo un número y     devolviendo una variable booleana (True/False) 
7.	Recibir una lista y devolver otra lista con los números pares de la lista original
8.	Recibir una lista y devolver otra lista con los números impares de la lista original
9.	Recibir una lista y devolver otra lista con los números primos de la lista original
------------------------------------------------------------------------------------------------------------
1.	Generar una lista de números, con 15 elementos entre 10 y 40
2.	Mostrar el contenido de lista números
3.	Extraer de la lista de números los pares y almacenarlos en otra lista
4.	Mostrar la lista de números pares  
5.	Extraer de la lista de números los impares y almacenarlos en otra lista
6.	Mostrar la lista de números impares
7.	Extraer de la lista de números los primos y almacenarlos en otra lista
8.	Mostrar la lista de números primos  
9.	Ordenar de forma ascendente la lista de números pares
10.	Ordenar de forma descendente la lista de números impares
11.	Ordenar de forma ascendente la lista de números primos

"""

import random
lista = []
cantElementos = 6
limInferior = 1
limSuperior = 6

def llenadoDeLista(lista, cantElementos, limInferior, limSuperior):
    i=0
    while i < cantElementos:
        agregar = random.randint(limInferior, limSuperior)
        lista.append(agregar)
        i += 1
    print(lista)
    return lista
llenadoDeLista(lista, cantElementos, limInferior, limSuperior)

def mostrarElContenido(lista):
    i = 0
    while i < len(lista):
        i +=1 
        print(f"Posición {i}" , lista[i-1])
        
mostrarElContenido(lista)

def ordenarListaAscendente(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)
    return lista
ordenarListaAscendente(lista)

def ordenarListaDescendiente(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(lista)
    return lista
ordenarListaDescendiente(lista)

numero = 2
def esParBool(numero):
    if numero % 2 == 0:
        espar = True
    else:
        espar = False

    return espar


def esPrimoBool(numero):
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            esPrimo = False
        else:
            esPrimo = True
    return esPrimo

def discriminarPares(lista):
    listapar = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            listapar.append(lista[i])
        i+=1    
    print(listapar)
discriminarPares(lista)


#8.	Recibir una lista y devolver otra lista con los números impares de la lista original

def discriminarImpares(lista):
    listaimpar = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            pass
        else:
            listaimpar.append(lista[i])
        i+=1    
    print(listaimpar)
discriminarImpares(lista)

#9.	Recibir una lista y devolver otra lista con los números primos de la lista original

def discriminarPrimos(lista):
    listaprimos = []
    j = 0
    while j < len(lista):
        for i in range(2, int(lista[j]**0.5) + 1):
            if lista[j] % i == 0:
                pass
            else:
                listaprimos.append(lista[j])
        j += 1
    print (listaprimos)
discriminarPrimos(lista)
        
