from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.productSchema import ProductCreateRequest, ProductCreateResponse

router = APIRouter(prefix="/create-product", tags=["Products"])


# 🔹 helper: set schema


@router.post("/", response_model=ProductCreateResponse)
def create_product(request: ProductCreateRequest, db: Session = Depends(get_db)):


    product = Product(
        name=request.name,
        price=request.price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product