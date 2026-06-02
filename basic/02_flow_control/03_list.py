###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos
###

# Creación de listas []
list = [1,2,3,4,5]
list_string = ["manzanas","peras","platanos"]
list_var = [1,"hola",True,None,2.5]
matrix = [[1,2],[2,3],[3,4],[4,5]]

# Acceso a elementos por indice
print(list_string[0]) #manzanas
print(list_string[-1]) #platanos
print(matrix[1][1]) #3

# Slicing (rebanado) de listas
print(list[1:4]) #[2,3,4]
print(list[:3]) # [1, 2, 3]
print(list[3:]) # [4, 5]
print(list[:]) # [1, 2, 3, 4, 5]

list = [1, 2, 3, 4, 5, 6, 7, 8]
print(list[::2]) # para devolver índices pares
print(list[::-1]) # para devolver índices inversos

# Modificar una lista
list[0] = 20
print(list)

# Añadir elementos a una lista
list = [1, 2, 3]

# forma larga y menos eficiente
list = list + [4, 5, 6]
print(list)

# forma corta y más eficiente
list += [7, 8, 9]
print(list)

# Recuperar longitud de una lista
print("Longitud de la lista", len(list))
