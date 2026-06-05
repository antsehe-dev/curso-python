"""
EJERCICIOS: Programación asíncrona básica (asyncio)
Nivel: Avanzado
"""

import asyncio

# Ejercicio 1: Coroutine básica
# Define una función async llamada saludar() que:
# - Imprima "¡Hola!"
# - Haga await asyncio.sleep(1)
# - Imprima "¡Adiós!"
# Ejecútala con asyncio.run().
async def saludar():
    print("¡Hola!")
    await asyncio.sleep(1)
    print("¡Adiós!")

asyncio.run(saludar())

# Ejercicio 2: Múltiples coroutines secuenciales
# Define 3 funciones async: tarea1(), tarea2(), tarea3()
# Cada una debe hacer await asyncio.sleep() con tiempos diferentes (1, 2, 3 segundos)
# y luego imprimir "Tarea X completada".
# Ejecútalas secuencialmente (una tras otra).
async def tarea1():
    await asyncio.sleep(1)
    print("Tarea 1 completada")

async def tarea2():
    await asyncio.sleep(2)
    print("Tarea 2 completada")

async def tarea3():
    await asyncio.sleep(3)
    print("Tarea 3 completada")

async def secuencial():
    await tarea1()
    await tarea2()
    await tarea3()

asyncio.run(secuencial())

# Ejercicio 3: asyncio.gather (concurrencia)
# Usa las mismas 3 tareas del ejercicio anterior, pero ahora
# ejecútalas de forma CONCURRENTE usando asyncio.gather().
# Mide el tiempo total con asyncio.get_event_loop().time().
async def concurrente():
    inicio = asyncio.get_event_loop().time()
    await asyncio.gather(tarea1(), tarea2(), tarea3())
    fin = asyncio.get_event_loop().time()
    print(f"Tiempo total: {fin - inicio:.2f}s")

asyncio.run(concurrente())

# Ejercicio 4: Retorno de valores
# Define una async def calcular(n) que haga await asyncio.sleep(n) y luego
# retorne n * 2. Usa gather para ejecutar [calcular(1), calcular(2), calcular(3)]
# y muestra los resultados.
async def calcular(n):
    await asyncio.sleep(n)
    return n * 2

async def main_calcular():
    resultados = await asyncio.gather(calcular(1), calcular(2), calcular(3))
    print(resultados)

asyncio.run(main_calcular())

# Ejercicio 5: Simular descargas
# Crea una función async descargar(url, tiempo) que simule descargar una URL
# (await asyncio.sleep(tiempo)) e imprima "Descargado: {url} en {tiempo}s".
# Simula 5 descargas concurrentes con gather().
async def descargar(url, tiempo):
    await asyncio.sleep(tiempo)
    print(f"Descargado: {url} en {tiempo}s")

async def main_descargas():
    urls = [("https://ejemplo.com/img1.jpg", 2), ("https://ejemplo.com/img2.jpg", 1), ("https://ejemplo.com/img3.jpg", 3), ("https://ejemplo.com/img4.jpg", 1.5), ("https://ejemplo.com/img5.jpg", 2.5)]
    await asyncio.gather(*[descargar(url, t) for url, t in urls])

asyncio.run(main_descargas())

# Ejercicio 6: Timeout
# Usa asyncio.wait_for() para ejecutar una coroutine con timeout de 2 segundos.
# Si tarda más, captura asyncio.TimeoutError y muestra "Timeout".
# Pista: await asyncio.wait_for(tarea_lenta(), timeout=2)
async def tarea_lenta():
    await asyncio.sleep(5)
    return "Completada"

async def main_timeout():
    try:
        resultado = await asyncio.wait_for(tarea_lenta(), timeout=2)
        print(resultado)
    except asyncio.TimeoutError:
        print("Timeout")

asyncio.run(main_timeout())

# Ejercicio 7: Semáforo (límite de concurrencia)
# Crea una función async tarea_limite(id) que haga algo simple.
# Usa asyncio.Semaphore(2) para limitar a 2 tareas concurrentes.
# Ejecuta 10 tareas y observa cómo se ejecutan de 2 en 2.
async def tarea_limite(id, semaforo):
    async with semaforo:
        print(f"Tarea {id} iniciada")
        await asyncio.sleep(1)
        print(f"Tarea {id} completada")

async def main_semaforo():
    semaforo = asyncio.Semaphore(2)
    tareas = [tarea_limite(i, semaforo) for i in range(10)]
    await asyncio.gather(*tareas)

asyncio.run(main_semaforo())
