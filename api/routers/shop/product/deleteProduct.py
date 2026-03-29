from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.productSchema import ProductDeleteRequest,   ProductDeleteResponse

router = APIRouter(prefix="/delete-product", tags=["Products"])


# 🔹 helper: set schema




@router.delete("/", response_model=ProductDeleteResponse, status_code=200)
def delete_product(request: ProductDeleteRequest, db: Session = Depends(get_db)):

    # ✅ Fetch from DB (makes it persistent)
    product = db.query(Product).filter(Product.id == request.id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # ✅ Now safe to delete
    db.delete(product)
    db.commit()
    details = product.name 

    return {
    "id": request.id,
    "name": details,
    "message": "Product deleted successfully"}