from typing import Optional

from pydantic import BaseModel, Field

# Product Schemas

class ProductCreateRequest(BaseModel):
    name: str
    price: float
    barcode: str = Field(..., max_length=50)   


class ProductCreateResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True   
        
        
        
        
class ProductUpdateRequest(BaseModel):
    name: str
    price: float
    barcode: str = Field(..., max_length=50)   

    
    
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
    barcode: str


    class Config:
        from_attributes = True   
        
        
class ProductPatchRequest(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    barcode: Optional[str] = Field(default=None, max_length=50)
  
    
class ProductPatchResponse(BaseModel):
    id: int
    name: str
    price: float
    barcode: str
    message: str

    class Config:
        from_attributes = True