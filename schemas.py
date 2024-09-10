from pydantic import BaseModel


class Item_Model(BaseModel):
    id: int = None
    name: str
    description: str

    class Config:
        from_attributes = True


class User_Model(BaseModel):

    id: int = None
    name: str
    age: int

    class Config:
        from_attributes = True
