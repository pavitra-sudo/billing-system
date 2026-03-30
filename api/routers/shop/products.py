from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db
from api.models.shop.product import Product
from api.services.shop.product import ProductCreateService, ProductGetService, ProductUpdateService    
from api.schemas.shop.product import ProductCreateRequest, ProductCreateResponse, ProductGetResponse, ProductUpdateRequest, ProductUpdateResponse, ProductDeleteRequest, ProductDeleteResponse

router = APIRouter(prefix="/api/products", tags=["Products"])



# POST /api/products/ - create product
@router.post("/", response_model=ProductCreateResponse)
def create_product(request: ProductCreateRequest, db: Session = Depends(get_db)):
    return ProductCreateService.create_product(db, request)


@router.delete("/{id}", response_model=ProductDeleteResponse, status_code=200)
def delete_product(id: int, db: Session = Depends(get_db)):

    
    product = db.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")


    db.delete(product)
    db.commit()

    return {
    "id": id,
    "message": "Product deleted successfully"}
    
# PUT /api/products/{id} - update product

@router.put("/{id}", response_model=ProductUpdateResponse, status_code=200)
def update_product(id: int, request: ProductUpdateRequest, db: Session = Depends(get_db)):
    return ProductUpdateService.update_product(db, id, request)
    
# GET /api/products/{id} - get product by id 

@router.get("/{id}", response_model=ProductGetResponse, status_code=200)
def get_product(id: int, db: Session = Depends(get_db)):
    return ProductGetService.get_product_by_id(db, id)

# GET /api/products/ - get all products

@router.get("/", response_model=list[ProductGetResponse], status_code=200)
def get_all_products(db: Session = Depends(get_db)):
    return ProductGetService.get_all_products(db)

   