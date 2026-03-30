from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from api.database.db import ShopBase


class Customer(ShopBase):
    __tablename__ = "customers"
    __table_args__ = {"schema": None}  # 🔹 dynamic schema support

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    phone = Column(String(20), unique=True, nullable=False, index=True)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)