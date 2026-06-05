"""
EJERCICIOS: SQLite - Bases de datos
Nivel: Intermedio-Avanzado
"""

import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "ejercicios.db"

# Ejercicio 1: Crear tabla
# Conecta a la base de datos (crea ejercicios.db).
# Crea una tabla "productos" con: id (INTEGER PRIMARY KEY), nombre (TEXT),
# precio (REAL), stock (INTEGER).
conn = sqlite3.connect(str(DB_PATH))
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
""")
conn.commit()

# Ejercicio 2: Insertar datos
# Inserta 5 productos en la tabla con INSERT.
# Usa parámetros con ? para evitar SQL injection.
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Portátil", 999.99, 15))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Ratón", 29.99, 50))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Teclado", 49.99, 30))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Monitor", 199.99, 10))
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Auriculares", 79.99, 25))
conn.commit()

# Ejercicio 3: Insertar múltiples filas
# Usa executemany() para insertar una lista de productos de una sola vez.
nuevos_productos = [
    ("Webcam", 59.99, 20),
    ("Altavoz", 39.99, 35),
    ("Disco SSD", 89.99, 40)
]
cursor.executemany("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", nuevos_productos)
conn.commit()

# Ejercicio 4: SELECT básico
# Selecciona y muestra todos los productos con precio > 20.
cursor.execute("SELECT * FROM productos WHERE precio > 20")
for fila in cursor.fetchall():
    print(fila)

# Ejercicio 5: Actualizar datos
# Actualiza el stock de un producto específico usando UPDATE con WHERE.
cursor.execute("UPDATE productos SET stock = 100 WHERE nombre = ?", ("Ratón",))
conn.commit()

# Ejercicio 6: Eliminar datos
# Elimina los productos con stock = 0 usando DELETE.
cursor.execute("DELETE FROM productos WHERE stock = 0")
conn.commit()

# Ejercicio 7: Row factory
# Configura row_factory = sqlite3.Row para acceder a las columnas por nombre.
# Selecciona todos los productos y muéstralos como si fueran diccionarios.
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM productos")
for fila in cursor.fetchall():
    print(dict(fila))

# Ejercicio 8: lastrowid
# Inserta un nuevo producto y muestra su id generado con cursor.lastrowid.
cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Tablet", 299.99, 12))
conn.commit()
print(f"Nuevo producto insertado con id: {cursor.lastrowid}")

# Ejercicio 9: Transacción
# Crea una función transferir_stock(origen_id, destino_id, cantidad) que:
# - Reduzca el stock del producto origen
# - Aumente el stock del producto destino
# - Use commit() para hacer la transacción atómica
def transferir_stock(origen_id, destino_id, cantidad):
    try:
        cursor.execute("UPDATE productos SET stock = stock - ? WHERE id = ? AND stock >= ?", (cantidad, origen_id, cantidad))
        if cursor.rowcount == 0:
            raise ValueError("Stock insuficiente o producto no encontrado")
        cursor.execute("UPDATE productos SET stock = stock + ? WHERE id = ?", (cantidad, destino_id))
        conn.commit()
        print(f"Transferencia de {cantidad} unidades de {origen_id} a {destino_id} completada")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

transferir_stock(1, 2, 3)

# Ejercicio 10: Sistema de tareas completo
# Implementa un gestor de tareas en SQLite con las operaciones:
# - Crear tarea (descripción, fecha_limite)
# - Listar tareas pendientes
# - Marcar tarea como completada
# - Eliminar tarea
# Usa un menú interactivo.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY,
        descripcion TEXT NOT NULL,
        fecha_limite TEXT,
        completada INTEGER DEFAULT 0
    )
""")
conn.commit()

def menu_tareas():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Crear tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            desc = input("Descripción: ")
            fecha = input("Fecha límite (DD/MM/AAAA): ")
            cursor.execute("INSERT INTO tareas (descripcion, fecha_limite) VALUES (?, ?)", (desc, fecha))
            conn.commit()
            print("Tarea creada")
        elif opcion == "2":
            cursor.execute("SELECT * FROM tareas WHERE completada = 0")
            for t in cursor.fetchall():
                print(f"{t[0]}. {t[1]} (límite: {t[2]})")
        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (id_tarea,))
            conn.commit()
            print("Tarea completada")
        elif opcion == "4":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
            conn.commit()
            print("Tarea eliminada")
        elif opcion == "5":
            break

conn.close()
