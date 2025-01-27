# Caso Mc Gonalds
# Entradas:
#  hamb_sencilla, hamb_doble, hamb_triple,val_queso, val_pepinillo, val_tocineta, tipo_hamburguesa (de tipo int)
#  ptje_propina, pago (float)
#  adi_queso, adi_pepinillo, adi_tocineta, adi_propina (str)
# Salidas:
# valor_cuenta, cambio (float)
# Análisis:
#   Se solicita el tipo de hambueguesa, se asina el valor inicial a la cuenta, la cual se actualiza
#   con los adicionales que quiera el usuario. Se muestra eñ valor de la cuenta.
#   Se pregunta si se adiciona el valor de la propina a la cuenta.
#   Se pide el valor de pago y se calcula el cambio.
#   Finalmente se muestra el cambio o se indica el valor faltante.

hamb_sencilla=10000
hamb_doble=15000
hamb_triple=20000
val_queso=2000
val_pepinillo=1000
val_tocineta=3000
pteje_propina=0.1

print("Restaurante Mc Gonalds")
print("         Menú")
print(" [1] Hambueguesa sencilla")
print(" [2] Hambueguesa doble")
print(" [3] Hambueguesa triple")
tipo_hamburguesa=int(input("Seleccione el tipo de hamburguesa "))

if  tipo_hamburguesa == 1:
     valor_cuenta = hamb_sencilla 
elif tipo_hamburguesa == 2:
    valor_cuenta = hamb_doble 
elif tipo_hamburguesa == 3:
    valor_cuenta = hamb_triple 
else:
    print(" opción no válida")

if tipo_hamburguesa>=1 and tipo_hamburguesa<=3:
    adi_queso=str(input("Desea adicionar queso (S/N)"))
    if adi_queso == "s" or adi_queso == "S":
        valor_cuenta = valor_cuenta+val_queso
    adi_pepinillo=str(input("Desea adicionar pepinillo (S/N)"))
    if adi_pepinillo == "s" or adi_pepinillo == "S":
        valor_cuenta = valor_cuenta+val_pepinillo
    adi_tocineta=str(input("Desea adicionar tocineta (S/N)"))
    if adi_tocineta == "s" or adi_tocineta == "S":
        valor_cuenta = valor_cuenta+val_tocineta
    adi_propina=str(input("Desea adicionar el valor de la propina (S/N)"))
    if adi_propina == "s" or adi_propina == "S":
       valor_cuenta = valor_cuenta+valor_cuenta*pteje_propina
       
    print(" El valor a pagar es :", valor_cuenta )
    pago=float(input("¿Con cuanto cancela? "))
    if pago>= valor_cuenta:
       cambio=pago-valor_cuenta
       print(" Su devuelta es: ", cambio)
    else:
        cambio=valor_cuenta-pago
        print(f"Falta dinero ${cambio} para cubrir la cuenta ")

        
