"""
EJERCICIOS: Tipos de datos (int, float, str, bool, NoneType)
Nivel: Básico
"""

# Ejercicio 1: Identificar tipos
# Usa type() para imprimir el tipo de cada variable:
# a = 42, b = 3.14, c = "Python", d = True, e = None
# Tu código aquí:
a, b, c, d, e = 42, 3.14, "Python", True, None
print(type(a))  # int
print(type(b))  # float  
print(type(c))  # str
print(type(d))  # bool
print(type(e))  # NoneType
# Ejercicio 2: Número complejo
# Crea un número complejo con parte real 3 y parte imaginaria 5.
# Imprime su parte real y su parte imaginaria por separado.
# Tu código aquí:
complejo = 3 + 5j
print(f"Parte real: {complejo.real}")
print(f"Parte imaginaria: {complejo.imag}")
# Ejercicio 3: Strings multilínea
# Crea un string multilínea que contenga un poema de 3 versos.
# Imprímelo usando print().
# Tu código aquí:
poema = """Rosas son rojas,
Violetas son azules,
Python es genial,
Y tú también."""

print(poema)
# Ejercicio 4: Tipo inesperado
# ¿Qué tipo tiene el resultado de 10 / 3? Verifícalo con type().
# ¿Y el resultado de 10 // 3? ¿Por qué son diferentes?
# Tu código aquí:
print(type(10 / 3))   # float
print(type(10 // 3))  # int
# La división normal (/) siempre devuelve un float, incluso si el resultado es un número entero.
# La división entera (//) devuelve un int si ambos operandos son enteros, y redondea hacia abajo el resultado.

# Ejercicio 5: Booleanos implícitos
# Determina sin usar type() cuáles de estos valores son truthy y cuáles falsy:
# 0, 1, "", "Hola", [], [1, 2], None
# Luego verifícalo con bool().
# Tu código aquí:
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Hola"))   # True
print(bool([]))       # False
print(bool([1, 2]))  # True
print(bool(None))     # False