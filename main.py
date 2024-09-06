from fastapi import FastAPI
from item_router import item_router


app = FastAPI()

app.include_router(item_router, prefix="/items")
