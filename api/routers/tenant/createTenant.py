from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ...database.db import get_db
from ...schemas.tenant.tenantCreateSchema import TenantCreate, TenantResponse
from ...services.tenant.tenantCreateService import ShopOwnerService

router = APIRouter(
    prefix="/create-tenant",
    tags=["Tenant Management"]
)

service = ShopOwnerService()


@router.post(
    "/",
    response_model=TenantResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_shop_owner(
    request: TenantCreate,
    db: Session = Depends(get_db)
):
    return service.create_shop_owner(db, request)