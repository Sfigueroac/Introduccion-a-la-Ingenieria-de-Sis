#El restaurante Mc Gonals le ha pedido que desarrolle un programa para la venta de sus Hamburguesas, el restaurante tiene 3 tipos de hamburguesa: la sencilla, la doble y la triple que cuestan 10.000, 15.000 y 20.000 respectivamente; a cada hamburguesa se le pueden adicionar: queso extra, pepinillos y tocineta; que tienen un valor adicional de 2.000, 1.000 y 3.000 respectivamente. construya el diagrama de flujo que le permita calcular el precio de una hamburguesa con sus adiciones más la propina, si el cliente acepta incluirla y que es el 10% del total de la cuenta; finalmente pregunte con cuanto pagará la cuenta y le indique el cambio a devolver.

# Entrada del usuario, convertida a entero
hamburguesa = int(input("Indique el tipo de Hamburguesa: Digite 1 para Hamburguesa Sencilla, 2 para Hamburguesa Doble y 3 para Hamburguesa Triple: "))
adiciones = int(input("Indique las adiciones que quiera agregar: Digite 1 para ninguna, 2 para Queso Extra, 3 para Pepinillos o 4 para Tocineta: "))
propina = int(input("Desea añadir propina?: 1 para SI, 2 para NO: "))

def precioTotal(hamburguesa, adiciones, propina):
    # Determinar el precio base según el tipo de hamburguesa
    if hamburguesa == 1:
        precio = 10000
    elif hamburguesa == 2:
        precio = 15000
    elif hamburguesa == 3:
        precio = 20000
    
  
    if adiciones == 1:
        pass 
    elif adiciones == 2:
        precio += 2000
    elif adiciones == 3:
        precio += 1000
    elif adiciones == 4:
        precio += 3000


    if propina == 1:
        precio *= 1.1 
    elif propina == 2:
        pass 

    return precio


precio = precioTotal(hamburguesa, adiciones, propina)
print(f"El precio total es: {precio}")

cantPago = float(input("Con cuanto cancelas?: "))
cambio = cantPago - precio
print(f"Su cambio es de {cambio}")
