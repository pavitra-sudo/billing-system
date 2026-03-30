from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.shop import product
from api.models.shop.product import Product
from api.schemas.shop.product import ProductCreateRequest 


class ProductGetService:

    @staticmethod
    def get_product_by_id(db: Session, product_id: int) -> Product:
        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product
    
    @staticmethod
    def get_all_products(db: Session) -> list[Product]:
        return db.query(Product).all()
    


class ProductCreateService:
    
    @staticmethod
    def create_product(db: Session, request: ProductCreateRequest):
        product = Product(
        name=request.name,
        price=request.price
    )

        db.add(product)
        db.commit()
        db.refresh(product)

        return product