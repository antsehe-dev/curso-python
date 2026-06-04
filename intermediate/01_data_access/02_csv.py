###
# 02 - Leer y escribir CSV
###
import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Escribir CSV
with open(DATA_DIR / "productos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nombre", "precio", "stock"])
    writer.writerow([1, "Teclado", 25.50, 10])
    writer.writerow([2, "Ratón", 15.00, 25])
    writer.writerow([3, "Monitor", 199.99, 5])

# Leer CSV
with open(DATA_DIR / "productos.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)

# Con DictReader/DictWriter (más legible)
with open(DATA_DIR / "productos.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(f"{fila['nombre']}: ${fila['precio']} (stock: {fila['stock']})")
