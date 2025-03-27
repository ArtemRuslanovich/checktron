from pydantic import BaseModel
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
    bandwidth_used: int | None
    bandwidth_available: int | None
    energy_used: int | None
    energy_available: int | None
    trx_balance: int | None

    class Config:
        from_attributes = True

class PaginatedResponse(BaseModel):
    items: list[AddressRequestRecord]
    total: int
    page: int
    per_page: int