"""
EJERCICIOS: API REST con FastAPI
Nivel: Avanzado
NOTA: Estos ejercicios deben ejecutarse con uvicorn, no directamente.
Ejecuta: uvicorn ejercicios.11_api_rest.01_fastapi_exercises:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# --- Modelos Pydantic ---

# Ejercicio 1: Modelo Usuario
# Crea un modelo Pydantic UsuarioCreate con: nombre (str), email (str), edad (int)
# Crea otro Usuario(UsuarioCreate) que herede y añada id (int).
# Tu código aquí:

# Ejercicio 2: Modelo Producto
# Crea modelos ProductoCreate (nombre, precio, categoria) y Producto (hereda, añade id).
# Tu código aquí:

# --- In-memory "database" ---
# Base de datos simulada (lista/diccionario)
# usuarios_db: dict[int, Usuario] = {}
# productos_db: dict[int, Producto] = {}

# --- Endpoints ---

# Ejercicio 3: GET raíz
# Crea un endpoint GET / que devuelva {"mensaje": "API de ejercicios funcionando"}.
# Tu código aquí:

# Ejercicio 4: CRUD Usuarios
# Implementa:
# - POST /usuarios: crea un usuario, asigna id autoincremental, devuelve 201.
# - GET /usuarios: lista todos los usuarios.
# - GET /usuarios/{usuario_id}: obtiene un usuario por id, 404 si no existe.
# - DELETE /usuarios/{usuario_id}: elimina un usuario, 404 si no existe.
# Tu código aquí:

# Ejercicio 5: CRUD Productos
# Implementa el mismo CRUD para productos.
# Añade un GET /productos?categoria=XYZ que filtre por categoría.
# Tu código aquí:

# Ejercicio 6: Búsqueda
# Añade un endpoint GET /usuarios/buscar?email=abc@test.com
# que busque un usuario por email.
# Tu código aquí:

# Ejercicio 7: Validación personalizada
# Añade validación al modelo UsuarioCreate:
# - nombre debe tener al menos 3 caracteres
# - email debe contener "@"
# - edad debe ser >= 18
# Pista: usa Field(min_length=...) de pydantic o validador @field_validator.
# Tu código aquí:

# Ejercicio 8: Respuesta personalizada
# Modifica los endpoints para usar response_model y status_code adecuados.
# - POST debe devolver 201 Created
# - DELETE debe devolver 204 No Content
# - Los errores deben usar HTTPException con mensajes descriptivos.
# Tu código aquí:

# Instancia de la app (debe estar al final para que funcione con uvicorn)
# app = FastAPI(title="API de Ejercicios", version="1.0.0")
