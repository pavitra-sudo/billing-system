from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float



class ProductCreateResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON