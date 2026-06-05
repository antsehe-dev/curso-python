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
# Tu código aquí:

# Ejercicio 2: Múltiples coroutines secuenciales
# Define 3 funciones async: tarea1(), tarea2(), tarea3()
# Cada una debe hacer await asyncio.sleep() con tiempos diferentes (1, 2, 3 segundos)
# y luego imprimir "Tarea X completada".
# Ejecútalas secuencialmente (una tras otra).
# Tu código aquí:

# Ejercicio 3: asyncio.gather (concurrencia)
# Usa las mismas 3 tareas del ejercicio anterior, pero ahora
# ejecútalas de forma CONCURRENTE usando asyncio.gather().
# Mide el tiempo total con asyncio.get_event_loop().time().
# Tu código aquí:

# Ejercicio 4: Retorno de valores
# Define una async def calcular(n) que haga await asyncio.sleep(n) y luego
# retorne n * 2. Usa gather para ejecutar [calcular(1), calcular(2), calcular(3)]
# y muestra los resultados.
# Tu código aquí:

# Ejercicio 5: Simular descargas
# Crea una función async descargar(url, tiempo) que simule descargar una URL
# (await asyncio.sleep(tiempo)) e imprima "Descargado: {url} en {tiempo}s".
# Simula 5 descargas concurrentes con gather().
# Tu código aquí:

# Ejercicio 6: Timeout
# Usa asyncio.wait_for() para ejecutar una coroutine con timeout de 2 segundos.
# Si tarda más, captura asyncio.TimeoutError y muestra "Timeout".
# Pista: await asyncio.wait_for(tarea_lenta(), timeout=2)
# Tu código aquí:

# Ejercicio 7: Semáforo (límite de concurrencia)
# Crea una función async tarea_limite(id) que haga algo simple.
# Usa asyncio.Semaphore(2) para limitar a 2 tareas concurrentes.
# Ejecuta 10 tareas y observa cómo se ejecutan de 2 en 2.
# Tu código aquí:
