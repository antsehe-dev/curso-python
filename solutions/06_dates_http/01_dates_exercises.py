"""
EJERCICIOS: Fechas y horas (datetime, timedelta)
Nivel: Intermedio
"""

from datetime import datetime, timedelta
import locale

# Ejercicio 1: Fecha actual
# Muestra la fecha y hora actual con formato: "Hoy es 05/06/2026 y son las 14:30"
# (Usa strftime con los códigos %d/%m/%Y y %H:%M)
ahora = datetime.now()
print(f"Hoy es {ahora.strftime('%d/%m/%Y')} y son las {ahora.strftime('%H:%M')}")

# Ejercicio 2: Fecha específica
# Crea un objeto datetime para el 25 de diciembre de 2024 a las 10:30.
navidad = datetime(2024, 12, 25, 10, 30)
print(navidad)

# Ejercicio 3: Días hasta una fecha
# Calcula cuántos días faltan desde hoy hasta el próximo 1 de enero.
# Pista: (fecha_futura - datetime.now()).days
prox_anio = datetime(ahora.year + 1, 1, 1)
dias = (prox_anio - ahora).days
print(f"Faltan {dias} días para Año Nuevo")

# Ejercicio 4: Timedelta
# Calcula qué fecha será dentro de 30 días a partir de hoy.
# Calcula qué fecha fue hace 100 días.
print("Dentro de 30 días:", ahora + timedelta(days=30))
print("Hace 100 días:", ahora - timedelta(days=100))

# Ejercicio 5: Edad exacta
# Pide al usuario su fecha de nacimiento (DD/MM/AAAA) y calcula su edad exacta en años.
nacimiento = input("Introduce tu fecha de nacimiento (DD/MM/AAAA): ")
fecha_nac = datetime.strptime(nacimiento, "%d/%m/%Y")
edad = ahora.year - fecha_nac.year
if (ahora.month, ahora.day) < (fecha_nac.month, fecha_nac.day):
    edad -= 1
print(f"Tienes {edad} años")

# Ejercicio 6: Diferencia en horas
# Dadas dos fechas: inicio = datetime(2024, 1, 1, 8, 0) y fin = datetime(2024, 1, 3, 17, 30)
# Calcula la diferencia total en horas.
inicio = datetime(2024, 1, 1, 8, 0)
fin = datetime(2024, 1, 3, 17, 30)
diferencia = fin - inicio
print(f"Diferencia en horas: {diferencia.total_seconds() / 3600:.2f}")

# Ejercicio 7: Formateo localizado
# Configura el locale a español y muestra la fecha actual con el mes en español.
# (Nota: en Windows puede ser "es-ES", en Linux "es_ES.UTF-8")
try:
    locale.setlocale(locale.LC_TIME, "es-ES")
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    except locale.Error:
        print("Locale español no disponible")
print(ahora.strftime("%A, %d de %B de %Y"))
