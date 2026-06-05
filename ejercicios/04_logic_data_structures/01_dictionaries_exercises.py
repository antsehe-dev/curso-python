"""
EJERCICIOS: Diccionarios
Nivel: Básico-Intermedio
"""

# Ejercicio 1: Crear y acceder
# Crea un diccionario persona con clave: nombre, edad, ciudad.
# Accede e imprime cada valor.
persona = {"nombre": "Luis", "edad": 30, "ciudad": "Madrid"}
print(persona["nombre"], persona["edad"], persona["ciudad"])

# Ejercicio 2: Añadir y modificar
# Dado usuario = {"nombre": "Ana"}
# Añade las claves "email" y "edad". Luego modifica "edad".
usuario = {"nombre": "Ana"}
usuario["email"] = "ana@email.com"
usuario["edad"] = 25
usuario["edad"] = 26
print(usuario)

# Ejercicio 3: Métodos del diccionario
# Dado inventario = {"manzanas": 5, "peras": 3, "uvas": 12}
# Usa .keys(), .values(), .items() para mostrar cada componente.
inv = {"manzanas": 5, "peras": 3, "uvas": 12}
print("Keys:", list(inv.keys()))
print("Values:", list(inv.values()))
print("Items:", list(inv.items()))

# Ejercicio 4: Verificar existencia
# Pide una clave al usuario y verifica si existe en el diccionario usando "in".
d = {"a": 1, "b": 2, "c": 3}
clave = input("Clave a buscar: ")
if clave in d:
    print(f"Existe, valor: {d[clave]}")
else:
    print("No existe")

# Ejercicio 5: Diccionario anidado
# Crea un diccionario estudiantes donde cada clave es un nombre y cada valor
# es otro diccionario con "edad", "nota", "asignaturas" (lista).
# Tu código aquí:

# Ejercicio 6: Iterar diccionario
# Usando el diccionario anterior, itera con for clave, valor in estudiantes.items():
# y muestra toda la información formateada.
# Tu código aquí:

# Ejercicio 7: Frecuencia de palabras
# Pide una frase al usuario y cuenta cuántas veces aparece cada palabra.
# Devuelve un diccionario {palabra: frecuencia}.
# Tu código aquí:

# Ejercicio 8: Merge de diccionarios
# Dados d1 = {"a": 1, "b": 2} y d2 = {"c": 3, "d": 4}
# Combínalos en un solo diccionario usando update().
# Tu código aquí:
