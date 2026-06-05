"""
EJERCICIOS: Bucle for, enumerate, list comprehensions
Nivel: Básico-Intermedio
"""

# Ejercicio 1: Iterar lista
# Dada frutas = ["manzana", "pera", "uva", "naranja", "sandía"]
# Itera con for e imprime cada fruta.
frutas = ["manzana", "pera", "uva", "naranja", "sandía"]
for f in frutas:
    print(f)

# Ejercicio 2: enumerate
# Usa enumerate() para iterar la lista anterior mostrando:
# "0: manzana, 1: pera, ..."
for i, f in enumerate(frutas):
    print(f"{i}: {f}")

# Ejercicio 3: Nested loop (matriz)
# Dada matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Itera con un for anidado e imprime todos los elementos en formato de matriz.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elem in fila:
        print(elem, end=" ")
    print()

# Ejercicio 4: List comprehension básica
# Crea una lista con los cuadrados de los números del 1 al 10 usando list comprehension.
cuadrados = [n**2 for n in range(1, 11)]
print(cuadrados)

# Ejercicio 5: List comprehension con filtro
# Dada una lista de números, crea una nueva lista solo con los pares usando comprehension.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in nums if n % 2 == 0]
print(pares)

# Ejercicio 6: for con strings
# Pide una frase al usuario. Cuenta cuántas vocales tiene (a, e, i, o, u).
# Tu código aquí:

# Ejercicio 7: FizzBuzz
# Imprime los números del 1 al 100, pero:
# - Si es múltiplo de 3: "Fizz"
# - Si es múltiplo de 5: "Buzz"
# - Si es múltiplo de 3 y 5: "FizzBuzz"
# Tu código aquí:

# Ejercicio 8: Comprehension con strings
# Dada una lista de palabras, crea una nueva lista con las palabras que tengan más de 5 letras.
# Tu código aquí:

# Ejercicio 9: Anagramas
# Pide dos palabras y determina si son anagramas (tienen las mismas letras).
# Pista: sorted(palabra1) == sorted(palabra2)
# Tu código aquí:
