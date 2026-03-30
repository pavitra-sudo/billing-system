from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.services.shop.product import ProductCreateService, ProductDeleteService, ProductGetService, ProductUpdateService    
from api.schemas.shop.product import ProductCreateRequest, ProductCreateResponse, ProductGetResponse, ProductUpdateRequest, ProductUpdateResponse, ProductDeleteResponse

router = APIRouter(prefix="/api/products", tags=["Products"])



# POST /api/products/ - create product
@router.post("/", response_model=ProductCreateResponse)
def create_product(request: ProductCreateRequest, db: Session = Depends(get_db)):
    return ProductCreateService.create_product(db, request)


# DELETE /api/products/{id} - delete product

@router.delete("/{id}", response_model=ProductDeleteResponse, status_code=200)
def delete_product(id: int, db: Session = Depends(get_db)):
    return ProductDeleteService.delete_product(db, id)
    
    
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

   