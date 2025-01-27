#Defino las variables
cuentaTotal = 0
i = 0
#Muestro el menú
print("MENÚ")
print("Se cuenta con tres tipos de helados: ")
print("Pequeño [1]")
print("Mediano [2]")
print("Grande [3]")

helados = ["Pequeño,", "Mediano", "Grande"]
toppings = ["Chocolate", "Chispas", "Frutas"]
preciosHelados = [5000, 8000, 10000]
precioToppings = [1500, 2000, 3000]
cantHelados = [0,0,0]
cantToppings = [0,0,0]
totalHelados = [0,0,0]
totalToppings = [0,0,0]


while not(mandartodopalaM):


    finalizar = False #Bucle para identificar y rechazar las respuestas inválidas
    while not(finalizar):
        tipoHelado = int(input("Indique qué tipo de helado desea: "))
        if  tipoHelado > 3 or tipoHelado < 1:
            print("Respuesta Inválida")
        else:
            if tipoHelado == 1:
                cuentaTotal += preciosHelados[0]
                cantHelados[0] += 1
                totalHelados[0] += preciosHelados[0]
                finalizar = True
            elif tipoHelado == 2:
                cuentaTotal += preciosHelados[1]
                cantHelados[1] += 1
                totalHelados[1] += preciosHelados[1]
                finalizar = True
            elif tipoHelado == 3:
                cuentaTotal += preciosHelados[2]
                cantHelados[0] += 1
                totalHelados[2] += preciosHelados[2]
                finalizar = True

    finalizarChocolate = False
    while not(finalizarChocolate): #Bucle para identificar y rechazar las respuestas inválidas
        adiChocolate = str(input("Desea adicionar chocolate? [S/N]")).upper()
        if adiChocolate != "S" and adiChocolate != "N":
            print("Respuesta Inválida")
        else:
            if adiChocolate == "S":
                cuentaTotal += precioToppings[0]
                cantToppings[0] += 1
                totalToppings[0] += precioToppings[0]
                finalizarChocolate = True
            if adiChocolate == "N":
                finalizarChocolate = True

    finalizarChispas = False
    while not(finalizarChispas): #Bucle para identificar y rechazar las respuestas inválidas
        adiChispas = str(input("Desea adicionar chispas? [S/N]")).upper()
        if adiChispas != "S" and adiChispas != "N":
            print("Respuesta Inválida")
        else:
            if adiChispas == "S":
                cuentaTotal += precioToppings[1]
                cantToppings[1] += 1
                totalToppings[1] += precioToppings[1]
                finalizarChispas = True
            if adiChispas == "N":
                finalizarChispas = True


    finalizarFrutas = False
    while not(finalizarFrutas): #Bucle para identificar y rechazar las respuestas inválidas
        adiFrutas = str(input("Desea adicionar frutas? [S/N]")).upper()
        if adiFrutas != "S" and adiFrutas != "N":
            print("Respuesta Inválida")
        else:
            if adiFrutas == "S":
                cuentaTotal += precioToppings[2]
                cantToppings[2] += 1
                totalToppings[2] += precioToppings[2]
                finalizarFrutas = True
            if adiFrutas == "N":
                finalizarFrutas = True


        #Finalizar todo
    finalizarOrdenVarias = False
    while not(finalizarOrdenVarias):
        ordenVarias = input("Desea Pedir Otro Helado? [S/N]").upper()
        if ordenVarias != "S" and ordenVarias != "N":
            print("Respuesta Inválida")
        else:
            if ordenVarias == "S":
                pass
            if ordenVarias == "N":
                mandartodopalaM = True


    #-----------------------------------------------------------------------------------


    finalizarPropina = False
    while not(finalizarPropina):
        adiPropina = input("Desea agregar propina? [S/N]").upper()
        if adiPropina != "S" and adiPropina != "N":
            print("Respuesta Inválida")
        else:
            if adiPropina == "S":
                cuentaTotal = cuentaTotal + 0.1*cuentaTotal
                finalizarPropina = True
            if adiPropina == "N":
                finalizarPropina = True

    finalizarDevuelta = False
    while not(finalizarDevuelta):
        print(f"Su total es {cuentaTotal}")
        cobro = int(input(f"Con cuánto cancela? "))
        if cobro < cuentaTotal:
            print("Respuesta Inválida")
        else:
            devuelta = cobro - cuentaTotal
            if devuelta == 0:
                print("Gracias por su compra")
            else:
                print("Su devuelta es de: ", devuelta)
                finalizarDevuelta = True
    #Cuantos helados, cuantos topings y cuanto se recaudó por cada uno



            





