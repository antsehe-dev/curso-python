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
# Tu código aquí:

# Ejercicio 2: Mediana
# Con la misma lista velocidades, calcula la mediana manualmente
# (ordena los valores y toma el del medio) y con np.median().
# Tu código aquí:

# Ejercicio 3: Moda
# Dada la lista: datos = [1, 2, 3, 2, 4, 2, 5, 2, 3, 1, 2]
# Encuentra la moda (valor más frecuente) manualmente y con scipy.stats.mode().
# Tu código aquí:

# Ejercicio 4: Desviación estándar
# Con velocidades, calcula la desviación estándar manualmente:
# 1. Calcula la media
# 2. Resta la media a cada valor
# 3. Eleva al cuadrado cada diferencia
# 4. Calcula la media de esas diferencias (varianza)
# 5. Raíz cuadrada de la varianza
# Luego verifica con np.std().
# Tu código aquí:

# Ejercicio 5: Varianza
# Calcula la varianza manualmente y con np.var().
# Recuerda: la varianza es la desviación estándar al cuadrado.
# Tu código aquí:

# Ejercicio 6: Percentiles
# Dada la lista de edades:
edades = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
# Calcula e interpreta:
# - Percentil 25: ¿qué significa?
# - Percentil 50 (mediana)
# - Percentil 75
# - Percentil 90
# Tu código aquí:

# Ejercicio 7: Rango intercuartílico (IQR)
# Usa los percentiles para calcular el IQR = Q3 - Q1
# ¿Qué indica el IQR sobre los datos?
# Tu código aquí:

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
# Tu código aquí:

# Ejercicio 9: Normalización de datos
# Normaliza los salarios al rango [0, 1] usando:
# z = (x - min) / (max - min)
# Muestra los valores originales y normalizados.
# Tu código aquí:

# Ejercicio 10: Estandarización (Z-score)
# Estandariza los salarios usando:
# z = (x - mean) / std
# ¿Qué representa un Z-score de 1.5?
# Tu código aquí:

# ============================================================
# PARTE 3: Correlación y tendencias
# ============================================================

# Ejercicio 11: Correlación básica
# Dados años de experiencia y salario correspondiente:
experiencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
salario_exp  = [28000, 32000, 35000, 40000, 43000, 47000, 50000, 55000, 60000, 65000]
# Calcula la correlación con np.corrcoef().
# ¿Es positiva o negativa? ¿Qué significa?
# Tu código aquí:

# Ejercicio 12: Regresión lineal simple (concepto)
# Con los mismos datos, calcula la pendiente de la recta de regresión:
# pendiente = sum((x - mean_x) * (y - mean_y)) / sum((x - mean_x)**2)
# intercepto = mean_y - pendiente * mean_x
# Predice el salario para 12 años de experiencia.
# Tu código aquí:

# ============================================================
# PARTE 4: Distribuciones
# ============================================================

# Ejercicio 13: Distribución normal
# Genera 1000 números aleatorios con distribución normal
# (media=50, desviación_std=10) usando np.random.normal().
# Calcula la media y std de los datos generados.
# ¿Qué porcentaje de datos está dentro de 1 desviación estándar de la media?
# (Entre media - std y media + std)
# Tu código aquí:

# Ejercicio 14: Histograma de frecuencias
# Usando los datos generados, crea bins (intervalos) y cuenta
# cuántos valores caen en cada bin. Usa np.histogram().
# Muestra los bins y sus frecuencias.
# Tu código aquí:

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
# Tu código aquí:

# Ejercicio 16: Detectar outliers con Z-score
# Usa el mismo dataset. Calcula Z-scores y detecta outliers
# (valores con |z| > 3).
# Compara los resultados con el método IQR.
# Tu código aquí:

# ============================================================
# PARTE 6: Proyecto final - Análisis completo de dataset
# ============================================================

# Ejercicio 17: Análisis completo
# Crea un pequeño dataset de ventas:
# mes = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
#        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
# ventas = [12000, 15000, 11000, 18000, 22000, 19000,
#           25000, 21000, 16000, 20000, 23000, 28000]
# gastos = [10000, 12000, 11000, 13000, 15000, 14000,
#           16000, 15000, 13000, 14000, 16000, 18000]
# Realiza:
# - Estadísticas descriptivas de ventas y gastos
# - Mes con mayor y menor venta
# - Beneficio mensual (ventas - gastos) y total anual
# - Correlación entre ventas y gastos
# - ¿Hay algún mes outlier en ventas?
# Tu código aquí:
