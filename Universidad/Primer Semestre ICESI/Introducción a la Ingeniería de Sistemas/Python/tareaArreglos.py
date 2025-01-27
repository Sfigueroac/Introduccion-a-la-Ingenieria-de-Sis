import random

i = 0
numeros = []
while i < 15:
    numeros.append(random.randint(15, 35))
    i += 1

print(f"La primera lista es {numeros}")

while len(numeros) != len(set(numeros)):
    numeros = list(set(numeros))  
    faltantes = 15 - len(numeros)  
    while faltantes > 0:
        nuevo_numero = random.randint(15, 35)
        if nuevo_numero not in numeros: 
            numeros.append(nuevo_numero)
            faltantes -= 1

print(f"La segunda lista es {numeros}")
