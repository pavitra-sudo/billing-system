from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import HTTPException

from api.models.tenant.tenantModel import Tenant
from api.database.db import engine, ShopBase
from api.models.shop.product import Product
from api.auth.hashing import get_password_hash
from api.middleware.schemaFetch import SchemaMiddleware





class ShopOwnerService:

    def create_shop_owner(self, db: Session, request):
        
        request.password = get_password_hash(request.password)
        
        # 🔹 check existing
        existing = db.query(Tenant).filter(
            Tenant.email == request.email
        ).first()

        if existing:
            raise HTTPException(status_code=400, detail="Email already exists")

        try:
            # 🔹 create user
            owner = Tenant(
                name=request.name,
                email=request.email,
                password=request.password,
                schema_name=None
            )

            db.add(owner)
            db.flush()

            # 🔹 create schema name
            schema_name = f"schema_shop_{owner.id}"

            # 🔹 create schema
            db.execute(
                text(f'CREATE SCHEMA IF NOT EXISTS "{schema_name}"')
            )

            # 🔹 update owner first
            owner.schema_name = schema_name  # type: ignore
            db.flush()
            db.commit()

            # ✅ IMPORTANT: commit so schema is visible

            # 🔥 now create tables (new connection can see schema)
            ShopBase.metadata.create_all(
                bind=engine.execution_options(
                    schema_translate_map={None: schema_name}
                )
            )

            db.commit()
            db.refresh(owner)

            return owner

        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))