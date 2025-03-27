from app.services import DatabaseService
from app.models import AddressRequest
from sqlalchemy import inspect

def test_db_initialization(test_db):    
    inspector = inspect(test_db)
    assert "address_requests" in inspector.get_table_names()
    
    columns = [c["name"] for c in inspector.get_columns("address_requests")]
    assert all(col in columns for col in [
        "id", "address", "timestamp", 
        "trx_balance", "bandwidth_used"
    ])

def test_log_request(db_session):
    service = DatabaseService()
    address = "random123321"

    request = service.log_request(
        db_session,
        address,
        {"trx_balance": 1000}
    )

    record = db_session.query(AddressRequest).filter(
        AddressRequest.address == address
    ).first()
    
    assert record is not None
    assert record.trx_balance == 1000