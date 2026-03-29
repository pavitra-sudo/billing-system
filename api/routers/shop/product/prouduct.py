from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.product import ProductCreate, ProductCreateResponse

router = APIRouter(prefix="/products", tags=["Products"])


# 🔹 helper: set schema


@router.post("/", response_model=ProductCreateResponse)
def create_product(request: ProductCreate, db: Session = Depends(get_db)):


    product = Product(
        name=request.name,
        price=request.price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product