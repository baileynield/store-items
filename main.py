from fastapi import FastAPI

from models import Item


app = FastAPI()


@app.get("item")
async def list_item() -> list[Item]:
    