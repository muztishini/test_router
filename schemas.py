from pydantic import BaseModel


class Item_Model(BaseModel):
    id: int
    name: str
    description: str
