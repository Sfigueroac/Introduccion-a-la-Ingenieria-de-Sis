
import random
"""
9. ¡Rifa! El sistema debe generar un número aleatorio entre 1 y 10, luego le dará 3 oportunidades al jugador para adivinar qué número se generó. Si el jugador no acierta el sistema debe informar cual fue el número generado.
"""
def rifa():
    i = 0
    balotas = (random.randint(1,10))
    ganaste = False
    while i < 3:
        while True:
            tiquete = int(input("Ingrese un número del 1 al 10: "))
            if 1 <= tiquete <= 10:
                break
        i += 1 
        intento = 3 - i
        if tiquete == balotas:
            ganaste = True
            print("GANASTE!")
            break
        else:
            print(f"Te quedan {intento} intentos")

        if i == 3 and ganaste == False:
            print(f"El número era {balotas}")
            print("PERDISTE")

"""
12. Escriba un programa que pida un número, y si no está en el rango [m, n] lovuelva a pedir, y que repita este proceso hasta que el usuario ingrese un valordentro del rango [m, n].
"""
def validar():
    while True:
        valor = int(input("Ingrese un número del 1 al 15"))
        if 1 <= valor <= 15:
            break

"""
14. Escriba un programa que le pida un número y determine si este es primo. Recuerde que un número es primo si solo es divisible por él y por la unidad, en caso contrario no es primo. Tip: La cantidad de divisores de un número primo es igual a 2.
"""


def es_primo():
    numero = int(input("Digite el número: "))
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} No es primo")
        else:
            print(f"{numero} es primo")

"""
15. Crea un programa que invierta el orden de las cifras de un número utilizando divisiones sucesivas entre 10. Tip: Si al hacer la división entre 10 el cociente es igual a cero (0) se habrá encontrado la cifra de las unidades…
"""
def divisionesSucesivasProfePorDiosQueEsEsto():
    numero = float(input("Digite un número: "))
    while numero >= 1:
        numero = numero / 10
    print((numero))

"""
17. Una compañía paga semanalmente $500000 a sus vendedores, más una comisión del 9% sobre el total de ventas realizadas por cada uno. Elabore un programa que solicite al usuario el total de ventas de cada vendedor, calcule el pago correspondiente y, al finalizar, muestre el monto total pagado a todos los vendedores, la cantidad de vendedores que recibieron pago y cuántos de ellos recibieron un pago superior a $800,000.
"""
def calcularPagoProfeQueEjercicioTanDificil():
    salario_semanal = 500000  
    comision = 0.09 
    vendedores = []
    total_pagado = 0
    pago_superior_a_800000 = 0
    while True:
        ventas = float(input("Ingrese el total de ventas del vendedor (o 0 para finalizar): "))
        if ventas == 0:
            break
        pago = salario_semanal + (ventas * comision)
        vendedores.append(pago)
        total_pagado += pago
        if pago > 800000:
            pago_superior_a_800000 += 1
    print("\n--- Resultados ---")
    print(f"Total pagado a todos los vendedores: ${total_pagado:.2f}")
    print(f"Cantidad de vendedores que recibieron pago: {len(vendedores)}")
    print(f"Vendedores que recibieron un pago superior a $800,000: {pago_superior_a_800000}")


"""
19. En un supermercado un ama de casa pone en su carrito los artículos que va tomando de los estantes. La señora quiere asegurarse de que el cajero le cobre bien lo que ella ha comprado, por lo que cada vez que toma un artículo anota su precio junto con la cantidad de artículos que ha tomado y determina cuánto dinero gastara en ese artículo; a esto le suma lo que ira gastando en los demás  artículos, hasta que decide que ya tomo todo lo que necesitaba. Ayúdale a esta señora a obtener el total de sus compras
"""
def supermercado():
    control = False
    cuentaTotal = 0
    while control == False:
        anadirArticulo = input("Desea añadir otro artículo? [S/N]").upper()
        if anadirArticulo == "S":
            cantidadArticulos = int(input("Cuantas unidades de este mismo artículo lleva? "))
            valor = int(input("Digite el valor de este artículo: "))
            cuentaTotal += valor * cantidadArticulos
        elif anadirArticulo == "N":
            break
        else:
            print("Valor Inválido")
    
"""
20. Para ingresar al curso de Estudio de suelos se realizó un examen clasificatorio. Se tienen los resultados de dicho examen por aspirante (una nota comprendida entre 0.0 y 5 0). Se desea saber cuántos aspirantes aprobaron el examen, cuántos lo perdieron (nota menor que 3.0) y cuál fue el promedio de todo el grupo de aspirantes. No sabemos cuántos aspirantes son, pero sabemos que cuando se quiera indicar que se finalizó el ingreso de notas se digitará un valor negativo.
"""
def aspirantes():
    aspirantesTotales = input("Cuantos aspirantes hay: ")
    i = 0
    promedio = 0
    while aspirantesTotales > i:
        i += 1
        nota = int(input(f"Digite la nota del aspirante{i}"))
        promedio += nota
        
