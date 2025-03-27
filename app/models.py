from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.sql import func
from app.db import Base

class AddressRequest(Base):
    __tablename__ = 'address_requests'
    
    id = Column(Integer, primary_key=True)
    address = Column(String(50), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    bandwidth_used = Column(BigInteger, nullable=False, server_default="0")
    bandwidth_available = Column(BigInteger, nullable=False, server_default="0")
    energy_used = Column(BigInteger, nullable=False, server_default="0")
    energy_available = Column(BigInteger, nullable=False, server_default="0")
    trx_balance = Column(BigInteger, nullable=False, server_default="0")

    def __init__(self, **kwargs):
        self.address = kwargs.get('address')
        self.bandwidth_used = kwargs.get('bandwidth_used')
        self.bandwidth_available = kwargs.get('bandwidth_available')
        self.energy_used = kwargs.get('energy_used')
        self.energy_available = kwargs.get('energy_available')
        self.trx_balance = kwargs.get('trx_balance')