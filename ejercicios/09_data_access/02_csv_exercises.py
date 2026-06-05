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
with open(DATA_DIR / "alumnos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "edad", "nota"])
    w.writerow(["Ana", 25, 8.5])
    w.writerow(["Luis", 30, 7.0])
    w.writerow(["Sofia", 22, 9.2])
print("CSV creado")

# Ejercicio 2: Leer CSV
# Lee el archivo data/alumnos.csv con csv.reader() y muestra cada fila.
with open(DATA_DIR / "alumnos.csv", "r", newline="", encoding="utf-8") as f:
    for fila in csv.reader(f):
        print(fila)

# Ejercicio 3: DictWriter
# Usa csv.DictWriter para escribir un CSV con fieldnames y writer.writerow(diccionario).
# Crea data/empleados.csv con columnas: id, nombre, departamento, salario.
with open(DATA_DIR / "empleados.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["id", "nombre", "departamento", "salario"]
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerow({"id": 1, "nombre": "Ana", "departamento": "IT", "salario": 45000})
    w.writerow({"id": 2, "nombre": "Luis", "departamento": "Ventas", "salario": 35000})

# Ejercicio 4: DictReader
# Lee data/empleados.csv con csv.DictReader() y muestra el nombre de cada empleado.
with open(DATA_DIR / "empleados.csv", "r", newline="", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"])

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
