###
# 05 - Entrada de usuario -> input()
# La funcion input() nos permite solicitar datos al usuario a través de la consola.
###

name = input("¿Cuál es tu nombre?\n")

age = input("¿Cuál es tu edad?\n")

# Input devuelve cadena de texto SIEMPRE
print(f"Hola {name}, dentro de 20 años tendras: {int(age)+20} años")

# Pedir varios datos a la vez en un input:
country, city = input("En que país y ciudad vives?\n").split(sep=",")

print(f"Vives en {city}, {country}")