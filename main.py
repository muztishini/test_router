from fastapi import FastAPI
from item_router import item_router
from user_router import user_router


app = FastAPI()

app.include_router(item_router, prefix="/items", tags=["Item methods"])
app.include_router(user_router, prefix="/users", tags=["User methods"])
