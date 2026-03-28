# routers/shop_owner.py

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from api.database.db import get_db
from api.schemas.shop_owner import ShopOwnerCreate, ShopOwnerResponse
from api.repository.shop_owner_repo import ShopOwnerRepository

router = APIRouter(prefix="/shop-owner", tags=["Shop Owner"])

repo = ShopOwnerRepository()


@router.post(
    "/",
    response_model=ShopOwnerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_shop_owner(request: ShopOwnerCreate, db: Session = Depends(get_db)):

    # 🔹 check if email exists
    existing = repo.get_by_email(db, request.email)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    try:
        # 🔹 create user (flush gives id)
        owner = repo.create(db, {
            "name": request.name,
            "email": request.email,
            "password": request.password,  # ⚠️ hash later
            "schema_name": None
        })

        # 🔹 generate schema name
        schema_name = f"schema_shop_{int(owner.id)}"

        # 🔹 create schema
        db.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"'))

        # 🔹 OPTIONAL: create tables later via SQLAlchemy
        # ShopBase.metadata.create_all(bind=db.get_bind(), schema=schema_name)

        # 🔹 update schema_name
        owner.schema_name = schema_name

        # 🔹 commit everything together
        db.commit()
        db.refresh(owner)

        return owner

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))