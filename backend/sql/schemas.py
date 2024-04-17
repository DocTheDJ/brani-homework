from typing import Optional
from pydantic import BaseModel
import datetime

#these are basically serializers for whatever comes out of the database or tries to come in.

class OrderBase(BaseModel):
    email: str

class OrderCreate(OrderBase):
    pass

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        orm_mode=True

class Order(OrderBase):
    id: int

    class Config:
        orm_mode=True

class OrderTagBase(BaseModel):
    order_id: int
    tag_id: int

    class Config:
        orm_mode=True

class OrderTagCreate(OrderTagBase):
    pass

class OrderTagJoin(BaseModel):
    tag: Tag

class TagOrderJoin(BaseModel):
    order: Order

class OrderChildren(Order):
    tags: list[OrderTagJoin]
    created: Optional[datetime.datetime]

    class Config:
        orm_mode=True

class TagChildren(Tag):
    orders: list[TagOrderJoin]

    class Config:
        orm_mode=True
