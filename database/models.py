from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    referral_code = Column(String, nullable=True)
    points = Column(Integer, default=0)
    registered_at = Column(DateTime, default=datetime.datetime.utcnow)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    unit = Column(String, nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String, default="Pending")
    total_price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User")
