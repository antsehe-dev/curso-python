"""
EJERCICIOS: Tuplas
Nivel: Básico-Intermedio
"""

# Ejercicio 1: Creación y acceso
# Crea una tupla con los meses del año. Accede al primer y último mes.
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
print(meses[0], meses[-1])

# Ejercicio 2: Inmutabilidad
# Crea una tupla y demuestra que no se puede modificar (intenta cambiar un elemento).
# Usa try/except para capturar el error.
t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as e:
    print(f"Error: {e}")

# Ejercicio 3: Desempaquetado
# Dada tupla coordenadas = (latitud, longitud, altitud) = (40.41, -3.70, 650)
# Desempaqueta en tres variables e imprime cada una.
coordenadas = (40.41, -3.70, 650)
latitud, longitud, altitud = coordenadas
print(f"Lat: {latitud}, Lon: {longitud}, Alt: {altitud}")

# Ejercicio 4: Tupla como clave de diccionario
# Crea un diccionario donde las claves sean tuplas (x, y) y los valores sean nombres de ciudades.
# Ej: {(40.41, -3.70): "Madrid", (48.85, 2.35): "París"}
ciudades = {
    (40.41, -3.70): "Madrid",
    (48.85, 2.35): "París",
    (41.38, 2.17): "Barcelona"
}
print(ciudades)

# Ejercicio 5: count() e index()
# Dada tupla numeros = (1, 2, 3, 2, 4, 2, 5)
# Cuenta cuántas veces aparece el 2. Encuentra el índice de la primera ocurrencia del 4.
numeros = (1, 2, 3, 2, 4, 2, 5)

print(numeros.count(2))
print(numeros.index(4))


# Ejercicio 6: Lista de tuplas
# Crea una lista de tuplas con nombres y edades: [("Ana", 25), ("Luis", 30), ("Sofía", 22)]
# Itera e imprime "Nombre tiene X años".
nombres_edades = [("Ana", 25), ("Luis", 30), ("Sofía", 22)]
for nombre, edad in nombres_edades:
    print(f"{nombre} tiene {edad} años")


# Ejercicio 7: Comparar listas vs tuplas
# Crea una lista y una tupla con los mismos elementos. Muestra sus tipos y
# demuestra que la lista es mutable y la tupla inmutable.
lista = [1, 2, 3]
tupla = (1, 2, 3)
print(f"Lista: {lista}, Tipo: {type(lista)}")
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")
try:
    lista[0] = 99
    print(f"Lista modificada: {lista}")
except TypeError as e:
    print(f"Error al modificar lista: {e}")
try:
    tupla[0] = 99
except TypeError as e:
    print(f"Error al modificar tupla: {e}")
