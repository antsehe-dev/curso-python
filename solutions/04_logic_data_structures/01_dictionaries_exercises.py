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
estudiantes = {
    "Luis": {"edad": 28, "nota": 8.5, "asignaturas": ["Matemáticas", "Física"]},
    "Ana": {"edad": 22, "nota": 9.2, "asignaturas": ["Literatura", "Historia"]},
    "Carlos": {"edad": 25, "nota": 7.8, "asignaturas": ["Química", "Biología"]}
}

# Ejercicio 6: Iterar diccionario
# Usando el diccionario anterior, itera con for clave, valor in estudiantes.items():
# y muestra toda la información formateada.
for nombre, info in estudiantes.items():
    print(f"Nombre: {nombre}")
    print(f"Edad: {info['edad']}")
    print(f"Nota: {info['nota']}")
    print(f"Asignaturas: {', '.join(info['asignaturas'])}")
    print()

# Ejercicio 7: Frecuencia de palabras
# Pide una frase al usuario y cuenta cuántas veces aparece cada palabra.
# Devuelve un diccionario {palabra: frecuencia}.
phrase = input("Introduce una frase: ")

frecuencia = {}
import string

for palabra in phrase.lower().split():
    palabra = palabra.strip(string.punctuation + "¿¡")
    if not palabra:
        continue
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)  
    

# Ejercicio 8: Merge de diccionarios
# Dados d1 = {"a": 1, "b": 2} y d2 = {"c": 3, "d": 4}
# Combínalos en un solo diccionario usando update().
d1 = {"a": 1, "b": 2} 
d2 = {"c": 3, "d": 4} 

d1.update(d2)
print(d1)
