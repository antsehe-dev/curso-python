"""
EJERCICIOS: Listas - creación, indexación, slicing
Nivel: Básico
"""

# Ejercicio 1: Creación y acceso
# Crea una lista con los días de la semana. Imprime el primer y el último elemento.
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
print("Primer día:", dias[0])
print("Último día:", dias[-1])

# Ejercicio 2: Indexación negativa
# Dada la lista colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
# Usa indexación negativa para obtener el último y el penúltimo elemento.
colores = ["rojo", "verde", "azul", "amarillo", "naranja"]
print("Último:", colores[-1])
print("Penúltimo:", colores[-2])

# Ejercicio 3: Slicing básico
# Dada la lista numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Obtén: primeros 3, del 3 al 6, los pares (cada 2), la lista invertida.
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Primeros 3:", nums[:3])
print("Del 3 al 6:", nums[3:7])
print("Pares:", nums[::2])
print("Invertida:", nums[::-1])

# Ejercicio 4: Modificación por índice
# Crea una lista con 5 números. Cambia el valor del índice 2 por 100.
# Luego cambia los valores del índice 1 al 3 por [50, 60, 70].
nums2 = [1, 2, 3, 4, 5]
nums2[2] = 100
print(nums2)
nums2[1:4] = [50, 60, 70]
print(nums2)

# Ejercicio 5: Concatenación
# Crea dos listas de números y concaténalas usando + y +=. Muestra los resultados.
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenada = lista1 + lista2
print("Con +:", concatenada)
lista1 += lista2
print("Con +=:", lista1)

# Ejercicio 6: Longitud
# Pide al usuario 5 palabras y guárdalas en una lista. Muestra cuántas palabras introdujo.
# Tu código aquí:
