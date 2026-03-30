from sqlalchemy import Column, Integer
from api.database.db import PublicBase

class BillCounter(PublicBase):
    __tablename__ = "bill_counter"
    __table_args__ = {"schema": "public"}  # IMPORTANT

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False)
    counter = Column(Integer,unique=True)
    password = Column(Integer, nullable=False)