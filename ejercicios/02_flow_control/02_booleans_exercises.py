"""
EJERCICIOS: Booleanos y operadores lógicos
Nivel: Básico
"""

# Ejercicio 1: Tabla de verdad
# Evalúa las siguientes expresiones y predice el resultado antes de ejecutar:
# True and True, True and False, True or False, False or False, not True
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)

# Ejercicio 2: Rangos
# Pide un número y verifica si está entre 10 y 20 (incluidos).
# Muestra "Dentro del rango" o "Fuera del rango".
n = int(input("Número: "))
if 10 <= n <= 20:
    print("Dentro del rango")
else:
    print("Fuera del rango")

# Ejercicio 3: Validación de contraseña
# Pide una contraseña y verifica que tenga al menos 8 caracteres Y contenga un número.
# (Pista: usa any(c.isdigit() for c in password))
password = input("Contraseña: ")
if len(password) >= 8 and any(c.isdigit() for c in password):
    print("Contraseña válida")
else:
    print("Contraseña debe tener 8+ caracteres y al menos un número")

# Ejercicio 4: Tres números
# Pide tres números y determina si todos son positivos, al menos uno es negativo, o ninguno.
# Tu código aquí:

# Ejercicio 5: Comparación de strings
# Pide dos palabras y determina cuál es mayor alfabéticamente (lexicográficamente).
# Tu código aquí:

# Ejercicio 6: Descuento
# Pide el precio de un producto y si el usuario es "estudiante".
# Si es estudiante Y el precio > 100, aplica 20% descuento.
# Si es estudiante Y precio <= 100, aplica 10% descuento.
# Si no es estudiante, no hay descuento.
# Tu código aquí:
