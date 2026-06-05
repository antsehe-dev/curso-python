"""
EJERCICIOS: input() e interacción con usuario
Nivel: Básico
"""

# Ejercicio 1: Saludo personalizado
# Pide al usuario su nombre y muestra "¡Hola, [nombre]!".
nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}!")

# Ejercicio 2: Calculadora de edad
# Pide al usuario su año de nacimiento y calcula cuántos años tiene o tendrá este año.
nacimiento = int(input("¿En qué año naciste? "))
edad = 2026 - nacimiento
print(f"Tienes {edad} años.")

# Ejercicio 3: Suma de dos números
# Pide dos números al usuario (como input), conviértelos a int y muestra la suma.
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print(f"La suma es: {a + b}")

# Ejercicio 4: Dividir input en partes
# Pide al usuario tres palabras separadas por espacio.
# Usa .split() para separarlas y muestra cada una en una línea.
palabras = input("Escribe tres palabras separadas por espacio: ").split()
for i, p in enumerate(palabras, 1):
    print(f"{i}. {p}")

# Ejercicio 5: Calculadora de propina
# Pide el total de la cuenta (float) y el porcentaje de propina (int).
# Calcula y muestra: "Propina: X€ - Total: Y€"
total = float(input("Total de la cuenta (€): "))
porcentaje = int(input("Porcentaje de propina: "))
propina = total * porcentaje / 100
print(f"Propina: {propina:.2f}€ - Total: {total + propina:.2f}€")

# Ejercicio 6: Conversor de unidades
# Pide una distancia en kilómetros y conviértela a millas (1 km = 0.621371 millas).
# Muestra el resultado con 2 decimales.
km = float(input("Distancia en kilómetros: "))
millas = km * 0.621371
print(f"{km} km son {millas:.2f} millas")
