from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlmodel import Field, SQLModel

from apps.config.db import Base


class ProductDB(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)


class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: int
    quantity: int


class ProductSchema(BaseModel):
    name: str
    description: str
    price: int
    quantity: int
