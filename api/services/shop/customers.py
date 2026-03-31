from urllib import request

from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.models.shop.customers import Customer
from api.schemas.shop.customers import CustomerCreateRequest, CustomerPatchRequest

class CustomerService:
    
    # Static method to create a new customer
    @staticmethod
    def create_customer(db: Session, request: CustomerCreateRequest):
        customer = Customer(
            name=request.name,
            mobile_number=request.mobile_number)
        
        if db.query(Customer).filter(Customer.mobile_number == request.mobile_number).first():
            raise HTTPException(status_code=400, detail="Mobile number already exists")
        db.add(customer)
        db.flush()
        db.refresh(customer)
        return customer
    
    # Static method to get a customer by name or mobile number
    @staticmethod
    def get_all_customers(db: Session, name: str | None = None, mobile: str | None = None) -> list[Customer]:
        query = db.query(Customer)
        if name is not None and name.strip():
            query = query.filter(Customer.name.ilike(f"%{name.strip()}%"))
        if mobile is not None and mobile.strip():
            query = query.filter(Customer.mobile_number == mobile.strip())
        return query.all()
    
    @staticmethod
    def get_customer_by_id(db: Session, id: int) -> Customer:
        customer = (
            db.query(Customer)
            .filter(Customer.id == id)
            .first()
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )
            
        return customer
    
    @staticmethod
    def delete_customer(db: Session, id: int):
        customer = db.query(Customer).filter(Customer.id == id).first()

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        db.delete(customer)
        db.flush()
        return
    
        
    @staticmethod
    def patch_customer(db: Session, id: int, request: CustomerPatchRequest):
        customer = db.query(Customer).filter(Customer.id == id).first()

        if request.name is not None:
            customer.name = request.name  # type: ignore

        if request.mobile_number is not None:
            customer.mobile_number = request.mobile_number  # type: ignore
        

        db.flush()
        db.refresh(customer)
        return customer
        