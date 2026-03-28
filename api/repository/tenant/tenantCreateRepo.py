# repository/shop_owner_repo.py

from sqlalchemy.orm import Session
from api.models.tenant.tenantModel import ShopOwner


class ShopOwnerRepository:

    def get_by_email(self, db: Session, email: str) -> ShopOwner | None:
        return db.query(ShopOwner).filter(ShopOwner.email == email).first()

    def create(self, db: Session, data: dict) -> ShopOwner:
        obj = ShopOwner(**data)
        db.add(obj)
        db.flush()  # IMPORTANT: get ID without full commit
        return obj