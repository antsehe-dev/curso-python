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
# Tu código aquí:

# Ejercicio 6: Leer y filtrar
# Lee data/productos.json, filtra los productos con precio < 50 y muéstralos.
# Tu código aquí:

# Ejercicio 7: ensure_ascii
# Guarda un diccionario con caracteres especiales (ñ, tildes) en un archivo JSON.
# Pruébalo con ensure_ascii=True y ensure_ascii=False. Compara los archivos.
# Tu código aquí:
