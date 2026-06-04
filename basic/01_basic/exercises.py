###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

name = input("Como te llamas? ")
city = input("Como se llama tu ciudad? ")

print(f"Hola {name} \nEres de {city}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

dates = [a,b,c,d,e]

for i in dates:
    print(type(i))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

a = "12345"
a = int(a)
print(type(a))
a = float(a)
print(type(a))

b = 3.99
b = int(b)
print(type(b), f"num: {b}")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")


name = input("Cuál es tu nombre? ")
age = int(input("Cuantos anyos tienes? "))
height = float(input("Cuanto mides? "))

print(f"Hola {name}, tienes {age} años y mides {height} cm.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

num_pi = 3.1415
num_pi = round(num_pi)
result=num_pi/2
print(result)