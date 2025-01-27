"""
Actividad Propuesta:
• Simula un bucle do-while que imprima cinco veces la palabra "Python".
• Simula un bucle do-while que imprima los números del 5 al 1 (en orden descendente).
"""
def whileTruePy():
    i = 1
    while True:
        print("Python")
        i += 1
        if i > 5:
            break
def whileTrueDes():
    numero = 5
    while True:
        print(numero)
        numero -= 1
        if numero == 0:
            break

"""
Actividad Propuesta:
• Escribe un bucle for que imprima cinco veces la palabra "Python".
• Escribe un bucle for que imprima los números del 5 al 1 (en orden descendente)
"""

def forPy():
    i = 1
    for i in range (1,6):
        print("Python")

def forDesc():
    i = 5
    for i in range (5,0,-1):
        print(i)

"""
Actividad Propuesta:
• Escribe un bucle while que imprima cinco veces la palabra "Python".
• Escribe un bucle while que imprima los números del 5 al 1 (en orden descendente).
"""

def whilePy():
    i=1
    while i <= 5:
        print("Python")
        i += 1

def whileDesc():
    i = 5
    while i > 0:
        print(i)
        i -= 1


def menu():
    end = False
    while not(end):
        opc = int(input("Opción:"))
        if (opc==1):
            whileTruePy()
        elif(opc==2):
            whileTrueDes()
        elif(opc==3):
            forPy()
        elif(opc==4):
            forDesc()
        elif(opc==5):
            whilePy()
        elif(opc==6):
            whileDesc()

        elif(opc == 7):
            end = 1
menu()