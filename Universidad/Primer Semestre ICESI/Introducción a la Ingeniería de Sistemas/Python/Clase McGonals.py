#Caso hamburguesa Mc Gonals 
#Primer paso entradas (constante: son variables que no cambian su valor.)
sencilla = int(10000)
doble = int(15000)
triple = int(20000)
queso = int(2000)
pepinillos = int(1000)
tocineta = int(3000)
ptje_propina = float(0.1)
print("Menú Hamburguesa Mc Gonals")
print(" [1] Simple")
print(" [2] Doble")
print(" [3] Triple")
tipoHamburguesa = int(input(" Seleccine el tipo de hamburguesa: ")) #Entrada 

if tipoHamburguesa < 1 and tipoHamburguesa > 3:
    print(" Opción inválida")
else:

    if tipoHamburguesa == 1:
        totalCuenta = sencilla
    elif tipoHamburguesa == 2:
        totalCuenta = doble
    elif tipoHamburguesa == 3: 
        totalCuenta = triple
    adiQueso = str(input(" Desea adicion de queso?: s/n "))
    adiQueso = adiQueso.upper()
    if adiQueso == "S":
        totalCuenta = totalCuenta + queso 
    adiPepinillo = str(input(" Desea adicion de pepinillo?: s/n "))
    adiPepinillo = adiPepinillo.upper()
    if adiPepinillo == "S":
        totalCuenta = totalCuenta + pepinillos
    adiTocineta = str(input(" Desea adicion de tocineta?: s/n "))
    adiTocineta = adiTocineta.upper()
    if adiTocineta == "S":
        totalCuenta = totalCuenta + tocineta
    propina = str(input(" Desea agregar propina?: s/n "))
    propina = propina.upper()
    if propina == "S":
        totalPropina = totalCuenta * ptje_propina
        totalCuenta = totalCuenta + totalPropina
    print("El total de su cuenta es: ", totalCuenta)   
    pago = int(input("Con cuento desea pagar: "))
    if pago > totalCuenta:
        cambio = pago - totalCuenta
        print("Su cambio es: ", cambio)
    if pago == totalCuenta:
        print("Gracias por su compra!")
    if pago < totalCuenta:
        print("Le falta: ",totalCuenta - pago)
    


