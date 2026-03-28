from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database.db import ShopBase


# 🔹 Shop Details (1 per schema)
class ShopDetail(ShopBase):
    __tablename__ = "shop_detail"
    __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True)
    shop_name = Column(String(150), nullable=False)
    owner_name = Column(String(150))



    # relationships
    customers = relationship("Customer", back_populates="shop")
    orders = relationship("Order", back_populates="shop")


# 🔹 Customer
class Customer(ShopBase):
    __tablename__ = "customers"
    __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(150))

    shop_id = Column(Integer, ForeignKey("shop_detail.id"))

    # relationships
    shop = relationship("ShopDetail", back_populates="customers")
    orders = relationship("Order", back_populates="customer")


# 🔹 Product
class Product(ShopBase):
    __tablename__ = "products"
    __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=False)

    order_items = relationship("OrderItem", back_populates="product")


# 🔹 Order (Order History)
class Order(ShopBase):
    __tablename__ = "orders"
    __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    shop_id = Column(Integer, ForeignKey("shop_detail.id"))

    # relationships
    customer = relationship("Customer", back_populates="orders")
    shop = relationship("ShopDetail", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


# 🔹 Order Items (IMPORTANT for many-to-many)
class OrderItem(ShopBase):
    __tablename__ = "order_items"
    __table_args__ = {"schema": None}

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer, nullable=False)

    # relationships
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")