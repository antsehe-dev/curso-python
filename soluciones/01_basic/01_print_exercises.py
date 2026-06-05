"""
EJERCICIOS: print() y f-strings
Nivel: Básico
"""

# Ejercicio 1: Saludo personalizado
# Usa print() para mostrar "¡Hola, Mundo!" en la consola.
print("¡Hola, Mundo!")

# Ejercicio 2: Separador personalizado
# Usa print() con el parámetro sep para mostrar los números 1, 2, 3 separados por " - "
# Resultado esperado: 1 - 2 - 3
print(1, 2, 3, sep=" - ")

# Ejercicio 3: Sin salto de línea
# Usa print() con el parámetro end para imprimir "Hola " y "Mundo" en la misma línea.
print("Hola ", end=" ")
print("Mundo")

# Ejercicio 4: f-strings
# Crea una variable nombre = "Ana" y otra edad = 25.
# Usa un f-string para imprimir: "Me llamo Ana y tengo 25 años."
nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años")

# Ejercicio 5: Formateo avanzado
# Dado precio = 19.99 y producto = "camiseta", usa un f-string para mostrar:
# "La camiseta cuesta 19.99€"
precio, producto = 19.99, "camiseta"

print(f"La {producto} cuesta {precio} €")

# Ejercicio 6: Múltiples variables
# Define tres variables (ciudad, pais, habitantes) e imprime una frase usando f-string.
ciudad, pais, habitantes = "Cordoba", "España", 300000

print(f"En {ciudad} hay aproximadamente {habitantes} habitantes y está ubicada en {pais}.")
