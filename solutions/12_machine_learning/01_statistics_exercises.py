"""
EJERCICIOS: Machine Learning - Estadística y análisis de datos
Nivel: Intermedio-Avanzado
"""

import numpy as np
from scipy import stats

# ============================================================
# PARTE 1: Estadística descriptiva básica
# ============================================================

# Ejercicio 1: Media (promedio)
# Dada la siguiente lista de velocidades de 10 coches:
velocidades = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78]
# Calcula la media manualmente (suma / total) y con np.mean().
# Compara los resultados.
media_manual = sum(velocidades) / len(velocidades)
media_np = np.mean(velocidades)
print(f"Media manual: {media_manual}, Media numpy: {media_np}")

# Ejercicio 2: Mediana
# Con la misma lista velocidades, calcula la mediana manualmente
# (ordena los valores y toma el del medio) y con np.median().
ordenado = sorted(velocidades)
n = len(ordenado)
if n % 2 == 0:
    mediana_manual = (ordenado[n//2 - 1] + ordenado[n//2]) / 2
else:
    mediana_manual = ordenado[n//2]
print(f"Mediana manual: {mediana_manual}, Mediana numpy: {np.median(velocidades)}")

# Ejercicio 3: Moda
# Dada la lista: datos = [1, 2, 3, 2, 4, 2, 5, 2, 3, 1, 2]
# Encuentra la moda (valor más frecuente) manualmente y con scipy.stats.mode().
datos = [1, 2, 3, 2, 4, 2, 5, 2, 3, 1, 2]
moda_manual = max(set(datos), key=datos.count)
moda_scipy = stats.mode(datos, keepdims=True)
print(f"Moda manual: {moda_manual}, Moda scipy: {moda_scipy.mode[0]}")

# Ejercicio 4: Desviación estándar
# Con velocidades, calcula la desviación estándar manualmente:
# 1. Calcula la media
# 2. Resta la media a cada valor
# 3. Eleva al cuadrado cada diferencia
# 4. Calcula la media de esas diferencias (varianza)
# 5. Raíz cuadrada de la varianza
# Luego verifica con np.std().
media = sum(velocidades) / len(velocidades)
varianza = sum((x - media)**2 for x in velocidades) / len(velocidades)
std_manual = varianza ** 0.5
print(f"Desviación manual: {std_manual}, Numpy: {np.std(velocidades)}")

# Ejercicio 5: Varianza
# Calcula la varianza manualmente y con np.var().
# Recuerda: la varianza es la desviación estándar al cuadrado.
print(f"Varianza manual: {varianza}, Numpy: {np.var(velocidades)}")

# Ejercicio 6: Percentiles
# Dada la lista de edades:
edades = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
# Calcula e interpreta:
# - Percentil 25: ¿qué significa?
# - Percentil 50 (mediana)
# - Percentil 75
# - Percentil 90
print(f"P25: {np.percentile(edades, 25)} (el 25% de los datos está por debajo)")
print(f"P50: {np.percentile(edades, 50)} (mediana)")
print(f"P75: {np.percentile(edades, 75)}")
print(f"P90: {np.percentile(edades, 90)}")

# Ejercicio 7: Rango intercuartílico (IQR)
# Usa los percentiles para calcular el IQR = Q3 - Q1
# ¿Qué indica el IQR sobre los datos?
Q1, Q3 = np.percentile(edades, [25, 75])
IQR = Q3 - Q1
print(f"IQR: {IQR} (rango donde está el 50% central de los datos)")

# ============================================================
# PARTE 2: Análisis de datos con numpy
# ============================================================

# Ejercicio 8: Estadísticas completas
# Dado el conjunto de datos:
salarios = [32000, 45000, 38000, 52000, 29000, 41000, 48000, 35000, 55000, 31000]
# Calcula e imprime en un formato claro:
# - Media, mediana, desviación estándar, varianza
# - Mínimo, máximo, rango (max - min)
# - Percentiles 25, 50, 75
print(f"Media: {np.mean(salarios):.2f}")
print(f"Mediana: {np.median(salarios):.2f}")
print(f"Desviación estándar: {np.std(salarios):.2f}")
print(f"Varianza: {np.var(salarios):.2f}")
print(f"Mínimo: {np.min(salarios)}")
print(f"Máximo: {np.max(salarios)}")
print(f"Rango: {np.max(salarios) - np.min(salarios)}")
print(f"P25: {np.percentile(salarios, 25):.2f}")
print(f"P50: {np.percentile(salarios, 50):.2f}")
print(f"P75: {np.percentile(salarios, 75):.2f}")

# Ejercicio 9: Normalización de datos
# Normaliza los salarios al rango [0, 1] usando:
# z = (x - min) / (max - min)
# Muestra los valores originales y normalizados.
salarios_np = np.array(salarios)
min_sal, max_sal = np.min(salarios_np), np.max(salarios_np)
salarios_norm = (salarios_np - min_sal) / (max_sal - min_sal)
print("Salarios originales:", salarios)
print("Salarios normalizados:", salarios_norm)

# Ejercicio 10: Estandarización (Z-score)
# Estandariza los salarios usando:
# z = (x - mean) / std
# ¿Qué representa un Z-score de 1.5?
media_sal = np.mean(salarios_np)
std_sal = np.std(salarios_np)
z_scores = (salarios_np - media_sal) / std_sal
print("Z-scores:", z_scores)
print("Un Z-score de 1.5 significa que el valor está 1.5 desviaciones estándar por encima de la media")

# ============================================================
# PARTE 3: Correlación y tendencias
# ============================================================

# Ejercicio 11: Correlación básica
# Dados años de experiencia y salario correspondiente:
experiencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salario_exp  = [28000, 32000, 35000, 40000, 43000, 47000, 50000, 55000, 60000, 65000]
# Calcula la correlación con np.corrcoef().
# ¿Es positiva o negativa? ¿Qué significa?
corr = np.corrcoef(experiencia, salario_exp)[0, 1]
print(f"Correlación: {corr:.4f}")
print("Es positiva y cercana a 1, lo que indica una fuerte relación lineal directa: a más experiencia, mayor salario")

# Ejercicio 12: Regresión lineal simple (concepto)
# Con los mismos datos, calcula la pendiente de la recta de regresión:
# pendiente = sum((x - mean_x) * (y - mean_y)) / sum((x - mean_x)**2)
# intercepto = mean_y - pendiente * mean_x
# Predice el salario para 12 años de experiencia.
x = np.array(experiencia)
y = np.array(salario_exp)
mean_x, mean_y = np.mean(x), np.mean(y)
pendiente = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x)**2)
intercepto = mean_y - pendiente * mean_x
print(f"Pendiente: {pendiente:.2f}, Intercepto: {intercepto:.2f}")
prediccion = pendiente * 12 + intercepto
print(f"Salario estimado para 12 años: {prediccion:.2f}€")

# ============================================================
# PARTE 4: Distribuciones
# ============================================================

# Ejercicio 13: Distribución normal
# Genera 1000 números aleatorios con distribución normal
# (media=50, desviación_std=10) usando np.random.normal().
# Calcula la media y std de los datos generados.
# ¿Qué porcentaje de datos está dentro de 1 desviación estándar de la media?
# (Entre media - std y media + std)
datos_norm = np.random.normal(50, 10, 1000)
print(f"Media generada: {np.mean(datos_norm):.2f}")
print(f"Std generada: {np.std(datos_norm):.2f}")
dentro = np.sum((datos_norm > np.mean(datos_norm) - np.std(datos_norm)) & (datos_norm < np.mean(datos_norm) + np.std(datos_norm)))
print(f"Porcentaje dentro de 1 std: {dentro / len(datos_norm) * 100:.2f}%")

# Ejercicio 14: Histograma de frecuencias
# Usando los datos generados, crea bins (intervalos) y cuenta
# cuántos valores caen en cada bin. Usa np.histogram().
# Muestra los bins y sus frecuencias.
hist, bins = np.histogram(datos_norm, bins=10)
for i in range(len(hist)):
    print(f"Bin [{bins[i]:.1f}, {bins[i+1]:.1f}): {hist[i]} valores")

# ============================================================
# PARTE 5: Análisis de outliers
# ============================================================

# Ejercicio 15: Detectar outliers con IQR
# Dado el dataset:
datos_con_outliers = [10, 12, 11, 13, 12, 11, 14, 13, 12, 100, 11, 13, 12, 200]
# Detecta outliers usando el método IQR:
# - Q1 - 1.5*IQR (límite inferior)
# - Q3 + 1.5*IQR (límite superior)
# Muestra qué valores son outliers.
datos_arr = np.array(datos_con_outliers)
Q1_iqr, Q3_iqr = np.percentile(datos_arr, [25, 75])
IQR_val = Q3_iqr - Q1_iqr
lim_inf = Q1_iqr - 1.5 * IQR_val
lim_sup = Q3_iqr + 1.5 * IQR_val
outliers_iqr = datos_arr[(datos_arr < lim_inf) | (datos_arr > lim_sup)]
print(f"Límite inferior: {lim_inf}, Límite superior: {lim_sup}")
print(f"Outliers (IQR): {list(outliers_iqr)}")

# Ejercicio 16: Detectar outliers con Z-score
# Usa el mismo dataset. Calcula Z-scores y detecta outliers
# (valores con |z| > 3).
# Compara los resultados con el método IQR.
mean_out = np.mean(datos_arr)
std_out = np.std(datos_arr)
z = (datos_arr - mean_out) / std_out
outliers_z = datos_arr[np.abs(z) > 3]
print(f"Outliers (Z-score): {list(outliers_z)}")
print("El método IQR detecta más outliers que el Z-score con |z|>3 en este caso")

# ============================================================
# PARTE 6: Proyecto final - Análisis completo de dataset
# ============================================================

# Ejercicio 17: Análisis completo
# Crea un pequeño dataset de ventas:
mes = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
       "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = [12000, 15000, 11000, 18000, 22000, 19000,
          25000, 21000, 16000, 20000, 23000, 28000]
gastos = [10000, 12000, 11000, 13000, 15000, 14000,
          16000, 15000, 13000, 14000, 16000, 18000]
# Realiza:
# - Estadísticas descriptivas de ventas y gastos
# - Mes con mayor y menor venta
# - Beneficio mensual (ventas - gastos) y total anual
# - Correlación entre ventas y gastos
# - ¿Hay algún mes outlier en ventas?
ventas_np = np.array(ventas)
gastos_np = np.array(gastos)

print("--- Estadísticas de Ventas ---")
print(f"Media: {np.mean(ventas_np):.2f}, Mediana: {np.median(ventas_np):.2f}, Std: {np.std(ventas_np):.2f}")
print("--- Estadísticas de Gastos ---")
print(f"Media: {np.mean(gastos_np):.2f}, Mediana: {np.median(gastos_np):.2f}, Std: {np.std(gastos_np):.2f}")
print(f"Mes con mayor venta: {mes[np.argmax(ventas_np)]} ({np.max(ventas_np)})")
print(f"Mes con menor venta: {mes[np.argmin(ventas_np)]} ({np.min(ventas_np)})")
beneficio = ventas_np - gastos_np
print(f"Beneficio total anual: {np.sum(beneficio)}")
corr_vg = np.corrcoef(ventas_np, gastos_np)[0, 1]
print(f"Correlación ventas-gastos: {corr_vg:.4f}")
Q1_v, Q3_v = np.percentile(ventas_np, [25, 75])
IQR_v = Q3_v - Q1_v
lim_inf_v = Q1_v - 1.5 * IQR_v
lim_sup_v = Q3_v + 1.5 * IQR_v
for i, v in enumerate(ventas_np):
    if v < lim_inf_v or v > lim_sup_v:
        print(f"Outlier en ventas: {mes[i]} ({v})")
