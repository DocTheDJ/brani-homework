from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, Mapped
from .database import Base
import datetime

# class that represets the connection between Orders and tags
# basically many to many
class OrderTag(Base):
    __tablename__ = "order_tags",
    # primary key is here the 2 foreign keys, if either parent primary key is deleted this row is deleted too
    order_id = Column(ForeignKey("orders.id"), primary_key=True)
    tag_id = Column(ForeignKey("tags.id"), primary_key=True)
    order = relationship("Order", back_populates="tags")
    tag = relationship("Tag", back_populates="orders")

# class representation of table to store orders
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    created = Column(DateTime, default=datetime.datetime.now())
    #backrelation to get tags that are related to this order
    tags = relationship("OrderTag", back_populates="order", cascade="delete")

# class representation of table to store tags
class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    #backrelation to get to orders that use this tag
    orders = relationship("OrderTag", back_populates="tag", cascade="delete")