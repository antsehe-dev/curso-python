###
# 01 - Dates
# Fechas y horas en Python
###

from datetime import datetime, timedelta

# 1. Obtener la fecha y hora actual
print(datetime.now())

# Crear una fecha específica
specific_date = datetime(2022, 1, 1, 12, 0, 0)
print(specific_date)

# 3. Formatear una fecha 
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Establecer el locale a español



formatted_date = datetime.now().strftime("%H:%M:%S")
# H: hora, M: minutos, S: segundos, Y: año, m: mes, d: día, D: día de la semana.
# Puedes mirar la documentacion en: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(formatted_date)

# 4. Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# 5. Obtener componentes de una fecha
now = datetime.now()
year = now.year
month = now.month

# 6. Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2022, 1, 1)
difference = date1 - date2
print(f"Diferencia: {difference}")