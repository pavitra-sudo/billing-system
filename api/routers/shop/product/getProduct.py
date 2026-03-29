from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.productSchema import ProductGetResponse


router = APIRouter(prefix="/get-product", tags=["Products"])


# 🔹 helper: set schema




@router.get("/{id}", response_model=ProductGetResponse, status_code=200)
def get_product(id: int, db: Session = Depends(get_db)):

    # ✅ Fetch from DB (makes it persistent)
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # ✅ Return the product
    return product
    