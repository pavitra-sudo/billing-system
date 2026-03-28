from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..database.db import get_db
from ..schemas.shop_owner import ShopOwnerCreate, ShopOwnerResponse
from ..services.create_shop_owner_service import ShopOwnerService

router = APIRouter(
    prefix="/shop-owner",
    tags=["Shop Owner"]
)

service = ShopOwnerService()


@router.post(
    "/",
    response_model=ShopOwnerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_shop_owner(
    request: ShopOwnerCreate,
    db: Session = Depends(get_db)
):
    return service.create_shop_owner(db, request)