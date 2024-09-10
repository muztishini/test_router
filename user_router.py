from fastapi import APIRouter, Body
from database import User, SessionLocal
from fastapi.responses import JSONResponse
from schemas import User_Model
from typing import List


user_router = APIRouter()


@user_router.get("/", response_model=List[User_Model])
async def read_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users


@user_router.post("/")
async def create_user(data: User_Model = Body()):
    db = SessionLocal()
    db_user = User(name=data.name, age=data.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created", "data": db_user}


@user_router.get("/{user_id}", response_model=User_Model)
async def read_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return JSONResponse(status_code=404, content={"message": f"Пользователь {user_id} не найден"})
    return user


@user_router.put("/{user_id}")
async def update_user(user_id: int, data: User_Model = Body()):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return JSONResponse(status_code=404, content={"message": f"Пользователь {user_id} не найден"})
    db_user.name = data.name
    db_user.age = data.age
    db.commit()
    db.refresh(db_user)
    return {"message": f"User {user_id} updated", "data": db_user}


@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return JSONResponse(status_code=404, content={"message": f"Пользователь {user_id} не найден"})
    db.delete(db_user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}
