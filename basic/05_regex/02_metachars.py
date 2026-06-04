###
# 02 - Meta characters
###

import re

# Usar prefijo r para determinar que es una expresion regular
pattern = r"H.la"


# 1. El punto (.)
# El punto coincide con cualquier carácter excepto el salto de línea. Pero solo coincide con un carácter a la vez no varios.
text = "Hola mundo. Hila mundo."
pattern = r"H.la"
result = re.search(pattern,text)
print(result.group())  # Imprime "Hola" y "Hila"

# Para hacer que busque el . se debe usar \. para escapar el punto
pattern = r"\."
result = re.search(pattern,text)
print(result.group())  # Imprime "."

# 2. Buscar un dígito con \d
text = "Mi número de teléfono es 123456789."
result = re.findall( r'\d{9}',text)
print(result)  # Imprime ['1234567890']

# 3. Buscar un espacio en blanco con \s (espacio, tabulación, salto de línea)
text = "Hola mundo. Hila mundo."
result = re.findall(r'\s',text)
print(result)  # Imprime [' ', ' ', ' ', ' ']

# 4. Buscar un carácter alfanumérico con \w (A-Z, a-z, 0-9 y _)
text = "Hola mundo. Hila mundo."
result = re.findall(r'\w',text)
print(result)  # Imprime ['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o', 'H', 'i', 'l', 'a', 'm', 'u', 'n', 'd', 'o']

# 5. ^ y $ para indicar el inicio y el final de una cadena respectivamente
text = "Hola mundo. Hila mundo."
result = re.search(r'^Hola',text)
print(result.group())  # Imprime "Hola"
result = re.search(r'mundo\.$',text)
print(result.group())  # Imprime "mundo."