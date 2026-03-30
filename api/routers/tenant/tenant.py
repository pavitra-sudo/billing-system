from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ...database.db import get_db
from ...schemas.tenant.tenant import TenantCreate, TenantResponse
from ...services.tenant.tenant import ShopOwnerService, TenantLoginService
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from api.auth.hashing import  verify_password
from api.auth.token import create_access_token



router = APIRouter(
    prefix="/api/auth",
    tags=["Tenant Management"]
)

service = ShopOwnerService()


@router.post("/register",response_model=TenantResponse,status_code=status.HTTP_201_CREATED)
async def create_shop_owner( request: TenantCreate,db: Session = Depends(get_db)
):
    return service.create_shop_owner(db, request)


@router.post("/login", status_code=status.HTTP_200_OK)
def tenant_login(request: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    login = TenantLoginService()
    return login.tenant_login(db, request)
