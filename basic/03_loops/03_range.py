###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

print("\nRange(): ")

# Secuencia del 0 al 9
for i in range(10):
    print(i, end=" ")
print(" ")


# Range (inicio, fin)
for num in range (5,10): #de 5 a 9
    print(num, end=" ")
print()

# Range (inicio, fin, paso)
for num in range (0,20,2): # de 0 a 19, de 2 en dos
    print(num, end=" ")
print() 

# Casos especiales
for num in range(-5, 0):
    print(num, end=" ")
print()
for num in range(10, 0, -1):
    print(num, end=" ")
print()

# Usar range para rellenar lista
list_of_nums = list(range(10))
print(list_of_nums)

# Hacer 5 veces algo
for i in range(5):
    print(f"Vez nº: {i+1}")


###
# EJERCICIOS (range)
###

print("\n--------------------------")
print("EJERCICIOS: ")

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for i in range(10): print(f"{i+1}",end=" ")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
impares = [num for num in range(1,21) if num%2!=0]
print(impares)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for i in range (1,51):
    if i%5==0:
        print(i, end=" ")
print()

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for i in range (10,0,-1):
    print(i, end=" ")
print()
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
sum = 0
for i in range(1,101):
    sum += i
print(sum)
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
num_usuario = int(input("Introduce un numero y veras su tabla de multiplicar: "))
for i in range(1,11):
    print(f"{num_usuario} X {i} = {num_usuario * i}")


