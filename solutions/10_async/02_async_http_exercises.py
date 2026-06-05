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
async def get_simple():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://httpbin.org/get")
        print(f"Status: {resp.status_code}")
        print(resp.json())

asyncio.run(get_simple())

# Ejercicio 2: Múltiples peticiones secuenciales
# Haz 3 peticiones GET secuenciales a httpbin.org/get.
# Mide el tiempo total.
async def secuenciales():
    inicio = time.time()
    async with httpx.AsyncClient() as client:
        for i in range(3):
            resp = await client.get("https://httpbin.org/get")
            print(f"Petición {i+1}: {resp.status_code}")
    print(f"Tiempo secuencial: {time.time() - inicio:.2f}s")

asyncio.run(secuenciales())

# Ejercicio 3: Múltiples peticiones concurrentes
# Las mismas 3 peticiones pero ahora CONCURRENTES usando asyncio.gather().
# Compara el tiempo con el ejercicio anterior.
async def concurrentes():
    inicio = time.time()
    async with httpx.AsyncClient() as client:
        tareas = [client.get("https://httpbin.org/get") for _ in range(3)]
        respuestas = await asyncio.gather(*tareas)
        for i, resp in enumerate(respuestas, 1):
            print(f"Petición {i}: {resp.status_code}")
    print(f"Tiempo concurrente: {time.time() - inicio:.2f}s")

asyncio.run(concurrentes())

# Ejercicio 4: Fetch con manejo de errores
# Crea una función async fetch_url(client, url) que:
# - Haga un GET
# - Use resp.raise_for_status() para verificar errores
# - Retorne {"url": url, "status": resp.status_code, "size": len(resp.text)}
# Pruébala con URLs válidas y una inválida.
async def fetch_url(client, url):
    try:
        resp = await client.get(url)
        resp.raise_for_status()
        return {"url": url, "status": resp.status_code, "size": len(resp.text)}
    except httpx.HTTPError as e:
        return {"url": url, "error": str(e)}

async def main_fetch():
    async with httpx.AsyncClient() as client:
        urls = ["https://httpbin.org/get", "https://httpbin.org/status/404", "https://httpbin.org/get"]
        resultados = await asyncio.gather(*[fetch_url(client, url) for url in urls])
        for r in resultados:
            print(r)

asyncio.run(main_fetch())

# Ejercicio 5: Scraping asíncrono
# Descarga 5 URLs de ejemplo (pueden ser https://httpbin.org/get?n=1, etc.)
# de forma concurrente. Para cada una, extrae la respuesta JSON.
async def scraping():
    async with httpx.AsyncClient() as client:
        tareas = [client.get(f"https://httpbin.org/get?n={i}") for i in range(1, 6)]
        respuestas = await asyncio.gather(*tareas)
        for resp in respuestas:
            data = resp.json()
            print(f"Args: {data['args']}")

asyncio.run(scraping())

# Ejercicio 6: Rate limiting
# Implementa un sistema que haga peticiones con un intervalo mínimo de 1 segundo
# entre cada una (para no sobrecargar el servidor).
# Pista: guarda el tiempo de la última petición con time.time()
async def rate_limited():
    async with httpx.AsyncClient() as client:
        ultima = 0
        for i in range(5):
            ahora = time.time()
            espera = max(0, 1 - (ahora - ultima))
            if espera > 0:
                print(f"Esperando {espera:.2f}s...")
                await asyncio.sleep(espera)
            resp = await client.get("https://httpbin.org/get")
            print(f"Petición {i+1}: {resp.status_code}")
            ultima = time.time()

asyncio.run(rate_limited())

# Ejercicio 7: Comparativa sync vs async
# Crea una función síncrona que haga 5 peticiones SECUENCIALES (sin asyncio).
# Crea una función asíncrona que haga las mismas 5 peticiones CONCURRENTES.
# Mide y compara los tiempos de ambas.
import requests

def sync_requests():
    inicio = time.time()
    for i in range(5):
        resp = requests.get(f"https://httpbin.org/get?n={i}")
        print(f"Síncrono {i+1}: {resp.status_code}")
    print(f"Tiempo síncrono: {time.time() - inicio:.2f}s")

async def async_requests():
    inicio = time.time()
    async with httpx.AsyncClient() as client:
        tareas = [client.get(f"https://httpbin.org/get?n={i}") for i in range(5)]
        respuestas = await asyncio.gather(*tareas)
        for i, resp in enumerate(respuestas, 1):
            print(f"Asíncrono {i}: {resp.status_code}")
    print(f"Tiempo asíncrono: {time.time() - inicio:.2f}s")

sync_requests()
asyncio.run(async_requests())
