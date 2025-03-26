from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db import Base

class AddressRequest(Base):
    __tablename__ = "address_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    bandwidth_used = Column(Integer, nullable=True) #использовано bandwidth
    bandwidth_available = Column(Integer, nullable=True) #осталось bandwidth

    en_used = Column(Integer, nullable=True) #использовано en
    en_availible = Column(Integer, nullable=True) #осталось en

    trx_balance = Column(Integer, nullable=True) #баланс