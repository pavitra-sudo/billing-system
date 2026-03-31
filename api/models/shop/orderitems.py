from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.database.db import ShopBase


class OrderItem(ShopBase):
    __tablename__ = "order_items"; __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="orderitems")