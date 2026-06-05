"""
EJERCICIOS: if/elif/else y condicionales
Nivel: Básico
"""

# Ejercicio 1: Mayor de edad
# Pide la edad al usuario y muestra si es mayor de edad (>= 18) o menor.
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2: Par o impar
# Pide un número entero y determina si es par o impar usando el operador %.
n = int(input("Dime un número: "))
if n % 2 == 0:
    print("Es par")
else:
    print("Es impar")

# Ejercicio 3: Nota escolar
# Pide una nota numérica (0-10) y muestra la calificación:
# 0-4: Suspenso, 5-6: Suficiente, 7-8: Notable, 9-10: Sobresaliente
nota = float(input("Nota (0-10): "))
if nota < 5:
    print("Suspenso")
elif nota <= 6:
    print("Suficiente")
elif nota <= 8:
    print("Notable")
else:
    print("Sobresaliente")

# Ejercicio 4: Calculadora simple
# Pide dos números y un operador (+, -, *, /). Realiza la operación y muestra el resultado.
# Si el operador no es válido, muestra un mensaje de error.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
op = input("Operador (+, -, *, /): ")
if op == "+":
    print(f"{a} {op} {b} = {a + b}")
elif op == "-":
    print(f"{a} {op} {b} = {a - b}")
elif op == "*":
    print(f"{a} {op} {b} = {a * b}")
elif op == "/":
    print(f"{a} {op} {b} = {a / b}")
else:
    print("Operador no válido")

# Ejercicio 5: Año bisiesto
# Pide un año y determina si es bisiesto:
# - Divisible entre 4 y no entre 100, o divisible entre 400.
anio = int(input("Año: "))
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es bisiesto")
else:
    print(f"{anio} no es bisiesto")

# Ejercicio 6: Operador ternario
# Dado un número, usa el operador ternario para asignar "par" o "impar" a una variable.
n = 7
resultado = "par" if n % 2 == 0 else "impar"
print(f"{n} es {resultado}")

# Ejercicio 7: Anidación
# Pide tres números y determina cuál es el mayor (sin usar max()).
x = int(input("Número 1: "))
y = int(input("Número 2: "))
z = int(input("Número 3: "))
if x > y and x > z:
    print(f"El mayor es {x}")
elif y > x and y > z:
    print(f"El mayor es {y}")
else:
    print(f"El mayor es {z}")
