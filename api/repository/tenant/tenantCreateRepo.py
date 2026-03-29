# repository/shop_owner_repo.py

from sqlalchemy.orm import Session
from api.models.tenant.tenantModel import Tenant 


class TenantRepository:

    def get_by_email(self, db: Session, email: str) -> Tenant | None:
        return db.query(Tenant).filter(Tenant.email == email).first()

    def create(self, db: Session, data: dict) -> Tenant:
        obj = Tenant(**data)
        db.add(obj)
        db.flush()  # IMPORTANT: get ID without full commit
        return obj