###
# 01 - Fundamentos de async/await
# async = define una función asíncrona (corutina)
# await = espera a que una corutina termine su ejecución
###
import asyncio

# async def define una corutina
async def saludar(nombre: str, demora: float) -> str:
    await asyncio.sleep(demora)
    return f"Hola, {nombre}!"

# asyncio.gather ejecuta varias corutinas en paralelo
async def main():
    resultados = await asyncio.gather(
        saludar("Ana", 1),
        saludar("Luis", 0.5),
        saludar("Sofía", 0.3),
    )
    for r in resultados:
        print(r)

asyncio.run(main())
