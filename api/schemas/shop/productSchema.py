from pydantic import BaseModel

class ProductCreateRequest(BaseModel):
    name: str
    price: float



class ProductCreateResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON
        
        
class ProductDeleteRequest(BaseModel):
    id: int
        
        
class ProductDeleteResponse(BaseModel):
    id: int
    name: str
    message: str

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON