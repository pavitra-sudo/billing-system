from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database.db import get_db
from api.services.shop.customers import CustomerService
from api.schemas.shop.customers import *

router = APIRouter(prefix="/api/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(request: CustomerCreateRequest, db: Session = Depends(get_db)):
    return CustomerService.create_customer(db, request)


@router.get("/", response_model=list[CustomerResponse], status_code=200)
def get_customers(db: Session = Depends(get_db), name: str | None = None, mobile: str | None = None):
    return CustomerService.get_all_customers(db, name, mobile)

@router.get("/{id}", response_model=CustomerResponse, status_code=200, responses={404: {"description": "Customer not found"}})
def get_customer_by_id(id: int, db: Session = Depends(get_db)):
    return CustomerService.get_customer_by_id(db, id)

@router.delete("/{id}", status_code=204, responses={404: {"description": "Customer not found"}})
def delete_customer(id: int, db: Session = Depends(get_db)):
    return CustomerService.delete_customer(db, id)

@router.patch("/{id}", response_model=CustomerResponse, status_code=200, responses={404: {"description": "Customer not found"}})
def patch_customer(id: int, request: CustomerPatchRequest, db: Session = Depends(get_db)):
    return CustomerService.patch_customer(db, id, request)
