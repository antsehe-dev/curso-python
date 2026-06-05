"""
EJERCICIOS: HTTP asíncrono con httpx
Nivel: Avanzado
"""

import asyncio
import httpx
import time

# Ejercicio 1: GET asíncrono simple
# Usa httpx.AsyncClient para hacer un GET a https://httpbin.org/get
# Muestra el status code y el contenido JSON.
# Tu código aquí:

# Ejercicio 2: Múltiples peticiones secuenciales
# Haz 3 peticiones GET secuenciales a httpbin.org/get.
# Mide el tiempo total.
# Tu código aquí:

# Ejercicio 3: Múltiples peticiones concurrentes
# Las mismas 3 peticiones pero ahora CONCURRENTES usando asyncio.gather().
# Compara el tiempo con el ejercicio anterior.
# Tu código aquí:

# Ejercicio 4: Fetch con manejo de errores
# Crea una función async fetch_url(client, url) que:
# - Haga un GET
# - Use resp.raise_for_status() para verificar errores
# - Retorne {"url": url, "status": resp.status_code, "size": len(resp.text)}
# Pruébala con URLs válidas y una inválida.
# Tu código aquí:

# Ejercicio 5: Scraping asíncrono
# Descarga 5 URLs de ejemplo (pueden ser https://httpbin.org/get?n=1, etc.)
# de forma concurrente. Para cada una, extrae la respuesta JSON.
# Tu código aquí:

# Ejercicio 6: Rate limiting
# Implementa un sistema que haga peticiones con un intervalo mínimo de 1 segundo
# entre cada una (para no sobrecargar el servidor).
# Pista: guarda el tiempo de la última petición con time.time()
# Tu código aquí:

# Ejercicio 7: Comparativa sync vs async
# Crea una función síncrona que haga 5 peticiones SECUENCIALES (sin asyncio).
# Crea una función asíncrona que haga las mismas 5 peticiones CONCURRENTES.
# Mide y compara los tiempos de ambas.
# Tu código aquí:
