"""
EJERCICIOS: Expresiones regulares (re)
Nivel: Intermedio
"""

import re

# Ejercicio 1: Buscar patrón
# Dado el texto "Mi correo es usuario@example.com y otro es test@test.org"
# Usa re.search() para encontrar el primer correo electrónico.
# Patrón: r'\S+@\S+\.\S+'
texto = "Mi correo es usuario@example.com y otro es test@test.org"
match = re.search(r'\S+@\S+\.\S+', texto)
print(match.group())

# Ejercicio 2: Extraer todos
# Del mismo texto anterior, usa re.findall() para extraer TODOS los correos.
correos = re.findall(r'\S+@\S+\.\S+', texto)
print(correos)

# Ejercicio 3: Grupos
# Dado el texto "Fecha: 15/03/2024", usa re.search() con grupos
# para extraer día, mes y año por separado. Patrón: r'(\d{2})/(\d{2})/(\d{4})'
fecha = "Fecha: 15/03/2024"
m = re.search(r'(\d{2})/(\d{2})/(\d{4})', fecha)
print(f"Día: {m.group(1)}, Mes: {m.group(2)}, Año: {m.group(3)}")

# Ejercicio 4: Reemplazar
# Dado "Hola, mi número es 123-456-789. Llámame."
# Usa re.sub() para reemplazar el patrón de teléfono por "[OCULTO]".
# Patrón: r'\d{3}-\d{3}-\d{3}'
t = "Hola, mi número es 123-456-789. Llámame."
resultado = re.sub(r'\d{3}-\d{3}-\d{3}', '[OCULTO]', t)
print(resultado)

# Ejercicio 5: Validar formato
# Pide al usuario un número de teléfono en formato "+34 612345678" y valida
# que cumpla el patrón. Usa re.fullmatch().
# Patrón: r'^\+34 \d{9}$'
telefono = input("Introduce un teléfono (+34 612345678): ")
if re.fullmatch(r'^\+34 \d{9}$', telefono):
    print("Teléfono válido")
else:
    print("Teléfono no válido")

# Ejercicio 6: Extraer URLs
# Dado un texto con URLs como "Visita https://ejemplo.com o http://test.org/path"
# Extrae todas las URLs. Patrón: r'https?://\S+'
texto_urls = "Visita https://ejemplo.com o http://test.org/path"
urls = re.findall(r'https?://\S+', texto_urls)
print(urls)

# Ejercicio 7: Palabras con mayúscula
# Dado un texto, encuentra todas las palabras que empiezan con mayúscula.
# Patrón: r'\b[A-ZÁÉÍÓÚÑ]\w*'
texto_mayus = "Hoy es Martes y Ana fue a Barcelona"
mayusculas = re.findall(r'\b[A-ZÁÉÍÓÚÑ]\w*', texto_mayus)
print(mayusculas)
