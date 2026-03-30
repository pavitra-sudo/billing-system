from typing import Optional

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
    message: str

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON
        
class ProductUpdateRequest(BaseModel):
    name: Optional[str]
    price: Optional[float]
    
    
class ProductUpdateResponse(BaseModel):
    id: int
    name: str
    price: float
    message: str

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON
        
        

        
class ProductGetResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON
        