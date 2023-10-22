print("hola mundo",type("hola mundo"))
print(5, type(5))
print(5.5, type(5.5))
print(True, type(True))

# Variables
# Que es una variable? Es un espacio de memoria para almacenar valores que cambian a lo largo de la ejecucion del programa
# Puedes pensar en una variable como una caja que contiene informacion que puede ser modificada
# El nombre de la variable es como una etiqueta para identificarla
# Las variables se crean cuando se les asigna un valor por primera vez
# Las variables se pueden reasignar a cualquier momento, independientemente de su tipo de datos
# Las variables no necesitan declararse con ningun tipo en particular y pueden incluso cambiar de tipo despues de haber sido establecidas
nombre = "Karlita"

print(nombre, type(nombre))

edad = 20

print(edad, type(edad))

estatura = 1.63

print(estatura, type(estatura))

es_sabado = True

print(es_sabado, type(es_sabado))

# Operaciones

# Strings

# Concatenacion

nombre_completo = nombre + " " + "Gonzalez"

print(nombre_completo)

# Interpolacion

print(f"Hola mi nombre es {nombre} y tengo {edad} años")

# Numeros

# Suma

print(5 + 5)

# Resta

print(10 - 5)

# Multiplicacion

print(3 * 3)

# Division

print(10 / 2)

# Division entera

print(10 // 3)

# Modulo

print(10 % 3)

# Exponente

print(3 ** 3)

# Booleanos

# Negacion

print(not True)

# And

print(True and False)
print(True and True)
print(False and False)

# Or

print(True or False)
print(True or True)
print(False or False)

# Igualdad

print(5 == 5)

# Diferencia

print(5 != 5)

# Mayor que

print(5 > 5)

# Menor que

print(5 < 5)

# Mayor o igual que

print(5 >= 5)

# Menor o igual que

print(5 <= 5)

# Ejemplo: puedo comprar cerveza?

edad = 18
print(edad >= 18)
