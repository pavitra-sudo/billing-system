from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.shop.product import Product
from api.schemas.shop.product import ProductCreateRequest, ProductPatchRequest ,ProductUpdateRequest


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
    
    
class ProductUpdateService:
    
    @staticmethod
    def update_product(db: Session, id: int, request: ProductUpdateRequest):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        product.name = request.name  # type: ignore
        product.price = request.price  # type: ignore
            
        db.commit()
        db.refresh(product)


        return {
            "id": id,
            "name": product.name,
            "price": product.price,
            "message": "Product updated successfully"
        }
        
        
class ProductDeleteService:
    
    @staticmethod
    def delete_product(db: Session, id: int):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")


        db.delete(product)
        db.commit()
        return 
    
class ProductPatchService:
    
    @staticmethod
    def patch_product(db: Session, id: int, request: ProductPatchRequest):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if request.name is not None:
            product.name = request.name  # type: ignore

        if request.price is not None:
            product.price = request.price  # type: ignore
            
        db.commit()
        db.refresh(product)


        return {
            "id": id,
            "name": product.name,
            "price": product.price,
            "message": "Product updated successfully"
        }