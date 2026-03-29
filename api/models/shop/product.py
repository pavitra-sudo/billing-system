from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from api.database.db import ShopBase   # 👈 use your ShopBase for per-schema tables

class Product(ShopBase):
    __tablename__ = "products"
    __table_args__ = {"schema": None}  # 👈 required for dynamic schema switching

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)