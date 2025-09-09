from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .db import Base
import datetime

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String)
    phone = Column(String)
    national_id = Column(String, unique=True)
    accounts = relationship("Account", back_populates="customer")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    account_number = Column(String, unique=True, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    balance = Column(Numeric, default=0)
    customer = relationship("Customer", back_populates="accounts")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    tx_id = Column(String, unique=True, nullable=False)
    from_account = Column(String, nullable=True)
    to_account = Column(String, nullable=True)
    amount = Column(Numeric, nullable=False)
    currency = Column(String, default="SEK")
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    is_incoming = Column(Boolean, default=True)
    validated = Column(Boolean, default=False)
    suspicious = Column(Boolean, default=False)
