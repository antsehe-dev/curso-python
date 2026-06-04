###
# 02 - Peticiones HTTP asíncronas con httpx
###
import asyncio
import httpx
import time

URLS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
]

async def fetch(url: str, client: httpx.AsyncClient) -> dict:
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.json()

async def main():
    async with httpx.AsyncClient() as client:
        tareas = [fetch(url, client) for url in URLS]
        resultados = await asyncio.gather(*tareas)
        for r in resultados:
            print(f"#{r['id']}: {r['title'][:50]}...")

inicio = time.time()
asyncio.run(main())
print(f"\nTiempo total: {time.time() - inicio:.2f}s")
