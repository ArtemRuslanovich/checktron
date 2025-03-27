from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
    bandwidth_used: Optional[int] = None
    bandwidth_available: Optional[int] = None
    energy_used: Optional[int] = None
    energy_available: Optional[int] = None
    trx_balance: Optional[int] = None

class PaginatedAddressRequests(BaseModel):
    items: list[AddressRequestRecord]
    total: int
    page: int
    per_page: int