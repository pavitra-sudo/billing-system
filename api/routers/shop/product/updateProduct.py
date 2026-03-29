from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.productSchema import  ProductUpdateRequest,   ProductUpdateResponse

router = APIRouter(prefix="/update-product", tags=["Products"])


# 🔹 helper: set schema




@router.put("/", response_model=ProductUpdateResponse, status_code=200)
def update_product(request: ProductUpdateRequest, db: Session = Depends(get_db)):

    # 🔹 Fetch product
    product = db.query(Product).filter(Product.id == request.id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # 🔹 Update fields
    product.name = request.name  # type: ignore
    product.price = request.price  # type: ignore

    # 🔹 Commit changes
    db.commit()
    db.refresh(product)

    # 🔹 Return updated object
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "message": "Product updated successfully"
    }