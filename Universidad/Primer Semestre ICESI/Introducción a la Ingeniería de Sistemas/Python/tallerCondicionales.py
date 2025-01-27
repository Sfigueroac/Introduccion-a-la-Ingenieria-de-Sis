#Taller de Condicionales
"""
Para cada uno de los ejercicios elabore un algoritmo en pseudocódigo que resuelva
el problema presentado. Haga uso de las estructuras condicionales vistas en clase.
"""

# 1. Se debe averiguar si un número es par o impar y si es positivo o negativo.
def numeroImpar():
    print("Este programa averigua si el número que proporcione abajo es par o impar, y positivo o negativo.")
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 1:
        print(numero, " es impar")
    else:
        print(numero," es par")
    if numero < 0:
        print(numero, "es negativo")
    else:
        print(numero, "es positivo")
# 2. Determinar el tipo de ángulo según su medida:
# • Agudo si es menor a 90
# • Recto si es igual a 90°
# • Obtuso si es mayor que 90° pero menor que 180°
# • Llano si es igual a 180°\
# • Cóncavo si es mayor que 180° pero menor que 360°
# • Completo si es igual a 360°

def definirAngulo():
    print("Este programa se encarga de averiguar el tipo de ángulo.")
    angulo = int(input("Ingrese un ángulo: "))
    anguloes = ""
    if angulo < 90:
        anguloes = angulo + " es agudo"
    elif angulo == 90:
        anguloes = "Ángulo es recto"
    elif angulo > 90 and angulo < 180:
        anguloes = "Ángulo es obtuso"
    elif angulo == 180:
        anguloes = "Ángulo es llano"
    elif angulo == 360:
        anguloes = "Ángulo es completo"
    else:
        anguloes = "Ángulo es cóncavo"

    print(anguloes)

#3. Elaborar un algoritmo que permita identificar el tipo de triángulo solicitando el tamaño de sus lados

def tipoTriangulo():
    print("Este programa determian el tipo de triángulo teniendo en cuenta los 3 ángulos que se le ingresen.")
    lado1 = int(input("ingrese el primer lado del triángulo: "))
    lado2 = int(input("ingrese el segundo lado del triángulo: "))
    lado3 = int(input("ingrese el tercer lado del triángulo: "))
    tipotriangulo = ""
    if lado1 == lado2 == lado3:
        print("El triángulo es Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es Isósceles.")
    else:
        print("El triángulo es Escaleno.")
    print(tipotriangulo)

# 4. Solicitar al usuario el nombre y la edad de 2 personas, se debe indicar el nombre de la persona mayor

def personaMayor():
    print("Este programa se encarga de determinar si una persona es mayor o menor que otra.")
    nombre1 = input("Ingrese el primer nombre: ")
    edad1 = float(input("Ingrese la edad de esta persona: "))
    nombre2 = input("Ingrese el segundo nombre: ")
    edad2 = float(input("Ingrese la edad de la segunda persona: "))

    if edad2 > edad1:
        print(f"{nombre2} es mayor")
    else:
        print(nombre1, "es mayor")

#5
"""
Hugo, Paco y Luis son hermanos, y su tío quiere darle un regalo acorde al
orden de sus edades y necesita identificar quien es el mayor, quien está en
el medio y cuál es el menor, pues está sufriendo de problemas de memoria
y no logra recordar las edades de los tres. De lo que está seguro es que sus
edades son distintas. Nos piden ayudarlo elaborando un algoritmo que
solicite las edades de los sobrinos, presente un mensaje si detecta la
introducción de edades iguales e identifique quien es el mayor, el del medio
y el menor.
"""
def hugoPacoyLuis():
    print("Este programa, introduciendo la edad de Hugo, Paco y Luis, nos permite saber quién es el mayor, quién el menor, y quién el del medio.")
    edad1 = int(input("Introduce la edad de Hugo: "))
    edad2 = int(input("Introduce la edad de Paco: "))
    edad3 = int(input("Introduce la edad de Luis: "))

    if edad1 == edad2 or edad1 == edad3 or edad2 == edad3:
        print("Error: Las edades deben ser diferentes.")

    edades = [(edad1, "Hugo"), (edad2, "Paco"), (edad3, "Luis")]
    edades_ordenadas = sorted(edades, reverse=True)

    mayor = edades_ordenadas[0][1]
    medio = edades_ordenadas[1][1]
    menor = edades_ordenadas[2][1]
    print(f"El mayor es {mayor}, el del medio es {medio}, y el menor es {menor}.")

#6 Se debe solicitar al usuario un número del 1 al 10 y se debe mostrar su equivalente en números romanos.

#Aquí usé un diccionario
"""
numeros = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X"}
numeroarabe = int(input("Ingrese el número en notación arábica: "))
romamo = numeros[numeroarabe]
print("el número  en notación romana es:  ", romamo)

"""
#Aquí una lista
def calcularNumeros():
    print("Este programa convierte los números del 1 al 10 de notación arabica a romana.")
    numeros = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    numeroarabe = int(input("Ingrese el número en notación arábica: "))
    romano = numeros[numeroarabe-1]
    print("el numero en notación romana es: ", romano) #Yo sé que no usé condicionales pero no me diga que es no re ineficiente jajaja if elif elif elif elif elif elif elif elif elif elif... En tal caso sería algo así
    """
    if numero == 1:
        print ("I")
    elif numero == 2:
        print ("II")
    elif numero == 3:
        print ("III")
    elif numero == 4:
        print ("IV")
    elif numero == 5:
        print ("V")
    elif numero == 6:
        print ("VI")
    elif numero == 7:
        print ("VII")
    elif numero == 8:
        print ("VIII")
    elif numero == 9:
        print ("IX")
    elif numero == 10:
        print ("X")  
    """
#7 Si un operario trabaja semanalmente 40 horas o menos se le paga $16000 por hora. Si trabaja más de 40 horas se le paga $16000 por cada una de las primeras 40 horas y $20000 por cada hora extra.

def ejSalario():
    print("Este programa calcula el monto a pagarle a un operario teniendo en cuenta sus horas extras.")
    horasTrabajadas = int(input("Ingrese el número de horas trabajadas: "))

    def calcularSalario(horasTrabajadas):
        if 0 <= horasTrabajadas <= 40:
            salario = horasTrabajadas * 16000
        elif horasTrabajadas > 40:
            salario = (40*16000) + (horasTrabajadas-40)*20000
        return salario

    salario = calcularSalario(horasTrabajadas)
    print("El salario del operario debe ser ", salario)


#8. Calcular el número de pulsaciones que debe tener una persona por cada 10
# segundos de ejercicio aeróbico; la fórmula que se aplica cuando el sexo es
# femenino es: (220 - edad)/10 y si el sexo es masculino: (210 - edad)/10
def calcularPulsaciones():
    print("Este programa calcula el nûmero de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico, todo esto teniendo en cuenta género y edad")
    genero = input("Escriba F para género femenino y M para nombre masculino: ").upper
    edad = int(input("Ingrese su edad: "))
    if genero == "F":
        frecuencia = (220-edad)/10
    else: 
        frecuencia = (210-edad)/10
    print("El número de pulsaciones que esta persona debe tener por cada 10 segundos de ejercicio aeróbico es de: ", frecuencia)

#9. A un trabajador le descuentan de su sueldo el 10% si su sueldo es menor o igual a 1000. Por encima de 1000 y hasta 2000 el 5% del adicional, y por encima de 2000 el 3% del adicional. Calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo.

def descuento():
    print("Este programa se encarga de calcular el descuento que se la realiza a un trabajador teniendo en cuenta el sueldo.")
    sueldo = float(input("Ingrese el sueldo: "))
    if sueldo <= 1000:
        descuento = sueldo * 0.1
        sueldo -= descuento
    elif 1000 < sueldo <= 2000:
        descuento = 100 + (sueldo - 1000) * 0.05
        sueldo -= descuento
    elif sueldo > 2000:
        descuento = 100 + 50 + (sueldo - 2000) * 0.03
        sueldo -= descuento
    print("El sueldo es de ", sueldo)
    print("El descuento es de ", descuento)

#10. Una empresa calcula el salario mensual de un trabajador según la cantidad de horas trabajadas, si trabaja hasta 180 horas se le pagará cada hora al valor de su tarifa, si trabaja más de 180 horas al mes se le pagará un recargo de un 50% adicional a su tarifa por cada hora adicional trabajada

def calcularHorasTarifa():
    print("Este programa calcula el salario mensual de un trabajador según la cantidad de horas trabajadas.")
    horas = float(input("Ingrese la cantidad de horas trabajadas: "))
    tarifa = float(input("Ingrese la tarifa de este empleado: "))
    if 0 <= horas <= 180:
        pago = horas * tarifa
    elif horas > 180:
        pago = (180 * tarifa) + (horas-180)*(tarifa*1.5)
    print("El pago es de: ", pago)

# 11. Hacer un programa que muestre un mensaje de acuerdo a la edad ingresada de la siguiente manera: Si la edad es de 0 a 10 años “niño”, si la edad es de 11 a 14 años “púber”, si la edad es de 15 a 18 años “adolescente”, si la edad es de 19 a 25 años “joven”, si la edad es de 26 años en adelante “adulto”.\

def descEdades():
    print("Este programa le indica a usted en qué etapa de edad está teniendo en cuenta cuântos años tiene.")
    edad = int(input("ingrese una edad: "))
    if 0 < edad <= 10:
        tipoEdad = "niño"
    elif 10< edad <= 14:
        tipoEdad = "puber"
    elif 15 <= edad <= 18:
        tipoEdad = "adolescente"
    elif 19 <= edad <= 25:
        tipoEdad = "joven"
    elif edad > 25:
        tipoEdad = "adulto"
    
    print(tipoEdad)

#12. Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones: Si los ingresos del comprador son menores de $1.000.000, la cuota inicial será del 15% del costo de la casa y el resto se distribuirá en pagos mensuales, a pagar en diez años. Si los ingresos del comprador son igual o mayores de $1.000.000, la cuota inicial será del 30% del costo de la casa y el resto se distribuirá en pagos mensuales a pagar en 7 años. La empresa quiere obtener cuanto debe pagar un comprador por concepto de enganche y cuanto por cada pago parcial.

def vis():
    print("Este programa calcula la cuota inicial y pago mensual de una vivienda de interés social.")
    ingresosMensuales = float(input("Digite los ingresos mensuales de la persona: "))
    costoDeLaCasa = float(input("Ingrese el costo de la casa: "))
    if ingresosMensuales < 1000000:
        cuotaInicial = costoDeLaCasa * 0.15
        meses = 120
        pagos = (costoDeLaCasa - cuotaInicial) / meses
        
    elif ingresosMensuales >= 1000000:
        cuotaInicial = costoDeLaCasa * 0.30
        meses = 84
        pagos = (costoDeLaCasa - cuotaInicial) / meses
        

    print(f"La persona debe pagar {cuotaInicial} de cuota inicial y pagos mensuales de {pagos}, durante {meses} meses")

#13. En los almacenes es muy común que en ciertas épocas del año se realicen descuentos en las compras. En ocasiones dichos descuentos pasan de un determinado monto. Elabore un programa que permita calcular el descuento y el total a pagar a partir de las siguientes políticas previstas para las compras:
# • Si el valor de la compra es menor de $100.000 no tiene descuento
# • Si el valor de la compra esta entre $100.000 y $200.000 el descuento que aplica es del 5%.
# • Si el valor de compra es mayor que $200.000 el descuento que aplica es del 10%


def calcularDescuento():
    print("Este programa calcula el descuento realizado a una compra")
    compra = float( input ("Ingrese el monto de la compra: "))
    if 0 <= compra < 100000:
        pass
    elif 100000 <= compra <= 200000:
        descuento = compra * 0.05
        compra -= descuento
    elif compra > 200000:
        descuento = compra * 0.1
        compra -= descuento
    print(f"El descuento será de {descuento}, y el valor total después de esta será de {compra}") 

#14. Debido al cambio climático, el departamento del Valle del Cauca enfrenta una gran sequía, la gobernación ha decido implementar un sistema piloto para el cobro de agua en el cual se castiga el consumo excesivo de agua. El sistema se probará en la ciudad de Cali. En la tabla 1, se muestra el valor en pesos por los m3 consumidos. Tenga en cuenta que en la tabla se indica lo que hay que cobrar por los m3 que se encuentran en el intervalo.
    
def noMeSubanMasLosServiciosMalditaSea():
    print("Este programa calcula el monto a pagar del servicio público de agua teniendo en cuenta su consumo")
    consumo = float( input ( "Ingrese la cantidad de metros cúbicos consumidos: "))
    if consumo <= 100:
        tarifa = 100
    elif 100 < consumo <= 500:
        tarifa = 300
    elif 500 < consumo <= 1000:
        tarifa = 500
    elif consumo < 1000:
        tarifa = 1000
    cobro = tarifa * consumo
    print(f"Su consumo fue de {consumo}, por lo que su tarifa por m3 es de {tarifa}, resultando en un monto a cobrar de {cobro} pesos")

#15. Desarrolle un diagrama de flujo que dado un número de días lo exprese en el término de tiempo más amplio posible, es decir: años, meses, días. Ejemplo: 551 días = 1 año, 6 meses y 6 días; tenga en cuenta un año = 365 días, 1 mes = 30 días

def ultimaFunciónAlguienQueMeDeYaMiTituloDeIngenieroDeSistemasNoVenQueYaSeHacerIfsFuncionesYCiclos(): #Programando este bonus con las últimas energias, no me podia quedar sin probar lo del bucle
    print("Este programa convierte una cantidad de dias al formato Años, Meses, Dias.")
    diasAConvertir = int(input("Ingrese la cantidad de dias que desea convertir: "))
    diasTotales = diasAConvertir
    años = 0
    meses = 0
    while diasAConvertir >= 365:
        años += 1
        diasAConvertir -= 365
    while diasAConvertir >= 30:
        meses += 1
        diasAConvertir -= 30
    print(f"{diasTotales}, son {años} años, {meses} meses y {diasAConvertir} dias")

def ultimaFunciónAlguienQueMeDeYaMiTituloDeIngenieroDeSistemasNoVenQueYaSeHacerIfsYFunciones(): 
    print("Este programa convierte una cantidad de dias al formato Años, Meses, Dias.")
    diasAConvertir = int(input("Ingrese la cantidad de dias que desea convertir: "))
    años = 0
    if diasAConvertir > 365:
        años = diasAConvertir // 365
    
    if diasAConvertir - (años*365) > 30:
        meses = (diasAConvertir - (años*365)) // 30
    diasrestantes = diasAConvertir - ((años * 365) + (meses * 30))
    print(f"{diasAConvertir} son {años} años, {meses} meses y {diasrestantes} dias.")
    

def menu():
    end = False
    while not(end):
        opc = int(input("Escriba el número del ejercicio que desea verificar: (Ejercicios del 1 al 15, 16 para una variante del 15 pero con bucles y DIGITE 17 PARA SALIR): "))
        if (opc==1):
            numeroImpar()
        elif(opc==2):
            definirAngulo()
        elif(opc==3):
            tipoTriangulo()
        elif(opc==4):
            personaMayor()
        elif(opc == 5):
            hugoPacoyLuis()
        elif(opc == 6):
            calcularNumeros()
        elif(opc == 7):
            ejSalario()
        elif(opc == 8):
            calcularPulsaciones()
        elif(opc == 9):
            descuento()
        elif(opc == 10):
            calcularHorasTarifa()
        elif(opc == 11):
            descEdades()
        elif(opc == 12):
            vis()
        elif(opc == 13):
            calcularDescuento()
        elif(opc == 14):
            noMeSubanMasLosServiciosMalditaSea()
        elif(opc == 15):
            ultimaFunciónAlguienQueMeDeYaMiTituloDeIngenieroDeSistemasNoVenQueYaSeHacerIfsYFunciones()
        elif(opc == 16):
            ultimaFunciónAlguienQueMeDeYaMiTituloDeIngenieroDeSistemasNoVenQueYaSeHacerIfsFuncionesYCiclos()
        elif(opc==17):
            end = 1
        else:
            print("Escriba un número entre 1 y 17")
menu()