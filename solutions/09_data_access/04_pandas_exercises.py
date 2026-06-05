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
df = pd.DataFrame({
    "Nombre": ["Ana", "Luis", "Sofia", "Carlos", "Elena"],
    "Edad": [28, 35, 22, 40, 31],
    "Departamento": ["IT", "Ventas", "IT", "Ventas", "RRHH"],
    "Salario": [45000, 35000, 42000, 31000, 38000]
})
print(df)

# Ejercicio 2: Leer CSV con pandas
# Guarda el DataFrame anterior en data/empleados.csv y luego léelo con pd.read_csv().
df.to_csv(DATA_DIR / "empleados.csv", index=False)
df_leido = pd.read_csv(DATA_DIR / "empleados.csv")
print(df_leido)

# Ejercicio 3: Estadísticas básicas
# Usa el DataFrame de empleados y calcula:
# - Media de salarios
# - Salario máximo y mínimo
# - Número de empleados por departamento
print(f"Media salarios: {df['Salario'].mean()}")
print(f"Salario máximo: {df['Salario'].max()}")
print(f"Salario mínimo: {df['Salario'].min()}")
print(f"Empleados por departamento:\n{df['Departamento'].value_counts()}")

# Ejercicio 4: Filtrar datos
# Filtra los empleados con salario > 30000 y muestra solo Nombre y Salario.
filtrados = df[df["Salario"] > 30000][["Nombre", "Salario"]]
print(filtrados)

# Ejercicio 5: Exportar a JSON
# Exporta el DataFrame filtrado a data/altos_salarios.json con df.to_json().
filtrados.to_json(DATA_DIR / "altos_salarios.json", orient="records", indent=2)

# Ejercicio 6: SQL + Pandas
# Crea una tabla SQLite con los datos de empleados.
# Usa pd.read_sql_query() para leer la tabla directamente en un DataFrame.
conn = sqlite3.connect(str(DATA_DIR / "ejercicios.db"))
df.to_sql("empleados", conn, if_exists="replace", index=False)
df_sql = pd.read_sql_query("SELECT * FROM empleados WHERE Salario > 35000", conn)
print(df_sql)
conn.close()

# Ejercicio 7: Operaciones con columnas
# Añade una columna "Salario_Anual" que sea Salario * 12 (suponiendo que Salario es mensual).
# Añade otra columna "Categoria" que sea "Senior" si Salario > 40000, sino "Junior".
df["Salario_Anual"] = df["Salario"] * 12
df["Categoria"] = df["Salario"].apply(lambda x: "Senior" if x > 40000 else "Junior")
print(df)

# Ejercicio 8: Agrupación
# Agrupa los empleados por departamento y calcula la media de salario
# y la edad media por grupo.
print(df.groupby("Departamento").agg({"Salario": "mean", "Edad": "mean"}))

# Ejercicio 9: Dataset real
# Crea un pequeño dataset de ventas con columnas: fecha, producto, cantidad, precio_unitario.
# Calcula: total de ventas (cantidad * precio), producto más vendido, ventas por día.
ventas = pd.DataFrame({
    "fecha": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03"],
    "producto": ["Portátil", "Ratón", "Portátil", "Teclado", "Ratón"],
    "cantidad": [2, 5, 1, 3, 10],
    "precio_unitario": [999.99, 29.99, 999.99, 49.99, 29.99]
})
ventas["total"] = ventas["cantidad"] * ventas["precio_unitario"]
print(f"Total ventas: {ventas['total'].sum()}")
print(f"Producto más vendido (por cantidad): {ventas.groupby('producto')['cantidad'].sum().idxmax()}")
print(f"Ventas por día:\n{ventas.groupby('fecha')['total'].sum()}")
