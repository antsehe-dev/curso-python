###
# 06 - Estructura de datos en python: Listas, Diccionarios y Tuplas
###

# 1. Listas -> []
# Coleccion ordenada y mutable de elementos
print("="*50)
print("1. Listas")
frutas = ["pera", "melocotón", "manzana"]

# Acceder a elementos
print(frutas[0])  # pera
# Modificar elementos
frutas[1] = "naranja"
# Agregar elementos
frutas.append("plátano")
# Eliminar elementos
frutas.remove("manzana")
ultimo = frutas.pop()  # Elimina el último elemento y lo devuelve
# Buscar y ordenar elementos
print("naranja" in frutas)  # True
frutas.sort()  # Ordena la lista alfabéticamente
sorted_frutas = sorted(frutas)  # Devuelve una nueva lista ordenada
len_frutas = len(frutas)  # Número de elementos en la lista

# List comprehension
cuadrados = [x**2 for x in range(10)]  # Crea una lista de cuadrados del 0 al 9
print("Cuadrados:", cuadrados)

# 2. Tuplas -> ()
# Colección ordenada e inmutable de elementos
print("="*50)
print("2. Tuplas")
coordenadas = (10.0, 20.0)
unitaria = (42,)  # Tupla de un solo elemento, coma necesaria para diferenciar de un valor entre paréntesis
# Acceder a elementos igual que en listas
print(coordenadas[0])  # 10.0
# Asignar tupla a variables
x, y = coordenadas

# Metodos disponibles para tuplas
print("count:", coordenadas.count(10.0))  # Cuenta cuántas veces aparece un valor
print("index:", coordenadas.index(20.0))  # Devuelve el índice de un valor

# Tuplas son hashables, por lo que pueden ser usadas como claves en diccionarios o elementos de sets
mapa = {(0, 0): "origen", (1, 1): "punto1"}

# 3. Diccionarios -> {}
# Colección no ordenada de pares clave-valor
print("="*50)
print("3. Diccionarios")
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    'calificaciones': [8, 9, 10]
}
# Mirar en la clase 04_diccionarios.py para más ejemplos de diccionarios

nombre = persona["nombre"]  # Acceder a un valor por su clave

persona['last']=10

print(persona)