from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = "https://en.wikipedia.org/wiki/Web_scraping"
headers = {
    
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("La peticion fue exitosa")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    #Extraer todos los tiulos <h1>
    titulos = [titulo.string for titulo in soup.find_all('h1')]
    print("Titulos encontrados:")
    print(titulos)
    
    #Extraer todos los enlaces <a>
    enlaces = [urljoin(url, enlace['href']) for enlace in soup.find_all('a', href=True)]

    print("Enlaces encontrados:")
    print(enlaces)

else:
    print("La peticion no fue exitosa. Codigo de estado:", response.status_code)
