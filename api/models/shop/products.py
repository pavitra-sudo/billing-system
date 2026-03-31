from sqlalchemy import Column, Integer, String, Numeric, DateTime
from datetime import datetime
from api.database.db import ShopBase  # or PublicBase

class Product(ShopBase):
    __tablename__ = "products"
    __table_args__ = {"schema": None}  # schema will be set dynamically

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    barcode = Column(String(50), unique=True, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)