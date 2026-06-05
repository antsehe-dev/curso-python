"""
EJERCICIOS: Bucle while
Nivel: Básico
"""

# Ejercicio 1: Contador
# Usa un bucle while para imprimir los números del 1 al 10.
# Tu código aquí:
max = 10
contador = 1
while contador <= max:
    if contador == max:
        print(contador)
    else: 
        print(contador, end= ", ")
    contador += 1
# Ejercicio 2: Suma acumulada
# Pide números al usuario hasta que ingrese 0. Muestra la suma total.
# Tu código aquí:
sum = 0
while True:
    num = int(input("Introduce un numero (0 para salir):"))
    if num == 0:
        print("Saliendo...")
        break
    sum += num
    print(f"Suma actual: {sum}, ultimo numero sumado: {num}")
    
# Ejercicio 3: Número secreto
# Genera un número aleatorio entre 1 y 10. El usuario debe adivinarlo.
# Dale pistas de "mayor" o "menor" hasta que acierte. Usa import random.
# Tu código aquí:
import random
num_aleatorio = random.randint(1,10)

while True:
    num = int(input("Introduce un numero:"))
    if num <1 or num>10:
        print("El numero esta entre 1 y 10")
    else:
        if num == num_aleatorio:
            print(f"Adivinaste el numero {num_aleatorio}")
            break
        else:
            print(f"No adivinaste el numero aleatorio  {num_aleatorio}")
# Ejercicio 4: break
# Pide palabras al usuario. Si escribe "salir", termina el bucle.
# Muestra cuántas palabras introdujo (sin contar "salir").
# Tu código aquí:
contador = 0

while True:
    words = input('Introduce una palabra ("salir" para terminar): ')
    if(words.lower() == "salir"):
        print("Saliendo...")
        break
    contador +=1
    print(f"Ahora llevas un total de {contador} palabras")
    


# Ejercicio 5: continue
# Imprime los números del 1 al 20, pero salta los múltiplos de 3 con continue.
# Tu código aquí:


# Ejercicio 6: while...else
# Pide al usuario que introduzca una contraseña correcta ("python123").
# Usa while...else para mostrar "Acceso concedido" si acierta,
# o "Cuenta bloqueada" si falla 3 intentos.
# Tu código aquí:

# Ejercicio 7: Secuencia Fibonacci
# Genera los primeros N términos de la secuencia Fibonacci usando while.
# Pide N al usuario.
# Tu código aquí:
