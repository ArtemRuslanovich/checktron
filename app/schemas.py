from pydantic import BaseModel, Field
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
    bandwidth_used: int = Field(default=0)
    bandwidth_available: int = Field(default=0)
    energy_used: int = Field(default=0)
    energy_available: int = Field(default=0)
    trx_balance: int = Field(default=0)

    class Config:
        from_attributes = True
        extra = "ignore"

class PaginatedResponse(BaseModel):
    items: list[AddressRequestRecord]
    total: int
    page: int
    per_page: int