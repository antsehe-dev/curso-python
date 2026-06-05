"""
EJERCICIOS: Variables, naming y asignaciones
Nivel: Básico
"""

# Ejercicio 1: Naming correcto
# ¿Cuáles de estos nombres de variable son válidos en Python?
# 1nombre, nombre1, mi-variable, mi_variable, _edad, class, NombreCompleto
# Escribe una lista con los válidos y otra con los inválidos.
validos = ["nombre1", "mi_variable", "_edad", "NombreCompleto"]
invalidos = ["1nombre", "mi-variable", "class"]
print("Válidos:", validos)
print("Inválidos:", invalidos)
# 1nombre: empieza con número, inválido
# mi-variable: guión no permitido
# class: palabra reservada

# Ejercicio 2: Asignación múltiple
# Asigna los valores 10, 20, 30 a las variables a, b, c en una sola línea.
# Luego intercambia sus valores (swap) en una sola línea: a=30, b=10, c=20
a, b, c = 10, 20, 30
print(a, b, c)
a, b, c = 30, 10, 20
print(a, b, c)

# Ejercicio 3: Desempaquetado de tupla
# Dada la tupla coordenadas = (40.4168, -3.7038), desempaqueta en latitud y longitud.
coordenadas = (40.4168, -3.7038)
latitud, longitud = coordenadas
print(f"Latitud: {latitud}, Longitud: {longitud}")

# Ejercicio 4: Constantes por convención
# Define una constante PI con valor 3.14159 (usa mayúsculas por convención).
# Luego calcula el área de un círculo de radio 5: area = PI * radio ** 2
PI = 3.14159
radio = 5
area = PI * radio ** 2
print(f"Área del círculo: {area}")

# Ejercicio 5: Type hints
# Declara una variable nombre: str, edad: int, altura: float con type hints.
# Luego asigna valores y usa print() para mostrar el tipo real con type().
nombre: str = "Luis"
edad: int = 28
altura: float = 1.75
print(f"{nombre} es {type(nombre)}, {edad} es {type(edad)}, {altura} es {type(altura)}")
