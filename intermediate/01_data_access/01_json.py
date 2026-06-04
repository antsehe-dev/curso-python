###
# 01 - Leer y escribir JSON
###
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Escribir JSON
data = {
    "usuarios": [
        {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": True},
        {"id": 2, "nombre": "Luis", "email": "luis@example.com", "activo": False},
        {"id": 3, "nombre": "Sofía", "email": "sofia@example.com", "activo": True},
    ]
}

with open(DATA_DIR / "usuarios.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Leer JSON
with open(DATA_DIR / "usuarios.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Usuarios cargados:")
for usuario in loaded["usuarios"]:
    print(f"  {usuario['id']}: {usuario['nombre']} - {'activo' if usuario['activo'] else 'inactivo'}")

# json.dumps / json.loads (strings, no archivos)
cadena = json.dumps(data, indent=2)
diccionario = json.loads(cadena)
