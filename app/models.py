from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.sql import func
from app.db import Base

class AddressRequest(Base):
    __tablename__ = "address_requests"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(50), index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    bandwidth_used = Column(BigInteger, nullable=True) #использовано bandwidth
    bandwidth_available = Column(BigInteger, nullable=True) #осталось bandwidth

    en_used = Column(BigInteger, nullable=True) #использовано en
    en_availible = Column(BigInteger, nullable=True) #осталось en

    trx_balance = Column(BigInteger, nullable=True) #баланс