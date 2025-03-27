from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class AddressInfoRequest(BaseModel):
    address: str

class AddressInfoResponse(BaseModel):
    address: str
    bandwidth_used: int
    bandwidth_available: int
    energy_used: int
    energy_available: int
    trx_balance: int

class AddressRequestRecord(BaseModel):
    id: int
    address: str
    timestamp: datetime
    bandwidth_used: int = 0
    bandwidth_available: int = 0
    energy_used: int = 0
    energy_available: int = 0
    trx_balance: int = 0
    
    model_config = ConfigDict(from_attributes=True)

class PaginatedResponse(BaseModel):
    items: list[AddressRequestRecord]
    total: int = Field(...)
    page: int = Field(1)
    per_page: int = Field(5)