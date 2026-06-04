###
# 03 - Base de datos SQLite
###
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "tienda.db"

# 1. Conectar (crea la DB si no existe)
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 2. Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        creado_en TEXT DEFAULT CURRENT_TIMESTAMP
    )
""")

# 3. Insertar
cursor.execute(
    "INSERT INTO clientes (nombre, email) VALUES (?, ?)",
    ("Carlos", "carlos@example.com"),
)
conn.commit()
print(f"Insertado: {cursor.lastrowid}")

# 4. Insertar varios
clientes = [
    ("María", "maria@example.com"),
    ("Pedro", "pedro@example.com"),
    ("Laura", "laura@example.com"),
]
cursor.executemany(
    "INSERT OR IGNORE INTO clientes (nombre, email) VALUES (?, ?)", clientes
)
conn.commit()

# 5. Consultar
cursor.execute("SELECT id, nombre, email, creado_en FROM clientes")
for fila in cursor.fetchall():
    print(f"{fila['id']}: {fila['nombre']} <{fila['email']}> ({fila['creado_en']})")

# 6. Actualizar
cursor.execute(
    "UPDATE clientes SET email = ? WHERE nombre = ?",
    ("carlos.nuevo@example.com", "Carlos"),
)
conn.commit()

# 7. Eliminar
cursor.execute("DELETE FROM clientes WHERE nombre = ?", ("Laura",))
conn.commit()

conn.close()
