# schemas/shop_owner.py

from pydantic import BaseModel, EmailStr, Field


# Request Schema (input)
class TenantCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=255)


#  Response Schema (output)
class TenantResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    schema_name: str | None

    class Config:
        from_attributes = True  