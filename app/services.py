from tronpy import Tron
from tronpy.providers import HTTPProvider
from app.config import settings
from app.models import AddressRequest
from sqlalchemy.orm import Session

class TronService:
    def __init__(self):
        self.client = Tron(HTTPProvider(
            "https://api.trongrid.io" if settings.tron_network == "mainnet" 
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
    def log_request(db: Session, address: str, info: dict = None):
        db_request = AddressRequest(
            address=address,
            **info if info else {}
        )
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
