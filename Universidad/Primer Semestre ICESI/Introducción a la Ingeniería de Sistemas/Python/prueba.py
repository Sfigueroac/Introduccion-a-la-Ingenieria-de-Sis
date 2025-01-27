numero = int(input("Digite el número: "))
for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        print(f"{numero} No es primo")
    else:
        print(f"{numero} es primo")