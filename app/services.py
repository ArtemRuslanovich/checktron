from tronpy import Tron
from tronpy.providers import HTTPProvider
from app.config import settings
from app.models import AddressRequest
from sqlalchemy.orm import Session

class TronService:
    def __init__(self):
        self.client = Tron(HTTPProvider(
            "https://api.trongrid.io" if settings.tron_net == "mainnet" 
            else "https://api.shasta.trongrid.io"
        ))

    def get_address_info(self, address: str):
        account = self.client.get_account(address)
        resources = self.client.get_account_resource(address)
        return {
            "address": address,
            "bandwidth_used": resources.get("NetUsed", 0),
            "bandwidth_available": resources.get("NetLimit", 0),
            "energy_used": resources.get("EnergyUsed", 0),
            "energy_available": resources.get("EnergyLimit", 0),
            "trx_balance": account.get("balance", 0)
        }

class DatabaseService:
    @staticmethod
    def log_request(db, address: str, info: dict = None):
        request = AddressRequest(
            address=address,
            bandwidth_used=info.get("bandwidth_used", 0) if info else 0,
            bandwidth_available=info.get("bandwidth_available", 0) if info else 0,
            energy_used=info.get("energy_used", 0) if info else 0,
            energy_available=info.get("energy_available", 0) if info else 0,
            trx_balance=info.get("trx_balance", 0) if info else 0
        )
        db.add(request)
        db.commit()
        return request

    @staticmethod
    def get_requests(db, skip: int = 0, limit: int = 10):
        total = db.query(AddressRequest).count()
        requests = db.query(
            AddressRequest.id,
            AddressRequest.address,
            AddressRequest.timestamp,
            AddressRequest.bandwidth_used,
            AddressRequest.bandwidth_available,
            AddressRequest.energy_used,
            AddressRequest.energy_available,
            AddressRequest.trx_balance
        ).order_by(
            AddressRequest.timestamp.desc()
        ).offset(skip).limit(limit).all()
        
        return {
            "items": requests,
            "total": total,
            "page": skip // limit + 1,
            "per_page": limit
        }
