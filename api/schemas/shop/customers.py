from alembic.environment import Optional
from pydantic import BaseModel, Field

class CustomerBase(BaseModel):
    name: str
    mobile_number: str = Field(..., max_length=10)


class CustomerCreateRequest(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True   
        
        
        
class CustomerPatchRequest(BaseModel):
    name: Optional[str] = None
    mobile_number: Optional[str] = Field(default=None, max_length=10)

        

