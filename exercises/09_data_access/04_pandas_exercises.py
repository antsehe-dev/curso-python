"""
EJERCICIOS: Pandas - Análisis de datos
Nivel: Intermedio-Avanzado
"""

import pandas as pd
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

# Ejercicio 1: Crear DataFrame
# Crea un DataFrame con los siguientes datos de empleados:
# Nombre, Edad, Departamento, Salario
# (al menos 5 empleados)
# Tu código aquí:

# Ejercicio 2: Leer CSV con pandas
# Guarda el DataFrame anterior en data/empleados.csv y luego léelo con pd.read_csv().
# Tu código aquí:

# Ejercicio 3: Estadísticas básicas
# Usa el DataFrame de empleados y calcula:
# - Media de salarios
# - Salario máximo y mínimo
# - Número de empleados por departamento
# Tu código aquí:

# Ejercicio 4: Filtrar datos
# Filtra los empleados con salario > 30000 y muestra solo Nombre y Salario.
# Tu código aquí:

# Ejercicio 5: Exportar a JSON
# Exporta el DataFrame filtrado a data/altos_salarios.json con df.to_json().
# Tu código aquí:

# Ejercicio 6: SQL + Pandas
# Crea una tabla SQLite con los datos de empleados.
# Usa pd.read_sql_query() para leer la tabla directamente en un DataFrame.
# Tu código aquí:

# Ejercicio 7: Operaciones con columnas
# Añade una columna "Salario_Anual" que sea Salario * 12 (suponiendo que Salario es mensual).
# Añade otra columna "Categoria" que sea "Senior" si Salario > 40000, sino "Junior".
# Tu código aquí:

# Ejercicio 8: Agrupación
# Agrupa los empleados por departamento y calcula la media de salario
# y la edad media por grupo.
# Tu código aquí:

# Ejercicio 9: Dataset real
# Crea un pequeño dataset de ventas con columnas: fecha, producto, cantidad, precio_unitario.
# Calcula: total de ventas (cantidad * precio), producto más vendido, ventas por día.
# Tu código aquí:
