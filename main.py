import json

from fastapi import FastAPI

from models import Item


app = FastAPI()

with open("store_items.json", "r") as f:
    data = json.load(f)

items: list[Item] = []

for item in data:
    items.append(Item(**item))


@app.get("/items")
async def list_items() -> list[Item]:
    return items

@app.post("/items")
async def creat_items(item: Item) -> None:
    items.append(item)

@app.put("/items/{item_id}")
async def update_items(item_id: int, updated_item: Item) -> None:
    for x, item in enumerate(items):
        if item.id == item_id:
            items[x] = updated_item
            return

@app.delete("/items/{item_id}")
async def delete_items(item_id: int) -> None:
    for x, item in enumerate(items):
        if item.id == item_id:
            items.pop(x)
            return