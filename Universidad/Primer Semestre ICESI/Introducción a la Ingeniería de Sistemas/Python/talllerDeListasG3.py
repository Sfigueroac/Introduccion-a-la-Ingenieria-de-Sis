"""
Ejercicio 1: Operaciones básicas con listas.
• Definir una lista, solicitando al usuario el tamaño o cantidad de elementos que almacenará. (En otras
palabras, se debe solicitar el tamaño del grupo de estudiantes)
• Ingresar datos a una lista (solicitando los elementos (edades) al usuario o generando de forma
aleatoria números entre 15 y 45)
• Listar o mostrar el contenido de la lista indicando que elemento se encuentra almacenado en cada
posición.
• Buscar un dato en una lista, es decir, solicitar al usuario un valor (edad) y verificar si dicho valor se
encuentra almacenado en la lista, en cuyo caso debe indicar la posición(es) en la que fue hallado. En
caso de que la edad buscada no esté en la lista, dar un mensaje indicando que no fue encontrada la
edad en la lista.
• Reemplazar un dato en una lista, es decir, se solicita una edad al usuario, esta se busca dentro del
lista y se cambia por otra edad que igualmente se solicita al usuario. Si la edad que se pretende
cambiar no está en la lista, debe indicar que no fue encontrada. 
"""

import random
def edadesEstudiantes():
    cantEstudiantes = int(input("Cuantos estudiantes tiene la lista?"))
    estudiantes = []
    nombres = []
    while True:
        aleatorio = int(input(" Si desea llenar la lista de edades de forma aleatoria Digite [1], si desea llenar la lista de edades de forma manual digite [2]"))
        if aleatorio == 1:
            i = 0
            while i < cantEstudiantes:
                i += 1
                estudiantes.append(random.randint(15, 45))
                nombre = input(f"Ingrese el nombre del estudiante {i}: ")
                nombres.append(nombre)
            break
        elif aleatorio == 2:
            i = 0
            while i < cantEstudiantes:
                i += 1
                estudianteNuevo = int(input(f"Ingrese la edad del estudiante {i}"))
                estudiantes.append(estudianteNuevo)
                nombre = input(f"Ingrese el nombre del estudiante {i}: ")
                nombres.append(nombre)
            break
        else:
            print("Digite un número válido")
        
        #Mostrar el contenido
    print("Las edades de los estudiantes son: ")
    for i in range(cantEstudiantes):
        print(f"Posición {i}: {estudiantes[i]}")


        #Buscar un dato
    edad_a_buscar = int(input("Ingrese la edad que desea buscar: "))
    posiciones = []
    for i, edad in enumerate(estudiantes):
        if edad == edad_a_buscar:
            posiciones.append(i)
    if posiciones:
        print(f"La edad {edad_a_buscar} fue encontrada en las posiciones: {posiciones}")
    else:
        print(f"La edad {edad_a_buscar} no fue encontrada en la lista.")



        #Reemplazar edades
    edadReemplazar = int(input("Ingrese la edad que desea reemplazar: "))
    if edadReemplazar in estudiantes:
        nuevaEdad = int(input(f"Ingrese la nueva edad que reemplazará a {edadReemplazar}: "))
        for i in range(len(estudiantes)):
            if estudiantes[i] == edadReemplazar:
                estudiantes[i] = nuevaEdad
        print(f"La edad {edadReemplazar} ha sido reemplazada por {nuevaEdad}.")
    else:
        print(f"La edad {edadReemplazar} no fue encontrada en la lista.")

    # Mostrar la lista actualizada
    print("La lista actualizada de edades es: ")
    for i in range(cantEstudiantes):
        print(f"Posición {i}: {estudiantes[i]}")

    # Encontrar la edad menor y su posición
    edadMenor = estudiantes[0]
    posicionMenor = 0
    for i in range(1, cantEstudiantes):
        if estudiantes[i] < edadMenor:
            edadMenor = estudiantes[i]
            posicionMenor = i
    
    print(f"El estudiante con menor edad es {nombres[posicionMenor]} con {edadMenor} años.")
    # Encontrar la edad mayor y su posición
    edadMayor = estudiantes[0]
    posicionMayor = 0
    for i in range(1, cantEstudiantes):
        if estudiantes[i] > edadMayor:
            edadMayor = estudiantes[i]
            posicionMayor = i
    print(f"El estudiante con mayor edad es {nombres[posicionMayor]} con {edadMayor} años.")    
#Usando estructuras repetitivas

    contadorMayoresEdad = 0
    sumatoriaMayoresEdad = 0 
    sumatoriaTotal = 0
    promedio = 0
    porcentajeMayores = 0
    for edad in estudiantes:
        if edad >= 18:
            contadorMayoresEdad += 1
            sumatoriaMayoresEdad += edad 
        sumatoriaTotal += edad
    promedio = sumatoriaTotal / cantEstudiantes
    porcentajeMayores = (contadorMayoresEdad*100)/cantEstudiantes
    print("La cantidad de mayores de edad es: ", contadorMayoresEdad)
    print("Las edades de los mayores de edad suman", sumatoriaMayoresEdad)
    print("La sumatoria de todas las edades es", sumatoriaTotal)
    print("El promedio de todas las edades es", promedio)
    print("El porcentaje de mayores de edad es", porcentajeMayores)

    # Profe, en serio un bubble sort? >:(
    #Profe con una función sort se solucionaba, me acabo de tirar 20 lineas cuando pudieron ser doooooos 
    while True:
        orden = int(input("Para ordenar de forma ascendente digite [1], para descendente digite [2]: "))
        
        if orden == 1:
            for i in range(cantEstudiantes):
                for j in range(0, cantEstudiantes-i-1):
                    if estudiantes[j] > estudiantes[j+1]:
                        estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]
                        nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
            print("Lista ordenada de forma ascendente: ")
            break
        elif orden == 2:
            for i in range(cantEstudiantes):
                for j in range(0, cantEstudiantes-i-1):
                    if estudiantes[j] < estudiantes[j+1]:
                        # Intercambiar las edades
                        estudiantes[j], estudiantes[j+1] = estudiantes[j+1], estudiantes[j]
                        # Intercambiar los nombres correspondientes
                        nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
            print("Lista ordenada de forma descendente: ")
            break
        else:
            print("Digite un número válido")

    # Mostrar la lista ordenada
    for i in range(cantEstudiantes):
        print(f"Estudiante: {nombres[i]} - Edad: {estudiantes[i]}")

edadesEstudiantes()
        


