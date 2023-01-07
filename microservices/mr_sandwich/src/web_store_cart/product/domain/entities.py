from datetime import datetime
from shared.db import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from shared.ddd import AggregateRoot


class Product(Base, AggregateRoot):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    price = Column(Float)
    calories_per_100g = Column(Float)
    calories_per_serving = Column(Float)
    ingredients = Column(Text)
    weight = Column(Float)
    created_at = Column(DateTime, default=datetime.now)
