from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.services.shop.product import ProductService
from api.schemas.shop.product import *

router = APIRouter(prefix="/api/products", tags=["Products"])



# POST /api/products/ - create product
@router.post("/", response_model=ProductCreateResponse,status_code=201)
def create_product(request: ProductCreateRequest, db: Session = Depends(get_db)):
    return ProductService.create_product(db, request)

# GET /api/products/ - get all products
@router.get("/", response_model=list[ProductGetResponse], status_code=200)
def get_all_products(db: Session = Depends(get_db),name: str | None = None):
    return ProductService.get_all_products(db,name)

# GET /api/products/{id} - get product by id 
@router.get("/{id}", response_model=ProductGetResponse, status_code=200, responses= {404: {"description": "Product not found"}})
def get_product(id: int, db: Session = Depends(get_db)):
    return ProductService.get_product_by_id(db, id)

#PATCH /api/products/{id} - full or partial update product (optional fields)
@router.patch("/{id}", response_model=ProductPatchResponse, status_code=200, responses= {404: {"description": "Product not found"}})
def partial_update_product(id: int, request: ProductPatchRequest, db: Session = Depends(get_db)):
    return ProductService.patch_product(db, id, request)

# DELETE /api/products/{id} - delete product
@router.delete("/{id}",  status_code=204,responses= {404: {"description": "Product not found"}})
def delete_product(id: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(db, id)
   