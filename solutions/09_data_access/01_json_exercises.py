"""
EJERCICIOS: JSON - Lectura y escritura
Nivel: Intermedio
"""

import json
from pathlib import Path

# Configuración: carpeta para guardar archivos
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Ejercicio 1: Serializar a JSON
# Crea un diccionario con datos de una persona (nombre, edad, hobbies, dirección).
# Usa json.dumps() para convertirlo a string JSON con indent=2.
persona = {"nombre": "Ana", "edad": 28, "hobbies": ["leer", "correr"], "direccion": {"ciudad": "Madrid", "cp": 28001}}
print(json.dumps(persona, indent=2))

# Ejercicio 2: Guardar JSON a archivo
# Usa el diccionario anterior y json.dump() para guardarlo en data/persona.json.
with open(DATA_DIR / "persona.json", "w", encoding="utf-8") as f:
    json.dump(persona, f, indent=2, ensure_ascii=False)

# Ejercicio 3: Leer JSON de archivo
# Lee el archivo data/persona.json con json.load() y muestra el contenido.
with open(DATA_DIR / "persona.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
print(datos)

# Ejercicio 4: JSON desde string
# Dado el string JSON, cárgalo con json.loads() y accede al campo "precio".
json_str = '{"producto": "Portátil", "precio": 999.99, "stock": 15}'
obj = json.loads(json_str)
print("Precio:", obj["precio"])

# Ejercicio 5: Lista de objetos a JSON
# Crea una lista de 3 diccionarios (productos) y guárdalos en data/productos.json.
productos = [
    {"nombre": "Portátil", "precio": 999.99, "stock": 15},
    {"nombre": "Ratón", "precio": 29.99, "stock": 50},
    {"nombre": "Teclado", "precio": 49.99, "stock": 30}
]
with open(DATA_DIR / "productos.json", "w", encoding="utf-8") as f:
    json.dump(productos, f, indent=2, ensure_ascii=False)

# Ejercicio 6: Leer y filtrar
# Lee data/productos.json, filtra los productos con precio < 50 y muéstralos.
with open(DATA_DIR / "productos.json", "r", encoding="utf-8") as f:
    productos = json.load(f)
baratos = [p for p in productos if p["precio"] < 50]
print("Productos con precio < 50:", baratos)

# Ejercicio 7: ensure_ascii
# Guarda un diccionario con caracteres especiales (ñ, tildes) en un archivo JSON.
# Pruébalo con ensure_ascii=True y ensure_ascii=False. Compara los archivos.
datos_especiales = {"nombre": "Muñoz", "descripción": "cañón", "precio": 100}
with open(DATA_DIR / "con_ascii.json", "w", encoding="utf-8") as f:
    json.dump(datos_especiales, f, indent=2, ensure_ascii=True)
with open(DATA_DIR / "sin_ascii.json", "w", encoding="utf-8") as f:
    json.dump(datos_especiales, f, indent=2, ensure_ascii=False)
print("Con ensure_ascii=True:", open(DATA_DIR / "con_ascii.json").read())
print("Con ensure_ascii=False:", open(DATA_DIR / "sin_ascii.json").read())
