from typing import Optional

from pydantic import BaseModel, Field, field_validator

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
    name: str
    price: float

    
    
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
        
        
class ProductPatchRequest(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
  
    
class ProductPatchResponse(BaseModel):
    id: int
    name: str
    price: float
    message: str

    class Config:
        from_attributes = True