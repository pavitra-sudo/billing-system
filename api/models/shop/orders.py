from sqlalchemy import Column, Integer, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship
from api.database.db import ShopBase


class Orders(ShopBase):
    __tablename__ = "orders"; __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")