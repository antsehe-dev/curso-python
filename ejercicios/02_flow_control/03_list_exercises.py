"""
EJERCICIOS: Listas - creación, indexación, slicing
Nivel: Básico
"""

# Ejercicio 1: Creación y acceso
# Crea una lista con los días de la semana. Imprime el primer y el último elemento.
week_list = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print("Primer dia de la semana:",week_list[0])
print(f"Ultimo dia de la semana: {week_list[-1]}")

# Ejercicio 2: Indexación negativa
# Dada la lista colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
# Usa indexación negativa para obtener el último y el penúltimo elemento.
colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
print(f"Este es el ultimo color: {colores[-1]} y este el penultimo: {colores[-2]}")

# Ejercicio 3: Slicing básico
# Dada la lista numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Obtén: primeros 3, del 3 al 6, los pares (cada 2), la lista invertida.
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Tres primeros: {numeros[:3]} ")
print(f"Del 3 al 6: {numeros[3:6]} ")
print(f"Los pares: {numeros[::2]} ")
print(f"Invertida: {numeros[::-1]} ")


# Ejercicio 4: Modificación por índice
# Crea una lista con 5 números. Cambia el valor del índice 2 por 100.
# Luego cambia los valores del índice 1 al 3 por [50, 60, 70].
numeros = [0, 1, 2, 3, 4]
numeros[:3]=[50,60,70]
print(numeros)
    


# Ejercicio 5: Concatenación
# Crea dos listas de números y concaténalas usando + y +=. Muestra los resultados.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Concatenación con +:", list1 + list2)
list1 += list2
print("Concatenación con +=:", list1)
print("El resultado de list1 después de += es el mismo que list1 + list2, pero list1 se ha modificado en lugar de crear una nueva lista.")

# Ejercicio 6: Longitud
# Pide al usuario 5 palabras y guárdalas en una lista. Muestra cuántas palabras introdujo.
# Tu código aquí:
palabras = [input("Palabra 1: "), input("Palabra 2: "), input("Palabra 3: "), input("Palabra 4: "), input("Palabra 5: ")]
print(f"Has introducido {len(palabras)} palabras.")
