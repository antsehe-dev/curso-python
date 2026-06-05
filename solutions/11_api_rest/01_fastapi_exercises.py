"""
EJERCICIOS: API REST con FastAPI
Nivel: Avanzado
NOTA: Estos ejercicios deben ejecutarse con uvicorn, no directamente.
Ejecuta: uvicorn ejercicios.11_api_rest.01_fastapi_exercises:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# --- Modelos Pydantic ---

# Ejercicio 1: Modelo Usuario
# Crea un modelo Pydantic UsuarioCreate con: nombre (str), email (str), edad (int)
# Crea otro Usuario(UsuarioCreate) que herede y añada id (int).
class UsuarioCreate(BaseModel):
    nombre: str = Field(..., min_length=3)
    email: str
    edad: int = Field(..., ge=18)

class Usuario(UsuarioCreate):
    id: int

# Ejercicio 2: Modelo Producto
# Crea modelos ProductoCreate (nombre, precio, categoria) y Producto (hereda, añade id).
class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    categoria: str

class Producto(ProductoCreate):
    id: int

# --- In-memory "database" ---
# Base de datos simulada (lista/diccionario)
usuarios_db: dict[int, Usuario] = {}
productos_db: dict[int, Producto] = {}
next_usuario_id = 1
next_producto_id = 1

# --- Endpoints ---

# Ejercicio 3: GET raíz
# Crea un endpoint GET / que devuelva {"mensaje": "API de ejercicios funcionando"}.
app = FastAPI(title="API de Ejercicios", version="1.0.0")

@app.get("/")
def raiz():
    return {"mensaje": "API de ejercicios funcionando"}

# Ejercicio 4: CRUD Usuarios
# Implementa:
# - POST /usuarios: crea un usuario, asigna id autoincremental, devuelve 201.
# - GET /usuarios: lista todos los usuarios.
# - GET /usuarios/{usuario_id}: obtiene un usuario por id, 404 si no existe.
# - DELETE /usuarios/{usuario_id}: elimina un usuario, 404 si no existe.
@app.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate):
    global next_usuario_id
    nuevo = Usuario(id=next_usuario_id, **usuario.model_dump())
    usuarios_db[nuevo.id] = nuevo
    next_usuario_id += 1
    return nuevo

@app.get("/usuarios", response_model=list[Usuario])
def listar_usuarios():
    return list(usuarios_db.values())

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuarios_db[usuario_id]

@app.delete("/usuarios/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: int):
    if usuario_id not in usuarios_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    del usuarios_db[usuario_id]

# Ejercicio 5: CRUD Productos
# Implementa el mismo CRUD para productos.
# Añade un GET /productos?categoria=XYZ que filtre por categoría.
@app.post("/productos", status_code=status.HTTP_201_CREATED, response_model=Producto)
def crear_producto(producto: ProductoCreate):
    global next_producto_id
    nuevo = Producto(id=next_producto_id, **producto.model_dump())
    productos_db[nuevo.id] = nuevo
    next_producto_id += 1
    return nuevo

@app.get("/productos", response_model=list[Producto])
def listar_productos(categoria: str | None = None):
    if categoria:
        return [p for p in productos_db.values() if p.categoria == categoria]
    return list(productos_db.values())

@app.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos_db[producto_id]

@app.delete("/productos/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int):
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    del productos_db[producto_id]

# Ejercicio 6: Búsqueda
# Añade un endpoint GET /usuarios/buscar?email=abc@test.com
# que busque un usuario por email.
@app.get("/usuarios/buscar", response_model=Usuario)
def buscar_usuario(email: str):
    for u in usuarios_db.values():
        if u.email == email:
            return u
    raise HTTPException(status_code=404, detail="Usuario no encontrado con ese email")

# Ejercicio 7: Validación personalizada
# Añade validación al modelo UsuarioCreate:
# - nombre debe tener al menos 3 caracteres
# - email debe contener "@"
# - edad debe ser >= 18
# Pista: usa Field(min_length=...) de pydantic o validador @field_validator.

# La validación está en el modelo UsuarioCreate usando Field(...)

# Ejercicio 8: Respuesta personalizada
# Modifica los endpoints para usar response_model y status_code adecuados.
# - POST debe devolver 201 Created
# - DELETE debe devolver 204 No Content
# - Los errores deben usar HTTPException con mensajes descriptivos.

# Ya aplicado en los endpoints de arriba.
