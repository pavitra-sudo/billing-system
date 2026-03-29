from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db,set_schema
from api.models.shop.product import Product
from api.schemas.shop.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])


# 🔹 helper: set schema


@router.post("/", response_model=ProductResponse)
def create_product(request: ProductCreate, db: Session = Depends(get_db)):

    # ✅ switch schema
    set_schema(db, request.schema_name)

    product = Product(
        name=request.name,
        price=request.price
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product