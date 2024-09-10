from fastapi import APIRouter, Body
from database import Item, SessionLocal
from fastapi.responses import JSONResponse
from schemas import Item_Model
from typing import List


item_router = APIRouter()


@item_router.get("/", response_model=List[Item_Model])
async def read_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return items


@item_router.post("/")
async def create_item(data: Item_Model = Body()):
    db = SessionLocal()
    db_item = Item(name=data.name, description=data.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item created", "data": db_item}


@item_router.get("/{item_id}", response_model=Item_Model)
async def read_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        return JSONResponse(status_code=404, content={"message": f"Item {item_id} не найден"})
    return item


@item_router.put("/{item_id}")
async def update_item(item_id: int, data: Item_Model = Body()):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        return JSONResponse(status_code=404, content={"message": f"Item {item_id} не найден"})
    db_item.name = data.name
    db_item.description = data.description
    db.commit()
    db.refresh(db_item)
    return {"message": f"Item {item_id} updated", "data": db_item}


@item_router.delete("/{item_id}")
async def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        return JSONResponse(status_code=404, content={"message": f"Item {item_id} не найден"})
    db.delete(db_item)
    db.commit()
    return {"message": f"Item {item_id} deleted successfully"}
