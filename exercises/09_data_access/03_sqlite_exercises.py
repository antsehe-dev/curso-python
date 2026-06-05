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
# Tu código aquí:

# Ejercicio 2: Insertar datos
# Inserta 5 productos en la tabla con INSERT.
# Usa parámetros con ? para evitar SQL injection.
# Tu código aquí:

# Ejercicio 3: Insertar múltiples filas
# Usa executemany() para insertar una lista de productos de una sola vez.
# Tu código aquí:

# Ejercicio 4: SELECT básico
# Selecciona y muestra todos los productos con precio > 20.
# Tu código aquí:

# Ejercicio 5: Actualizar datos
# Actualiza el stock de un producto específico usando UPDATE con WHERE.
# Tu código aquí:

# Ejercicio 6: Eliminar datos
# Elimina los productos con stock = 0 usando DELETE.
# Tu código aquí:

# Ejercicio 7: Row factory
# Configura row_factory = sqlite3.Row para acceder a las columnas por nombre.
# Selecciona todos los productos y muéstralos como si fueran diccionarios.
# Tu código aquí:

# Ejercicio 8: lastrowid
# Inserta un nuevo producto y muestra su id generado con cursor.lastrowid.
# Tu código aquí:

# Ejercicio 9: Transacción
# Crea una función transferir_stock(origen_id, destino_id, cantidad) que:
# - Reduzca el stock del producto origen
# - Aumente el stock del producto destino
# - Use commit() para hacer la transacción atómica
# Tu código aquí:

# Ejercicio 10: Sistema de tareas completo
# Implementa un gestor de tareas en SQLite con las operaciones:
# - Crear tarea (descripción, fecha_limite)
# - Listar tareas pendientes
# - Marcar tarea como completada
# - Eliminar tarea
# Usa un menú interactivo.
# Tu código aquí:
