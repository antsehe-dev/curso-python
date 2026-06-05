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
a,b,c = map(float, input("Tres números separados por espacio: ").split())
if a > 0 and b > 0 and c > 0:
    print("Todos son positivos")
elif a < 0 or b < 0 or c < 0:
    print("Al menos uno es negativo")
else:
    print("Ninguno es negativo, pero no todos son positivos")
# Ejercicio 5: Comparación de strings
# Pide dos palabras y determina cuál es mayor alfabéticamente (lexicográficamente).
# Tu código aquí:
word1, word2 = input("Dos palabras separadas por espacio: ").split()
if word1 > word2:
    print(f"La palabra {word1} va después de {word2} alfabéticamente")
elif word1 < word2:
    print(f"La palabra {word1} va antes de {word2} alfabéticamente")
else:
    print("Ambas palabras son iguales")


# Ejercicio 6: Descuento
# Pide el precio de un producto y si el usuario es "estudiante".
# Si es estudiante Y el precio > 100, aplica 20% descuento.
# Si es estudiante Y precio <= 100, aplica 10% descuento.
# Si no es estudiante, no hay descuento.
# Tu código aquí:
price = float(input("Introduce el precio de un producto: "))
is_student = input("Eres estudiante? (Y/n): ")
if is_student.lower() == 'y':
    is_student = True
elif is_student.lower() == 'n':
    is_student = False

if is_student and price > 100:
    price = price-(price*.20)
elif is_student and price <= 100:
    price = price-(price*.10)

print(f"El precio se ha quedado en {price} €")
