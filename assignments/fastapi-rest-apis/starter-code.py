"""Starter code for the FastAPI REST APIs assignment.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI Assignment API")


class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class Item(ItemIn):
    id: int


items: list[Item] = []
next_id = 1


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI assignment API!"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemIn) -> Item:
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items.append(item)
    next_id += 1
    return item


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemIn) -> Item:
    for index, item in enumerate(items):
        if item.id == item_id:
            updated = Item(id=item_id, **payload.model_dump())
            items[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
