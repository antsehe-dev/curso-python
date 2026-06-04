###
# 02 - Request
# Peticiones a API's con Python
###

# 1. Sin dependecias
import urllib.request
import json

api_post = 'https://jsonplaceholder.typicode.com/posts'
# Realizar la petición a la API
try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    # Convertir la respuesta a un objeto de Python
    json_data = json.loads(data.decode('utf-8'))
    print(json_data[0])  # Imprime el primer post
    response.close() # Cerrar la conexión
except Exception as e:
    print(f"Error al realizar la petición: {e}")

# 2. Con dependencias
import requests

# Get: Obtener datos de una API
print("\nGET: ")
response = requests.get(api_post)
print(response.json()[0])  # Imprime el primer post


# Post: Enviar datos a una API
print("\nPOST: ")
new_post = {
    "title": "antse",
    "body": "dev",
    "userId": 5
}
try:
    response = requests.post(api_post, json=new_post)
    print(response.status_code)  # Imprime el código de estado de la respuesta
    print(response.json())  # Imprime la respuesta del nuevo post creado
except Exception as e:
    print(f"Error al realizar la petición: {e}")

# Lo mismo con otros métodos HTTP como PUT, DELETE, etc.
# Diferencia entre put y patch, el primero cambia todo, el segundo solo cambia lo que se le indique



