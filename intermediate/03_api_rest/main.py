###
# 03 - API REST con FastAPI
###
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API de ejemplo", version="0.1.0")

# --- Modelos ---

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class Item(ItemCreate):
    id: int

# --- Datos en memoria ---

items: list[Item] = [
    Item(id=1, name="Teclado", price=25.50, in_stock=True),
    Item(id=2, name="Ratón", price=15.00, in_stock=True),
]
next_id = 3

# --- Endpoints ---

@app.get("/")
def root():
    return {"message": "API de ejemplo funcionando"}

@app.get("/items", response_model=list[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new = Item(id=next_id, **item.model_dump())
    next_id += 1
    items.append(new)
    return new

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item no encontrado")
