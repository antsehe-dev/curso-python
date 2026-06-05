"""
EJERCICIOS: Casting y conversión de tipos
Nivel: Básico
"""

# Ejercicio 1: String a entero
# Convierte "123" a entero y súmale 77. Imprime el resultado.
num = int("123") + 77
print(num)

# Ejercicio 2: String a float
# Convierte "3.1416" a float y redondea a 2 decimales con round().
pi = round(float("3.1416"), 2)
print(pi)

# Ejercicio 3: Concatenación con casting
# Dado edad = 30, imprime: "Tengo 30 años" (sin usar f-strings, solo concatenación con +).
edad = 30
print("Tengo " + str(edad) + " años")

# Ejercicio 4: Truthy y falsy
# Convierte a bool los siguientes valores: 0, 1, "", "False", [], [0]
# ¿Cuáles dan True y cuáles False?
valores = [0, 1, "", "False", [], [0]]
for v in valores:
    print(f"{v!r} -> {bool(v)}")
# Solo 0, "" y [] dan False; el resto da True ("False" es un string no vacío, [0] es lista no vacía)

# Ejercicio 5: Redondeo
# Redondea los siguientes números a 1 decimal: 3.14159, 2.71828, 1.61803
print(round(3.14159, 1))
print(round(2.71828, 1))
print(round(1.61803, 1))

# Ejercicio 6: Casting peligroso
# ¿Qué ocurre si intentas convertir "Hola" a int? Pruébalo dentro de un try/except.
try:
    int("Hola")
except ValueError as e:
    print(f"Error: {e}")
