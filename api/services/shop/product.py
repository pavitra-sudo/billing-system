from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.shop.product import Product
from api.schemas.shop.product import ProductCreateRequest, ProductPatchRequest ,ProductUpdateRequest


class ProductService:
    
    # Static method to get a product by ID
    @staticmethod
    def get_product_by_id(db: Session, id: int) -> Product:
        product = (
            db.query(Product)
            .filter(Product.id == id)
            .first()
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product
    
    # Static method to get all products, with optional name filtering
    @staticmethod
    def get_all_products(db: Session,name: str | None = None) -> list[Product]:
        query = db.query(Product)
        if name is not None and name.strip():
            query = query.filter(Product.name.ilike(f"%{name.strip()}%"))

        return query.all()
    

    # Static method to create a new product
    @staticmethod
    def create_product(db: Session, request: ProductCreateRequest):
        product = Product(
        name=request.name,
        price=request.price,
        barcode=request.barcode
    )

        db.add(product)
        db.commit()
        db.refresh(product)

        return product
    
    
    # Static method to update an existing product
    @staticmethod
    def update_product(db: Session, id: int, request: ProductUpdateRequest):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        product.name = request.name  # type: ignore
        product.price = request.price  # type: ignore
        product.barcode = request.barcode  # type: ignore
            
        db.commit()
        db.refresh(product)
        product_data = {
            "id": id,
            "name": product.name,
            "price": product.price,
            "message": "Product updated successfully"}


        return product_data
        
        
    # Static method to delete a product
    @staticmethod
    def delete_product(db: Session, id: int):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")


        db.delete(product)
        db.commit()
        return 
    
    

    # Static method to partially update a product
    @staticmethod
    def patch_product(db: Session, id: int, request: ProductPatchRequest):

        product = db.query(Product).filter(Product.id == id).first()

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if request.name is not None:
            product.name = request.name  # type: ignore

        if request.price is not None:
            product.price = request.price  # type: ignore
        
        if request.barcode is not None:
            product.barcode = request.barcode  # type: ignore
            
        db.commit()
        db.refresh(product)
        
        product_data = {
            "id": id,
            "name": product.name,
            "price": product.price,
            "barcode": product.barcode,
            "message": "Product updated successfully"}
    
        return product_data