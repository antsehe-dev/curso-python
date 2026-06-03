###
# 02 - Bucles for
# Permiten repetir un bloque de código un número específico de veces.
###

print("\nBucle for:")

fruits = ["manzana", "banana", "cereza"]


# Iterar una lista
for fruit in fruits:
  print(fruit)
  
# Iterar todo tipo de iterables
string = "antsehe"
for char in string:
  print(char, end = "")
print("\n")


# Recuperar el indice de cada elemento - enumerate()
for index, fruit in enumerate(fruits):
  print(f"{index}: {fruit}")

# Bucles anidados
matrix =[[1, 2], [3, 4]]
# Iterar una matriz
print("\nMatriz:")
for row in matrix:
  for element in row:
    print(matrix[element], end=" ")
  print()

animales = ["perro","gato","raton","loro","pez","canario"]
# Break
print("\nBreak:")
for animal in animales:
  if animal == "loro":
    break
  print(animal)

# Continue
print("\nContinue:")
for animal in animales:
  if animal == "gato":
    continue
  print(animal)

# Compresion de listas
print("\nCompresión de listas:")
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Mostrar numeros pares de una lista
print("\nPares: ")
pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num%2==0]
print(pares)

###
# EJERCICIOS
###
print("\n-------------------")
print("EJERCICIOS: ")
# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
nums = []
for num in range (2, 21):
  nums.append(num)
  
pares = [num for num in nums if num%2==0]
print(pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
total = 0
for num in numeros:
  total += num

total = total/(len(numeros))

print(total)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

numeros = [15, 5, 25, 10, 20]
num_mayor = 0
for num in numeros:
  if num > num_mayor: num_mayor = num

print(num_mayor)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_5_letras = []

for palabra in palabras:
  contador = 0
  for char in palabra:
    contador +=1
    if contador == 5:
      palabras_5_letras.append(palabra)
      break

print(palabras_5_letras)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Introduce una letra: ")
cant_palabras = 0

for palabra in palabras:
  for char in palabra:
    if letra == char:
      cant_palabras +=1
      break
    else: break
print(cant_palabras)