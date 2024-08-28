
#Sección 1

"""
Actividad Propuesta:
1. Crea una variable llamada ciudad que almacene el nombre de la ciudad donde
quisieras ir de vacaciones.
2. Crea una variable años que almacene tu edad.
3. Crea una variable es_mayor_de_edad que almacene True si tienes 18 años o
más, y False en caso contrario.
4. Muestra el contenido de las variables
"""
ciudad = "Berlin" 
años = 19 
es_mayor_de_edad = True 

print(ciudad)
print(años)
print(es_mayor_de_edad)

#Sección 2
"""
1. Crea una variable precio que almacene el valor 99.99.
2. Crea una lista colores que contenga tres colores de tu preferencia.
3. Crea un diccionario producto con las llaves nombre, precio, y cantidad. Asigna
valores adecuados a cada una.
4. Muestra el contenido de las variables
"""

precio = 99.99
colores = ["azul", "amarillo", "verde"]
producto = {"nombre": "computador", "precio": 2300, "cantidad": 2}

print(precio)
print(colores)
print(producto)

#Sección 3
"""
1. Usa las variables precio y cantidad de la actividad anterior para calcular el
costo total de cantidad de productos.
2. Crea una lista numeros con valores del 1 al 5, y luego accede al tercer
elemento de la lista.
3. Concatenar dos cadenas de texto, saludo1 y saludo2, y almacénalo en una
nueva variable saludo_completo.
4. Muestra el contenido de las variables
"""

precioProducto = producto["precio"]
cantProducto = producto["cantidad"]
valorTotal = precioProducto * cantProducto

numeros = [1, 2, 3, 4, 5]
elnumero = numeros[2]

saludo1 = "Hola"
saludo2= "Buenas tardes"

saludoTotal = saludo1 + saludo2


print(valorTotal)
print(elnumero)
print(saludoTotal)

