"""
EJERCICIOS: range()
Nivel: Básico
"""

# Ejercicio 1: range(stop)
# Usa range(10) para imprimir los números del 0 al 9.
for i in range(10):
    print(i, end=" ")
print()

# Ejercicio 2: range(start, stop)
# Usa range(5, 15) para imprimir los números del 5 al 14.
for i in range(5, 15):
    print(i, end=" ")
print()

# Ejercicio 3: range(start, stop, step)
# Imprime los números pares del 0 al 20 usando range con step.
for i in range(0, 21, 2):
    print(i, end=" ")
print()

# Ejercicio 4: Cuenta atrás
# Usa range con step negativo para contar del 10 al 1.
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Ejercicio 5: Tabla de multiplicar
# Pide un número al usuario y muestra su tabla de multiplicar (del 1 al 10).
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Ejercicio 6: Suma 1 a N
# Pide un número N y calcula la suma de 1 a N usando range y un bucle.
N = int(input("N: "))
suma = sum(range(1, N + 1))
print(f"Suma de 1 a {N}: {suma}")

# Ejercicio 7: Números impares decrecientes
# Imprime los números impares del 99 al 1 usando range.
for i in range(99, 0, -2):
    print(i, end=" ")
print()

# Ejercicio 8: Lista con range
# Convierte range(0, 50, 5) en una lista y muéstrala.
print(list(range(0, 50, 5)))
