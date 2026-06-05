"""
EJERCICIOS: HTTP Requests (requests)
Nivel: Intermedio
"""

import requests

# Ejercicio 1: GET request
# Haz una petición GET a https://jsonplaceholder.typicode.com/posts/1
# Muestra el status code y el contenido JSON.
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status:", resp.status_code)
print(resp.json())

# Ejercicio 2: POST request
# Envía un POST a https://jsonplaceholder.typicode.com/posts con:
# { "title": "Mi título", "body": "Mi contenido", "userId": 1 }
# Muestra la respuesta JSON.
nuevo = {"title": "Mi título", "body": "Mi contenido", "userId": 1}
resp = requests.post("https://jsonplaceholder.typicode.com/posts", json=nuevo)
print("Status:", resp.status_code)
print(resp.json())

# Ejercicio 3: Parámetros en GET
# Busca posts del usuario 1 en JSONPlaceholder usando params:
# https://jsonplaceholder.typicode.com/posts?userId=1
# Muestra cuántos posts tiene.
resp = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": 1})
posts = resp.json()
print(f"El usuario 1 tiene {len(posts)} posts")

# Ejercicio 4: Manejo de errores
# Intenta hacer GET a una URL que no existe (status 404).
# Verifica el status code y muestra un mensaje adecuado.
resp = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
if resp.status_code == 404:
    print("El recurso no existe (404)")
else:
    print(f"Status: {resp.status_code}")

# Ejercicio 5: Headers personalizados
# Haz una petición GET con un User-Agent personalizado
# (ej: "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
# a https://httpbin.org/headers y muestra la respuesta.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
resp = requests.get("https://httpbin.org/headers", headers=headers)
print(resp.json())

# Ejercicio 6: API de clima simulada
# Usa https://jsonplaceholder.typicode.com como si fuera una API real.
# Obtén los primeros 5 posts y muestra sus títulos.
resp = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = resp.json()[:5]
for i, post in enumerate(posts, 1):
    print(f"{i}. {post['title']}")

# Ejercicio 7: Autenticación (simulada)
# Usa https://httpbin.org/basic-auth/user/pass con auth=(user, pass)
# para probar autenticación básica.
resp = requests.get("https://httpbin.org/basic-auth/user/pass", auth=("user", "pass"))
print(f"Autenticado: {resp.status_code == 200}")
print(resp.json())
