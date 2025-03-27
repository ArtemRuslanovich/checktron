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
        request_data = {
            "address": address,
            "bandwidth_used": info.get("bandwidth_used") if info else None,
            "bandwidth_available": info.get("bandwidth_available") if info else None,
            "energy_used": info.get("energy_used") if info else None,
            "energy_available": info.get("energy_available") if info else None,
            "trx_balance": info.get("trx_balance") if info else None
        }
        db_request = AddressRequest(**request_data)
        db.add(db_request)
        db.commit()
        return db_request

    @staticmethod
    def get_requests(db: Session, skip: int = 0, limit: int = 10):
        total = db.query(AddressRequest).count()
        requests = db.query(AddressRequest).order_by(
            AddressRequest.timestamp.desc()
        ).offset(skip).limit(limit).all()
        return {"items": requests, "total": total}
