# models/shop_owner.py

from sqlalchemy import Column, Integer, String
from api.database.db import PublicBase

class ShopOwner(PublicBase):
    __tablename__ = "tenant"
    __table_args__ = {"schema": "public"}  # IMPORTANT

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    schema_name = Column(String(100), nullable=True)