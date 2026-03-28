from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

from ..repository.shop_owner_repo import ShopOwnerRepository


class ShopOwnerService:

    def __init__(self):
        self.repo = ShopOwnerRepository()

    def create_shop_owner(self, db: Session, request):
        
        # 🔹 check existing
        existing = self.repo.get_by_email(db, request.email)
        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")

        try:
            # 🔹 create user (flush → id available)
            owner = self.repo.create(db, {
                "name": request.name,
                "email": request.email,
                "password": request.password,
                "schema_name": None
            })

            # 🔹 generate schema
            schema_name = f"schema_shop_{int(owner.id)}" # type: ignore

            # 🔹 create schema
            db.execute(
                text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')
            )

            # 🔹 update schema name
            owner.schema_name = schema_name # type: ignore

            # 🔹 commit everything
            db.commit()
            db.refresh(owner)

            return owner

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))