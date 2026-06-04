from bs4 import BeautifulSoup 
import requests

url = "https://www.amazon.es/s?k=comida&crid=28YCF3M41DK3L&sprefix=comid%2Caps%2C86&ref=nb_sb_noss_2"

headers ={
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("La solicitud fue exitosa")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    #print (soup.prettify())
    
    prices_tag = soup.find_all('span', class_='a-price-whole')
    if prices_tag:
        print("Precio encontrado:")
        for price in prices_tag:
            print(price.text.strip())
    else:
        print("Precio no encontrado")