from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

from sqlalchemy.orm import relationship
from api.database.db import ShopBase  

class Customer(ShopBase):
    __tablename__ = "customers"
    __table_args__ = {"schema": None}  # schema will be set dynamically

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    mobile_number = Column(String(10), unique=True, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    orders = relationship("Orders", back_populates="customer")
    

    