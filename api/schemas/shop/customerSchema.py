from typing import Optional
from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):
    name: str
    email: str
    phone: str
    address: Optional[str] = None
    
class CustomerCreateResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True   # 👈 required for ORM → JSON