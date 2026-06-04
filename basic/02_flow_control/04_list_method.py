###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)

# Eliminar por lo bestia un índice
del lista1[-1]

lista1.clear() # Eliminar todos los elementos de la lista

# Eliminar un rango de elementos
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3)
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

