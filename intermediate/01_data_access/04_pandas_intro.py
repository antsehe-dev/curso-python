###
# 04 - Introducción a pandas (CSV + SQL)
###
import pandas as pd
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Leer CSV con pandas
df = pd.read_csv(DATA_DIR / "productos.csv")
print("=== CSV ===")
print(df)
print(f"Precio medio: ${df['precio'].mean():.2f}")

# Leer SQL con pandas
conn = sqlite3.connect(DATA_DIR / "tienda.db")
df_clientes = pd.read_sql_query("SELECT * FROM clientes", conn)
print("\n=== SQL ===")
print(df_clientes)
conn.close()

# Escribir DataFrame a CSV y JSON
df.to_csv(DATA_DIR / "productos_copia.csv", index=False)
df.to_json(DATA_DIR / "productos.json", orient="records", indent=2)
