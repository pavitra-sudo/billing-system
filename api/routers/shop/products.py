from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db
from api.models.shop.product import Product
from api.schemas.shop.productSchema import ProductCreateRequest, ProductCreateResponse, ProductGetResponse, ProductUpdateRequest, ProductUpdateResponse, ProductDeleteRequest, ProductDeleteResponse

router = APIRouter(prefix="/api/products", tags=["Products"])


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

@router.delete("/{id}", response_model=ProductDeleteResponse, status_code=200)
def delete_product(id: int, db: Session = Depends(get_db)):

    # ✅ Fetch from DB (makes it persistent)
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # ✅ Now safe to delete
    db.delete(product)
    db.commit()

    return {
    "id": id,
    "message": "Product deleted successfully"}
    
    
@router.patch("/{id}", response_model=ProductUpdateResponse, status_code=200)
def update_product(id: int, request: ProductUpdateRequest, db: Session = Depends(get_db)):

    # 🔹 Fetch product
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if request.name is not None:
        product.name = request.name  # type: ignore
    if request.price is not None:
        product.price = request.price  # type: ignore

    # 🔹 Commit changes
    db.commit()
    db.refresh(product)

    # 🔹 Return updated object
    return {
        "id": id,
        "name": product.name,
        "price": product.price,
        "message": "Product updated successfully"
    }
    
@router.get("/{id}", response_model=ProductGetResponse, status_code=200)
def get_product(id: int, db: Session = Depends(get_db)):

    # ✅ Fetch from DB (makes it persistent)
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # ✅ Return the product
    return product