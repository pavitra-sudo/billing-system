from typing import Optional

from pydantic import BaseModel

# Product Schemas

class ProductCreateRequest(BaseModel):
    name: str
    price: float



class ProductCreateResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   
        
        
        
        
class ProductDeleteResponse(BaseModel):
    id: int
    message: str

    class Config:
        from_attributes = True   
        
class ProductUpdateRequest(BaseModel):
    name: Optional[str]
    price: Optional[float]
    
    
class ProductUpdateResponse(BaseModel):
    id: int
    name: str
    price: float
    message: str

    class Config:
        from_attributes = True   
        
        

        
class ProductGetResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   
        