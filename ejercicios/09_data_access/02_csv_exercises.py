"""
EJERCICIOS: CSV - Lectura y escritura
Nivel: Intermedio
"""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Ejercicio 1: Escribir CSV
# Crea un archivo data/alumnos.csv con las columnas: nombre, edad, nota
# y 3 filas de datos. Usa csv.writer() y writer.writerow().
# Tu código aquí:

# Ejercicio 2: Leer CSV
# Lee el archivo data/alumnos.csv con csv.reader() y muestra cada fila.
# Tu código aquí:

# Ejercicio 3: DictWriter
# Usa csv.DictWriter para escribir un CSV con fieldnames y writer.writerow(diccionario).
# Crea data/empleados.csv con columnas: id, nombre, departamento, salario.
# Tu código aquí:

# Ejercicio 4: DictReader
# Lee data/empleados.csv con csv.DictReader() y muestra el nombre de cada empleado.
# Tu código aquí:

# Ejercicio 5: Procesar CSV
# Dado el siguiente CSV como string (simulado), cárgalo y calcula el salario medio:
csv_data = """nombre,departamento,salario
Ana,Ventas,35000
Luis,IT,42000
Sofia,IT,38000
Carlos,Ventas,31000
"""
# Pista: usa csv.DictReader sobre csv_data.splitlines()
# Tu código aquí:

# Ejercicio 6: Añadir fila a CSV existente
# Abre data/empleados.csv en modo append ('a', newline='') y añade un nuevo empleado.
# Tu código aquí:

# Ejercicio 7: Filtrar CSV
# Lee data/empleados.csv y crea un nuevo archivo data/it_empleados.csv
# solo con los empleados del departamento "IT".
# Tu código aquí:
