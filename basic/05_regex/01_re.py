###
# 01 - Expresiones regulares
###

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """

# 1: Importar re
import re

# 2: Crear un patron
pattern = "Hola"

# 3: El texto en el que queremos buscar
text = "Hola mundo"

# 4: Usar funcion de busquedad de "re"
result = re.search(pattern,text)

if result:
    print("He encontrado el patrón en el texto")
else:
    print("No he encontrado el patrón en el texto")
    
# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start(), end() devolver la posicion inicial o final de la coincidencia
print(result.start(), result.end())

# Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias
text = "Me gusta Python. Python es lo maximo. Aunque Pyhhon no es tan dificil, ojo con Python"
pattern = "Py.hon"

matches = re.findall(pattern,text)

print(matches)


# ----------------------------


# iter()
matches=re.finditer(pattern,text)

for match in matches:
    print(match.group(), match.start(), match.end())

## Sustituir texto, re.sub()
text = "Hola Antonio, que tal estas?"
pattern = "Hola"
replacement= "Adios"

next_text = re.sub(pattern,replacement,text)

print(next_text)