"""
EJERCICIOS: Web Scraping con BeautifulSoup
Nivel: Intermedio
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Ejercicio 1: Extraer título
# Descarga el HTML de https://example.com con requests.
# Usa BeautifulSoup para extraer el título (<title>) y el contenido del <h1>.
resp = requests.get("https://example.com")
soup = BeautifulSoup(resp.text, 'html.parser')
print("Title:", soup.title.text)
print("H1:", soup.h1.text if soup.h1 else "No h1")

# Ejercicio 2: Encontrar por clase
# Dado el siguiente HTML simulado (variable html_str):
# Busca todos los elementos con class="producto" y extrae su texto.
html_str = """
<html>
<body>
    <div class="producto">Producto 1 - 10€</div>
    <div class="producto">Producto 2 - 20€</div>
    <div class="oferta">Oferta 1 - 5€</div>
    <div class="producto">Producto 3 - 15€</div>
</body>
</html>
"""
soup = BeautifulSoup(html_str, 'html.parser')
productos = soup.find_all(class_="producto")
for p in productos:
    print(p.text)

# Ejercicio 3: Extraer enlaces
# Descarga https://example.com y extrae TODOS los enlaces (<a>).
# Muestra el texto del enlace y el atributo href.
resp = requests.get("https://example.com")
soup = BeautifulSoup(resp.text, 'html.parser')
for a in soup.find_all('a'):
    print(f"{a.text.strip()} -> {a.get('href')}")

# Ejercicio 4: Scraping con headers
# Crea una función get_page_with_headers(url) que haga una petición GET
# con un User-Agent de navegador real. Retorna el texto de la respuesta.
def get_page_with_headers(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resp = requests.get(url, headers=headers)
    return resp.text
print(get_page_with_headers("https://httpbin.org/headers")[:200])

# Ejercicio 5: Extraer tabla
# Dado el HTML simulado, extrae todas las filas de la tabla.
tabla_html = """
<table>
    <tr><th>Nombre</th><th>Edad</th><th>Ciudad</th></tr>
    <tr><td>Ana</td><td>25</td><td>Madrid</td></tr>
    <tr><td>Luis</td><td>30</td><td>Barcelona</td></tr>
</table>
"""
soup_tabla = BeautifulSoup(tabla_html, 'html.parser')
for fila in soup_tabla.find_all("tr"):
    celdas = fila.find_all(["th", "td"])
    print([celda.text.strip() for celda in celdas])

# Ejercicio 6: Scraping real (Books to Scrape)
# Visita https://books.toscrape.com/ y extrae:
# - Los títulos de los primeros 5 libros
# - Los precios de esos libros
# Pista: busca los selectores adecuados con tu navegador.
# (Si no puedes acceder, simula con el HTML de ejemplo)
try:
    resp = requests.get("https://books.toscrape.com/")
    soup = BeautifulSoup(resp.text, 'html.parser')
    libros = soup.find_all("article", class_="product_pod")[:5]
    for libro in libros:
        titulo = libro.h3.a.get("title")
        precio = libro.find("p", class_="price_color").text
        print(f"{titulo} - {precio}")
except Exception as e:
    print(f"Error al acceder a books.toscrape.com: {e}")

# Ejercicio 7: URLs relativas
# Dada una URL base "https://ejemplo.com" y un enlace "/productos/123",
# usa urljoin (from urllib.parse import urljoin) para construir la URL completa.
url_base = "https://ejemplo.com"
enlace = "/productos/123"
url_completa = urljoin(url_base, enlace)
print(url_completa)
