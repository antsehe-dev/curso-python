"""
EJERCICIOS: Funciones (def, parámetros, *args, **kwargs, type hints)
Nivel: Básico-Intermedio
"""

# Ejercicio 1: Función simple
# Define una función saludar(nombre) que imprima "¡Hola, [nombre]!".
def saludar(nombre):
    print(f"¡Hola, {nombre}!")
saludar("Ana")

# Ejercicio 2: Return
# Define una función suma(a, b) que devuelva la suma de dos números.
def suma(a, b):
    return a + b
print(suma(3, 5))

# Ejercicio 3: Parámetros por defecto
# Define una función potencia(base, exponente=2) que calcule la potencia.
# Pruébala con y sin el segundo argumento.
def potencia(base, exponente=2):
    return base ** exponente
print(potencia(3))
print(potencia(3, 4))

# Ejercicio 4: *args
# Define una función sumar_todos(*args) que sume todos los números que reciba.
# Tu código aquí:

# Ejercicio 5: **kwargs
# Define una función presentar(**kwargs) que reciba nombre, edad, ciudad
# y los muestre formateados. Pruébala con: presentar(nombre="Luis", edad=28, ciudad="Madrid")
# Tu código aquí:

# Ejercicio 6: Type hints
# Define una función calcular_imc(peso: float, altura: float) -> float
# que calcule el índice de masa corporal (peso / altura**2).
# Tu código aquí:

# Ejercicio 7: Función con *args y **kwargs combinados
# Define una función hacer_pedido(producto, *args, **kwargs) donde:
# - producto es obligatorio
# - *args son extras (ej: "sin hielo", "poco cocido")
# - **kwargs son opciones (ej: tamaño="grande", cantidad=2)
# Muestra toda la información formateada.
# Tu código aquí:

# Ejercicio 8: Documentación
# Define una función es_primo(n) que devuelva True si n es primo.
# Incluye un docstring explicando qué hace.
# Tu código aquí:

# Ejercicio 9: Función como argumento
# Define una función aplicar_operacion(a, b, operacion) que reciba otra función
# y la aplique a a y b. Pruébala con suma, resta y multiplicación.
# Tu código aquí:
