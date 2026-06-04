###
# 01 - Basic Web Scraping
###
import requests
import re
url = "https://www.apple.com/es/shop/buy-mac/macbook-air"

response = requests.get(url)

if response.status_code == 200:
    print("La solicitud fue exitosa")
    html = response.text
    title_pattern = r'<title>(.*?)</title>'
    match = re.search(title_pattern, html)
    if match:
        print("Precio encontrado:")
        print(match.group(1))
else:
    print("La solicitud no fue exitosa")
