from typing import Optional
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    price: float
    barcode: str = Field(..., max_length=50)


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True  # required for ORM (SQLAlchemy)


class ProductCreateRequest(ProductBase):
    pass
       
        
class ProductPatchRequest(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    barcode: Optional[str] = Field(default=None, max_length=50)
  
    
