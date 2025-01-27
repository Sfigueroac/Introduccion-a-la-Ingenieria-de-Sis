"""
Ejercicio estructuras repetitivas
Solicitar un número al usuario. Mostrar los números del 1 hasta el número ingresado por el usuario. Decir cuántos números pares hay entre el 1 y el número ingresado por el usuario. Decir cuánto suman los números impares entre el 1 y el número ingresado por el usuario.
Hacer este ejercicio con cada una de las estructuras repetitivas con su respectiva
prueba de escritorio.
"""
def cicloBacanoWhile(): #Función para hacer el ciclo con el While
    sumaDeImpares = 0 #Definición de la suma de impares
    contadorDePares = 0 #Variable para la suma de pares
    i = 0
    numero = int(input("Ingrese el número: "))
    while i < numero:
        i += 1
        print(i)
        if i % 2 == 0:
            contadorDePares += 1#Cada que se realiza el ciclo y el número es par, se suma uno
        else:
            sumaDeImpares += i # Cada que se realiza el ciclo y el número es impar, se suma el mismo contador
    print(f"Hay {contadorDePares} pares de 1 a {numero}")
    print("La suma de impares es", sumaDeImpares)
def cicloBacanoFor():
    sumaDeImpares = 0
    contadorDePares = 0
    i = 1
    numero = int(input("Ingrese el número: "))
    for i in range (i , numero + 1):
        if i % 2 == 0:
            contadorDePares += 1 
        else:
            sumaDeImpares += i 
    print(f"Hay {contadorDePares} pares de 1 a {numero}")
    print("La suma de impares es", sumaDeImpares)
def cicloBacanoDoWhile():
    sumaDeImpares = 0
    contadorDePares = 0
    i = 1
    numero = int(input("Ingrese el número: "))
    while True:
        i += 1
        print(i)
        if i % 2 == 0:
            contadorDePares += 1
        else:
            sumaDeImpares += i
        if i == numero:
            break
    print(f"Hay {contadorDePares} pares de 1 a {numero}")
    print("La suma de impares es", sumaDeImpares)
def menu():
    end = False
    while not(end):
        print("[1] Para Realizar la actividad con ciclo while")
        print("[2] Para Realizar la actividad con ciclo For")
        print("[3] Para Realizar la actividad con ciclo DoWhile")
        print("[4] Para salir")
        opc = int(input("Digita su opción: "))
        if (opc==1):
            cicloBacanoWhile()
        elif(opc==2):
            cicloBacanoFor()
        elif(opc == 3):
            cicloBacanoDoWhile()
        elif(opc == 4):
            end = 1
        #elif(opc==3):
        
menu()


